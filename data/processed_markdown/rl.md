## Reinforcement Learning

<!-- image -->

## Outline

- o Offline Planning vs Online Learning
- o Markov Decision Processes is a planning
- o Reinforcement Learning is a learning
- o What is Reinforcement Learning
- o Solving an RL problem
- o Model-Based Learning
- o Model-Free Learning
- o Temporal-Difference learning
- o Q-Learning

## Double Bandits - Planning vs. Learning

1.00  $1

0.75  $2

0.25  $0

EU: 0.75 × 2 + 0.25 ×  0 = 1.5

<!-- image -->

EU: 1.00 × 1 = 1

## Offline Planning (MDP)

o

States: Win, Lose

o

Actions: Blue, Red

<!-- image -->

No discount ( ϒ =1) 100 steps (k=100)

## Let's Play!

## o Solving MDP is offline learning

- o You need to know the details of the MDP
- o You determine all quantities through computation
- o You don't actually play the game.

<!-- image -->

$1 $1

$1

$1 $1

- o Play Red, value = 2.
- o Play Blue, value = 1.
- o Optimal policy is to play Red.

<!-- image -->

……100 steps

$2 $0 $0 $0 $0 …… 100 steps

## Online Learning

- o Rules changed!  Red's win chance is unknown.

<!-- image -->

$1 $1 $1 $1 $1

<!-- image -->

……

## Let's Play!

<!-- image -->

$2 $0 $0 $0 $0 ……

Try it again and again (sampling)

## What Is Reinforcement Learning?

## o It isn't a planning, it is a learning!

- o Specifically, reinforcement learning.
- o There was an MDP, but you couldn't solve it with just computation because you don't know some parameters in the MDP.
- o You needed to actually act to figure it out.

## o Important ideas in reinforcement learning that came up

- o Exploration: you have to try unknown actions to find out how good/bad they are.
- o Exploitation: if you know they are good, you have to use what you know to collect more rewards from them.
- o Sampling: because of chance, you have to try things repeatedly.
- o Difficulty: learning can be much harder than solving a known MDP.

## Reinforcement Learning

