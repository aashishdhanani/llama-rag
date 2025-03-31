## Markov Decision Processes

<!-- image -->

- o MDP
- o Solving MDP
- o Value Iteration o Policy Iteration

## Outline

## Non-Deterministic Search

## Deterministic Grid World

## Stochastic Grid World

<!-- image -->

<!-- image -->

##  A maze-like problem

-  The agent lives in a grid
-  Walls block the agent's path

3

-  Noisy movement: actions do not always go as planned
-  80% of the time, the action North takes the agent North (if there is no wall there)
-  10% of the time, North takes the agent West; 10% East
-  If there is a wall in the direction the agent would have been taken, the agent stays in the same square
-  The agent receives rewards each time step
-  Small 'living' reward for nonterminal states (can be negative, -0.04)
-  Big rewards come for terminal states (good +1 or bad -1)
-  Goal: maximize sum of rewards

## Example: Grid World

<!-- image -->

Exit

## Probabilities of Reaching the Goal

From (1,1) by the action sequence [Up, Up, Right , Right , Right ], the probability of reaching the goal state at (4, 3) is 0.8 5 = 0.32768.

There is also a small chance of accidentally reaching the goal by going the other way around with probability 0.1 4  * 0.8 = 0.32776.

<!-- image -->

## Markov Decision Processes

