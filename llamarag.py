import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
from docling.document_converter import DocumentConverter
from langchain.schema import Document
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from operator import itemgetter 

load_dotenv()

CLAUDE_KEY = os.getenv("CLAUDE_KEY")
#MODEL = "claude-3-7-sonnet-20250219"
MODEL = "llama3.1"

if MODEL.startswith("claude"):
    llm = ChatAnthropic(model=MODEL, api_key=CLAUDE_KEY)
else:
    llm = OllamaLLM(model=MODEL)
    embeddings = OllamaEmbeddings(model=MODEL)
    
    
#llm.invoke("tell me a joke")
parser = StrOutputParser()
chain = llm | parser
#chain.invoke("tell me a joke")


#--------------------------------------------DATA PREPARATION ------------------------------------------
converter = DocumentConverter()

def load_pdfs(path):
    documents = []
    ctr = 1

    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(path, filename)

            result = converter.convert(file_path)
            content = result.document.export_to_markdown()

            doc = Document(
                page_content = content,
                metadata = {"source": file_path}
            )

            print(f"File {ctr}: {filename} loaded.")
            ctr += 1
            documents.append(doc)
    return documents

all_documents = load_pdfs("data/preprocessed")
print(len(all_documents)) #lengh of all the pdfs (should be 10)


def export_markdown_files(documents, output_dir="data/processed_markdown"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    for doc in documents:
        # Get the original filename from the source path
        file_path = doc.metadata["source"]
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Create markdown file path
        markdown_path = os.path.join(output_dir, f"{base_name}.md")
        
        # Write content to markdown file
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(doc.page_content)
        
        # Update metadata to include markdown path
        doc.metadata["markdown_path"] = markdown_path
        
        print(f"Exported: {markdown_path}")
    
    return documents

all_documents = export_markdown_files(all_documents)


def count_characters(documents):
    char_counts = {}
    
    for doc in documents:
        source = doc.metadata.get("source", "Unknown")
        char_count = len(doc.page_content)
        char_counts[source] = char_count
        
        # Print as we go
        print(f"{os.path.basename(source)}: {char_count} characters")
    
    return char_counts

char_counts = count_characters(all_documents)


def split_documents_by_structure(documents):
    # First try to split by markdown headers
    headers_to_split_on = [
        ("#", "section"),
        ("##", "subsection"),
        ("###", "subsubsection"),
    ]
    header_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    
    # For additional splitting of large sections
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,  # Larger than default since these are educational materials
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    
    all_splits = []
    
    for doc in documents:
        # Try header splitting first
        try:
            header_splits = header_splitter.split_text(doc.page_content)
            
            # Check if any splits are still too large
            final_splits = []
            for split in header_splits:
                if len(split.page_content) > 2000:  # If section is still large
                    smaller_splits = text_splitter.split_documents([Document(
                        page_content=split.page_content,
                        metadata={**doc.metadata, **split.metadata}
                    )])
                    final_splits.extend(smaller_splits)
                else:
                    final_splits.append(Document(
                        page_content=split.page_content,
                        metadata={**doc.metadata, **split.metadata}
                    ))
                    
            all_splits.extend(final_splits)
            
        except Exception as e:
            # Fallback to regular splitting if header splitting fails
            print(f"Header splitting failed for {doc.metadata.get('source')}, using regular splitting")
            regular_splits = text_splitter.split_documents([doc])
            all_splits.extend(regular_splits)
    
    return all_splits

all_splits = split_documents_by_structure(all_documents)
len(all_splits)
#--------------------------------------------DATA PREPARATION ------------------------------------------




#--------------------------------------------Creating RAG component ------------------------------------------

template = """You are an AI study assistant designed to help students with questions about their course materials. Your primary function is to provide accurate answers based solely on the information contained in the retrieved chunks of course documents. It is crucial that you do not add any information from your own knowledge or make up any details that are not explicitly stated in the provided text.

Here are the retrieved chunks of course material:
<context>
{context}
</context>

The student has asked the following question:
<student_question>
{question}
</student_question>

To answer the student's question, follow these steps:
1. Carefully read and analyze the retrieved chunks of text.
2. Identify any information directly relevant to the student's question.
3. Formulate an answer using only the information found in the retrieved chunks.
4. If you find conflicting information in different chunks, state this clearly in your answer.

Format your response as follows:
1. Begin with a <relevant_info> tag, where you will list the specific pieces of information from the chunks that are relevant to answering the question. Include the chunk number or identifier for each piece of information.
2. Follow this with your <answer> tag, where you will provide a clear and concise answer to the student's question based solely on the information you listed in the relevant_info section.

It is imperative that you only use information explicitly stated in the retrieved chunks. Do not add any additional information, explanations, or examples that are not present in the provided text, even if you believe them to be true or helpful.

If the question cannot be fully answered using only the information in the retrieved chunks, state this clearly in your answer. Provide whatever partial information you can from the chunks, and explain what specific information is missing to fully answer the question.

If the retrieved chunks contain no information relevant to the student's question, respond with:
<answer>I apologize, but I couldn't find any information in the provided course materials that answers your question about [brief restatement of the question]. If you believe this topic should be covered in your course, you may want to consult your instructor or additional course resources.</answer>

Remember, your role is to assist based strictly on the course materials provided, not to be a general knowledge resource. Accuracy and adherence to the given information are your top priorities."""

prompt = PromptTemplate.from_template(template)
print(prompt.format(context="Here is some context", question="here is a question") )

chain = prompt | llm | parser 

# chain.invoke(
#     {
#         "context": "The name I was given was Ant Man",
#         "question": "What is my name?",
#     }
# )

vectorstore = FAISS.from_documents(
    all_splits,
    embeddings
)

# Create keyword-based retriever
bm25_retriever = BM25Retriever.from_documents(all_splits)
bm25_retriever.k = 3  # Return top 3 keyword matches

# Create vector retriever from your FAISS index
vector_retriever = vectorstore.as_retriever()

# Combine them into a hybrid retriever
hybrid_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.5, 0.5]
)

# hybrid_retriever.invoke("PEAS")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    {
        "context": itemgetter("question") | hybrid_retriever | format_docs,
        "question": itemgetter("question")
    }
    | prompt
    | llm
    | parser
)

# chain.invoke({"question": "What does PEAS stand for?"})

#type in your question here
for s in chain.stream({"question": "What is the search method BFS?"}):
    print(s, end="", flush=True)