- o Still assume a Markov decision process (MDP):
- o A set of states s ∈ S
- o A set of actions (per state) a ∈ A
- o A model T(s,a,s')
- o A reward function R(s,a,s')
- o Still looking for a policy π (s)
- o
- New twist: don't know T or R
- o I.e. we don't know which states are good or what the actions do
- o Must actually try actions and states out to learn

<!-- image -->

<!-- image -->

<!-- image -->

## Reinforcement Learning

<!-- image -->

## o Basic idea:

- o Receive feedback in the form of rewards.
- o Agent's utility is defined by the reward function.
- o Must (learn to) act so as to maximize expected rewards.
- o All learning is based on observed samples of outcomes!

## The Crawler!

<!-- image -->

Two angles (states) +r for moving right -r for moving left

## Video of Demo Crawler Bot

## Model-Based Learning

<!-- image -->

## Model-Based Learning

## o Model-Based Idea:

- o Learn an approximate model based on experiences.
- o Solve for values as if the learned model were correct.
- o Step 1: Learn empirical MDP model
- o Count outcomes s' for each (s, a).
- o Normalize to give an estimate of                   .
- o Discover each when we experience (s, a, s').

<!-- image -->

## o Step 2: Solve the learned MDP

- o For example, use value iteration, as before.

<!-- image -->

## Example: Model-Based Learning

Input Policy π

## Observed Episodes (Training)

## Learned Model

Episode 1

Episode 2

B, east, C, -1

C, east, D, -1

D, exit,  x, +10

Episode 3

E, north, C, -1

C, east,   D, -1

D, exit,    x, +10

B, east, C, -1

C, east, D, -1

D, exit,  x, +10

## Episode 4

E, north, C, -1

C, east,   A, -1

A, exit,    x, -10

<!-- formula-not-decoded -->

R(s,a,s').

R(B, east, C) = -1

R(C, east, D) = -1

R(C, east, A) = -1

R(D, exit, x) = +10

R(A, exit, x) = -10

<!-- image -->

Assume: γ = 1

## Analogy: Expected Age

Goal: Compute expected age of CSCI-3344 students

Without P(A), instead collect samples [a , a , … a 1 2 N ]

Why does this work?  Because eventually you learn the right model.

## Answer

Goal: Compute expected age of CSCI-3344 students

Without P(A), instead collect samples [a , a , … a 1 2 N ]

## Unknown P(A): 'Model Based'

Unknown P(A): 'Model Free'

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Why does this work?  Because samples appear with the right frequencies.

## Model-Free Learning

<!-- image -->

## Passive Reinforcement Learning

- o Simplified task: policy evaluation
- o Input: a fixed policy π (s).
- o You don't know the transitions T(s,a,s').
- o You don't know the rewards R(s,a,s').
- o Goal: learn the state values.

## o In this case:

- o Learner is 'along for the ride'.
- o No choice about what actions to take.
- o Just execute the policy and learn from experience.
- o This is NOT offline planning!  You learn the state values from actual experience.

<!-- image -->

## Direct Evaluation

- o Goal: Compute values for each state under π .
- o Idea: Average together observed sample values.
- o Act according to π .
- o Every time you visit a state, write down what the sum of discounted rewards turned out to be.
- o Average those samples.
- o This is called direct evaluation.

<!-- image -->

## Example: Direct Evaluation

Input Policy π

<!-- image -->

Assume: γ = 1

## Observed Episodes (Training)

Episode 1

Episode 2

B, east, C, -1

C, east, D, -1

D, exit,  x, +10

Episode 3

E, north, C, -1

C, east,   D, -1

D, exit,    x, +10

B, east, C, -1

C, east, D, -1

D, exit,  x, +10

Episode 4

E, north, C, -1 C, east,   A, -1 A, exit,    x, -10

Output Values

<!-- image -->

## Problems with Direct Evaluation

## o What's good about direct evaluation?

## Output Values

- o It's easy to understand
- o It doesn't require any knowledge of T, R
- o It eventually computes the correct average values, using just sample transitions

## o What bad about it?

- o It wastes information about state connections
- o Each state must be learned separately
- o So, it takes a long time to learn

If B and E both go to C under this policy, how can their values be different?

<!-- image -->

## Why Not Use Policy Evaluation?

- o Simplified Bellman updates calculate V for a fixed policy:
- o Each round, replace V with a one-step-look-ahead layer over V.

<!-- formula-not-decoded -->

- o This approach fully exploited the connections between the states
- o Unfortunately, we need T and R to do it!
- o Key question: how can we do this update to V without knowing T and R?
- o In other words, how do we take a weighted average without knowing the weights?

<!-- image -->

## Sample-Based Policy Evaluation?

- o We want to improve our estimate of V by computing these averages:

<!-- formula-not-decoded -->

- o Idea: Take samples of outcomes s' (by doing the action!) and average

<!-- formula-not-decoded -->

<!-- image -->

<!-- formula-not-decoded -->

## Temporal Difference Learning

## o Big idea: learn from every experience!

- o Update V(s) each time we experience a transition (s, a, s', r)
- o The later samples will contribute updates more often b/c they are more accurate)

## o Temporal difference learning of values

- o Policy still fixed, still doing evaluation!
- o Move values toward value of whatever successor occurs: running average

Sample of V(s):

sample R(s, T(s), 8') + ~VT (s'

Update to V(s):

Same update:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Error (temporal difference)

α is called the learning rate , determining how fast/slow to learn from the temporal difference

<!-- image -->

## Learning Rate α

- o Learning rate (α) determines how much new information overrides old knowledge.
- o It controls the weight given to new experiences in reinforcement learning.
- · If α=1: You fully trust the most recent experience and completely overwrite the old value.
- · If α=0: You ignore the new information and keep the value unchanged.
- · If α ∈ (0,1) : You take a weighted average between the old value and the new estimate.

## Learning Rate α

- o Small α (e.g. 0.01): Slow learning, stable updates, but takes longer to converge.
- o Large α (e.g. 0.9): Fast learning, reacts quickly to new data, but can be unstable or noisy.
- o A decaying learning rate (e.g. α t = 1 1+𝑡𝑡 ) is often used to learn quickly at first and become more stable over time. Need careful tuning.

## Example: Temporal Difference Learning

<!-- image -->

## Problems with TD Value Learning

- o TD value leaning is a model-free way to do policy evaluation, mimicking Bellman updates with running sample averages.
- o However, if we want to turn values into a (new and better) policy, we're sunk:

<!-- formula-not-decoded -->

s

- o Idea: learn Q-values, not V values.
- o Makes action selection model-free too!
- o This is called Q Learning.

<!-- image -->

## Video of Demo Q-Learning -- Gridworld

## Detour: Q-Value Iteration

- o Value iteration: find successive (depth-limited) values.
- o Start with V (s) = 0 0
- o Given V k , calculate the depth k+1 values for all states:

<!-- formula-not-decoded -->

- o But Q-values are more useful, so compute them instead.
- o Start with Q (s,a) = 0. 0
- o Given Q k , calculate the depth k+1 q-values for all q-states:

<!-- formula-not-decoded -->

<!-- image -->

## Q-Learning

- o Q-Learning: sample-based Q-value iteration.

<!-- formula-not-decoded -->

- o Learn Q(s,a) values as you go:
- o Receive a sample (s,a,s',r).
- o Consider your old estimate:             .
- o Consider your new sample estimate:

<!-- formula-not-decoded -->

- o Incorporate the new estimate into a running average:

<!-- formula-not-decoded -->

<!-- image -->

## Video of Demo Q-Learning -- Crawler

- Q-Learning:

## act according to current optimal (and also explore…)

- o Full reinforcement learning: optimal policies (like value iteration).
- o You don't know the transitions T(s,a,s').
- o You don't know the rewards R(s,a,s').
- o You choose the actions now.
- o Goal: learn the optimal policy / values.

## o In this case:

<!-- image -->

- o Learner makes choices!
- o Fundamental tradeoff: exploration vs. exploitation.
- o This is NOT offline planning!  You actually take actions in the world and find out what happens…

## Q-Learning Properties

- o Amazing result: Q-learning converges to optimal policy -even if you're acting suboptimally (you just need to act frequently enough)!
- o This is called off-policy learning.
- o Caveats:
- o You have to explore enough.
- o You have to eventually make the learning rate small enough.
- o … but not decrease it too quickly.
- o Basically, in the limit, it doesn't matter how you select actions (!)

<!-- image -->

## Q-Learning Algorithm

<!-- image -->

## ɛ -Greedy Action Selection

Exploration allows an agent to improve its current knowledge about each action, hopefully leading to longterm benefit. Improving the accuracy of the estimated action-values, enables an agent to make more informed decisions in the future.

Exploitation on the other hand, chooses the greedy action to get the most reward by exploiting the agent's current action-value estimates. But by being greedy with respect to action-value estimates, may not actually get the most reward and lead to sub-optimal behaviour.

When an agent explores, it gets more accurate estimates of action-values. And when it exploits, it might get more reward. It cannot, however, choose to do both simultaneously, which is also called the explorationexploitation dilemma.

## ɛ -Greedy Action Selection

Epsilon-Greedy is a simple method to balance exploration and exploitation by choosing between exploration and exploitation randomly. For example, if ɛ=0.9, 90% of the chance to choose Exploitation (max Q) and 10% to choose Exploration (another action).