- o An MDP is defined by:
- o A set of states s ∈ S
- o A set of actions a ∈ A
- o A transition function T(s, a, s')
- o Probability that a from s leads to s', i.e., P(s'| s, a)
- o P((3,2) | (3, 1), up) = 0.8
- o P((2,1) | (3, 1), up) = 0.1
- o P((4,1) | (3, 1), up) = 0.1
- o Also called the model or the dynamics
- o A reward function R(s, a, s')
- o Sometimes just R(s) or R(s')
- o A start state
- o Maybe a terminal state

<!-- image -->

## Video of Demo Gridworld Manual Intro

## What is Markov about MDPs?

- o 'Markovian' generally means that given the present state, the future and the past are independent
- o For Markov decision processes, 'Markovian' means action outcomes depend only on the current state

<!-- formula-not-decoded -->

- o This is just like search, where the successor function could only depend on the current state (not the history)

Andrey Markov (1856-1922)

<!-- image -->

## Policies

- o In deterministic single-agent search problems, we wanted an optimal plan, or sequence of actions, from start to a goal
- o For MDPs, we want an optimal
- policy π *: S → A
- o A policy π gives an action for each state
- o An optimal policy is one that maximizes expected utility if followed

Optimal policy for all nonterminal s

<!-- image -->

## Optimal Policies

<!-- image -->

## Utilities of State Sequences

- o What preferences should an agent have over reward sequences?
- o More or less? [1, 2, 2] [2, 3, 4] or
- o Now or later? [0, 0, 1] [1, 0, 0] or

<!-- image -->

## Discounting

- o It's reasonable to maximize the sum of rewards
- o It's also reasonable to prefer rewards now to rewards later
- o One solution: values of rewards decay exponentially

<!-- image -->

## Discounting

## o How to discount?

- o Each time we descend a level, we multiply in the discount once
- o Example: discount of 0.5
- o U([1,2,3]) = 1*1 + 0.5*2 + 0.25*3
- o U([1,2,3]) &lt; U([3,2,1])

## o Why discount?

- o Simulate human nature.
- o In Economic, ϒ is equivalent to an interest rate of 1 ϒ -1.
- o Helps our algorithms converge.

<!-- image -->

## Stationary Preferences

- o A policy that depends on the time is called nonstationary.
- o For example, if an agent starts at (3,1) and is given 3 steps, the optimal action is to go UP. But this will risk to hit the -1 state.
- o If the agent is given 100 steps, there is plenty time to take the safe route by going LEFT.
- o With a finite time, an optimal action depends on how much time is left.
- o With an infinite time, there is no reason to behave differently in the same state at different times. In this case, the optimal policy is stationary.

<!-- image -->

## IcP: Discounting

- o Given:
- o Actions: East, West, and Exit (only available in exit states a, e)
- o Transitions: deterministic
- o Q1: For   = 1, what is the optimal policy? γ
- o Q2: For   = 0.1, what is the optimal policy? γ
- o Q3: For which γ are West and East equally good when in state d?

<!-- image -->

## Solution

- o Given:
- o Actions: East, West, and Exit (only available in exit states a, e)
- o Transitions: deterministic
- o Q1: For   = 1, what is the optimal policy? γ
- o Q2: For   = 0.1, what is the optimal policy? γ
- o Q3: For which γ are West and East equally good when in state d?

<!-- image -->

| <-   | <-   | <-   |
|------|------|------|
| <-   | <-   | ->   |

<!-- formula-not-decoded -->

## Infinite Utilities?!

-  Problem: What if the game lasts forever?  Do we get infinite rewards?
-  Solutions:
-  Finite horizon: (similar to depth-limited search)
-  Terminate episodes after a fixed T steps (e.g. life)
-  Problem: gives nonstationary policies ( π depends on time left)
-  Discounting: use 0 &lt;   &lt; 1 γ

<!-- image -->

<!-- formula-not-decoded -->

-  Smaller   means smaller 'horizon' - shorter term focus. Larger  , long-term planning γ γ (future rewards still contribute significantly) 1-

<!-- formula-not-decoded -->

-  Absorbing state: guarantee that for every policy, a terminal state will eventually be reached (like 'overheated' for racing)

## Solving MDPs

- · We want to find the optimal policy π*:
- · Find best action for each state such that it maximizes the expected utility (sum of discounted rewards).
- · Methods
- · Value iteration
- · Policy iteration

<!-- image -->

## Example: Racing

- o A robot car wants to travel far, quickly.
- o Three states: Cool, Warm, Overheated.
- o Two actions: Slow Fast. ,

<!-- image -->

## Racing Search Tree

<!-- image -->

## Racing Search Tree

## o Problem: States are repeated

- o Idea: Only compute needed quantities once
- o Problem: Tree goes on forever
- o Idea: Do a depth-limited computation, but with increasing depths until change is small
- o Note: deep parts of the tree eventually don't matter if γ &lt; 1

<!-- image -->

## MDP Search Trees

<!-- image -->

## Optimal Quantities

##  The value (utility) of a state s:

V * (s) = expected utility starting in s and acting optimally

##  The value (utility) of a q-state (s,a):

- Q * (s,a) = expected utility starting out having taken action a from state s and (thereafter) acting optimally

##  The optimal policy:

- π * (s) = optimal action from state s

<!-- image -->

## Snapshot of Demo - Gridworld V Values

<!-- image -->

Noise = 0.2 Discount ϒ = 0.9 Living reward r = 0

## Snapshot of Demo - Gridworld Q Values

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

## Values of States - Bellman Equation

- o Recursive definition of value:

<!-- formula-not-decoded -->

Expected Utility of an action a

The action that has the max expected utility

## Time-Limited Values

- o Key idea: time-limited values
- o Define V k (s) to be the optimal value of s if the game ends in k more time steps
- o k is the number of the time steps remaining in the future.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

T         R

ϒ

V(4,3)

V*(3,3)=0.8

×

[0 + 0.9

×

(+1)] = 0.72

k=2

Gridworld Display

0 .00

AFTER

2

ITERATIONS

VALUES

Noise = 0.2

Discount = 0.9

Living reward = 0

3

2

1

VALUES

(2,3)

0

0.1

×

[0 + 0.9

×

0.8

0] = 0

×

Gridworld Display

[0 + 0.9

0.09

0.8

0.1

(3,3)

0

×

0.1

1.00

AFTER

2

IIERATIONS

×

(4,3)

0

0] = 0

[0 + 0.9

×

1] = 0.09

0+0+0.09= 0.09

0.1

Up

(2,3)

0

0.1

(3, 3)

0.72

Down

0.09

0.8 0.1

(3,2)

(4,3)

0

0

0.1

×

V*(3,3) = 0.72, a = Right.

Right

Left

0.72

0.8

0.1

(4,3)

0.1

(3,3)

0

[0 + 0.9

×

0.8

×

0

0] = 0

[0 + 0.9

×

0.1

(3,2)

0

(3,3)

0

1] = 0.72

×

[0 + 0.9

×

0] = 0

0+0.72+0= 0.72

0.1

×

[0 + 0.9

×

0] = 0

0.8

×

[0 + 0.9

×

0.1

×

0

0.8 0.1

(2,3)

0

(3, 2)

0

0] = 0

[0 + 0.9

×

0] = 0

0+0+0= 0

0.1

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

## k=5

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

## k=9

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

## k=10

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

## k=11

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

## k=12

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

## k=100

Noise = 0.2 Discount = 0.9 Living reward = 0

<!-- image -->

## Computing Time-Limited Values

<!-- image -->

## Value Iteration

Idea: Find the optimal policy by iteratively updating the value function by the Bellman equation.

<!-- image -->

## Value Iteration

- o Start with V (s) = 0: no time steps left means an expected reward sum of zero 0
- o Given vector of V (s) values, do one ply of k Value Iteration from each state:

<!-- formula-not-decoded -->

- o Stopping condition: when the max difference between two successive value function estimates is below a small threshold.
- o Complexity of each iteration: O( s a 2 )
- o each state is O( sa )
- o iterate for   states s
- o so the total is O( s a 2 )
- o Theorem: will converge to unique optimal values
- o Basic idea: approximations get refined towards optimal values
- o Policy may converge long before values do

<!-- image -->

## Example: Value Iteration

<!-- image -->

## Example: Value Iteration

<!-- image -->

## Example: Value Iteration

<!-- image -->

## Example: Value Iteration

<!-- image -->

<!-- formula-not-decoded -->

## Example: Value Iteration

<!-- image -->

2

<!-- image -->

0

Fast                 Slow

γ =1 Assume no discount!

<!-- image -->

<!-- formula-not-decoded -->

## Policy Extraction

<!-- image -->

## Computing Actions from Values

- o Let's imagine we have the optimal values V*(s)
- o How should we act?
- o It's not obvious!
- o We need to do an expectimax (one step):

<!-- image -->

<!-- formula-not-decoded -->

- o This is called policy extraction, since it gets the policy implied by the values.

## Computing Actions from Q-Values

- o Let's imagine we have the optimal q-values.
- o How should we act?
- o Completely trivial to decide!

<!-- formula-not-decoded -->

<!-- image -->

- o Important lesson: actions are easier to select from q-values than values!

## Convergence

- o How do we know the V k  vectors are going to converge?
- o Case 1 : If γ= 1 (no discount), the tree has maximum depth M, then V M holds the actual untruncated values.

## o Case 2 : If γ&lt; 1 (discounting)

- o Sketch: For any state V  and V k k+1 can be viewed as depth k+1 results in nearly identical search trees.
- o The difference is that on the bottom layer, V k+1 has actual rewards while V  has zeros. k
- o That last layer is at best all R MAX  , at worst R MIN .
- o But everything is discounted by γ k  that far out.
- o So V k and V k+1 are at most γ k  max|R| different.
- o So as k increases, the values converge.

<!-- image -->

## Value Iteration Algorithm

Input

: MDP M={S, A, T(s, a, s'), R(s, a, s')}

*

Output : Optimal policy π

Set V to arbitrary value function, e.g., V(s)=0 for all s.

Repeat

∆ = 0 //value difference between Vk+1 and Vk for each s ∈ S

<!-- formula-not-decoded -->

Until ∆ &lt; θ

<!-- formula-not-decoded -->

Output an optimal policy π * such that

<!-- formula-not-decoded -->

## Let's Think

- o Take a minute, think about value iteration.
- o What is the biggest question you have about it?

## Problems with Value Iteration

- o Value iteration repeats the Bellman updates:

<!-- formula-not-decoded -->

- o Problem 1: It's slow - O( s a 2 ) per iteration (k iterations)
- o Problem 2: The 'max action' at each state rarely changes
- o Problem 3: The policy often converges long before the values

<!-- image -->

k=12                                k=100

<!-- image -->

## Policy Iteration

- o Alternative approach for optimal values:
- o Step 1: Policy evaluation: calculate utilities for some fixed policy (not optimal utilities!) until convergence.
- o Step 2: Policy improvement: update policy using one-step look-ahead with resulting converged (but not optimal!) utilities as future values.
- o Repeat steps until policy converges.
- o This is policy iteration.
- o It's still optimal!
- o Can converge (much) faster under some conditions.

## Fixed Policies

<!-- image -->

- o Search trees max over all actions to compute the optimal values.
- o If we fixed some policy π (s), then the tree would be simpler - only one action per state.
- o … though the tree's value would depend on which policy we fixed.

## Utilities for a Fixed Policy

- o Another basic operation: compute the utility of a state s under a fixed (generally non-optimal) policy.
- o Define the utility of a state s, under a fixed policy π : V (s) = expected total discounted rewards starting in s and following π π
- o Recursive relation (Bellman equation with a fixed policy π ):

<!-- image -->

<!-- formula-not-decoded -->

## Policy Evaluation

- o How do we calculate the Vs for a fixed policy π ?
- o

<!-- formula-not-decoded -->

- o Without the maxes, the Bellman equations are just a linear system.
- o Efficiency: O(S 2 ) per iteration because a=1 (one action per state).

<!-- image -->

## Example: Policy Evaluation

Always Go Right

Always Go Forward

<!-- image -->

## Example: Policy Evaluation

<!-- image -->

## Policy Iteration

<!-- image -->

## Policy Iteration

- Evaluation: For fixed current policy π , find values with policy evaluation:
- o o Iterate until values converge:

<!-- formula-not-decoded -->

- o Improvement: For fixed values, get a better policy using policy extraction o One-step look-ahead:

<!-- formula-not-decoded -->

## Policy Iteration Algorithm

```
Policy Iteration (using iterative policy evaluation) for estimating " 1. Initialization 2. Policy Evaluation v < V(s) V(s) 3 until 4 < 0 (a small positive number determining the accuracy of estimation) 3. Policy Improvement policy-stable < true For each s € S: old-action T(s) T(s) argmax If old-action = T(s) then policy-stable < false If policy-stable. then and return V ~ and T ~ T.; else go to 2 Loop: Loop stop U*
```

## Comparison

- o Both value iteration and policy iteration compute the same thing (all optimal values).
- o In value iteration:
- o Every iteration updates both the values and (implicitly) the policy.
- o We don't track the policy, but taking the max over actions implicitly recomputes it.
- o In policy iteration:
- o We do several passes that update utilities with fixed policy (each pass is fast because we consider only one action, not all of them).
- o After the policy is evaluated, a new policy is chosen (slow like a value iteration pass).
- o The new policy will be better (or we're done).

## Summary: MDP Equations

- o Bellman Equation
- o Value iteration equation:

<!-- formula-not-decoded -->

- o Policy evaluation equation:

<!-- formula-not-decoded -->

- o Policy improvement equation:

<!-- formula-not-decoded -->

## Summary: MDP Algorithms

## o So you want to….

- o Compute optimal values: use value iteration or policy iteration.
- o Compute values for a particular policy: use policy evaluation.
- o Turn your values into a policy: use policy extraction.

## o These all look the same!

- o They are all variations of Bellman Equation.
- o They all use one-step lookahead max expected utility (MEU) fragments.
- o They differ only in whether we plug in a fixed policy or max over actions.