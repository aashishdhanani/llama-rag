# llama-rag

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline that enhances language model responses by retrieving relevant information from a document collection. The system uses a hybrid retrieval approach, combining semantic (embedding-based) and lexical (keyword-based) search methods.

## Features

- **Document Processing**: Convert, split, and store documents for efficient retrieval
- **Hybrid Retrieval**: Combines vector-based (FAISS) and keyword-based (BM25) retrieval methods
- **Multiple LLM Support**: Works with both Claude (Anthropic) and Ollama models
- **Customizable Prompting**: Structured prompt templates for effective context integration

## Installation

1. Clone the repository
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Set up environment variables in `.env`:
```
ANTHROPIC_API_KEY=your_api_key_here
```
