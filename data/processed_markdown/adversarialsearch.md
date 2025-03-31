## Adversarial Search

## Outline

- · Games
- · Minimax search (foundation)
- · α β -pruning (adding intelligence into Minimax)

## Games vs. search problems

- · "Unpredictable" opponent  specifying a move for every possible opponent reply
- · Time limits  unlikely to find goal, must approximate
- · Game tree: 2-player, deterministic, turns.
- · Formulate game problems
- - Initial state: the board position and identifies the player to move.
- - Successor function: return a list of (move, state) pairs.
- - Goal test: determine terminal states (where the game has ended).
- - Utility function: give a numeric value for each terminal state.

## Game Tree of Tic-tac-toe

<!-- image -->

## Minimax

- · Perfect play for deterministic games.
- · Ideas
- - assume the opponent always chooses a move that minimizes the desirability of states (from my perspective).
- - The heuristic evaluation at level i depends on the move (by the other player) at level i+1.

## Minimax algorithm

- · Perform a fix-level look ahead (depth-first) search.
- · Evaluate the heuristic values of leaf nodes.
- · Back up the heuristic values from the leaf nodes to the root by choosing the maximal values when it's turn, and choosing the minimal values when it's opponent's turn.

## Example

E.g., 2-ply game:

<!-- image -->

## Result

E.g., 2-ply game:

<!-- image -->

## Properties of minimax

## (DFS)

- · Complete? Yes (if tree is finite)
- · Optimal? Yes (against an optimal opponent)
- · Time complexity? O(b m )
- · Space complexity? O(bm) (depth-first exploration)
- · For chess, b ≈ 35, m ≈ 100 for "reasonable" games  exact solution completely infeasible

## α β -Pruning

- · Each MAX node (your ply) has an α value to keep track of the current maximum of its back-up values.
- · Each MIN node (opponent's ply) has a β value to keep track of the current minimum of its back-up values.
- · Use α and β values to detect two kinds of opportunities for pruning the search tree without affecting the root node's decision.
- -α cutoff (cut min)
- -β cutoff (cut max)

## α cutoff

- · When  value of a MIN node  α value of an ancestor MAX node, all branches below the MIN node can be pruned.

<!-- image -->

##  cutoff

- · When   value of a MAX node α   value of an ancestor MIN node, all branches below the MAX node can be pruned.

<!-- image -->

## α β -pruning example

<!-- image -->

## α β -pruning example (cont'd)

<!-- image -->

## α β -pruning example (cont'd)

<!-- image -->

## α β -pruning example (cont'd)

<!-- image -->

## Why is it called α β -?

- · α is the value of the best (i.e., highestvalue) choice found so far at any choice point along the path for max
- · If v is worse than α , max will avoid it  prune that branch
- · Define β similarly for min

<!-- image -->

## Properties of α β -

- · Back up values from an intermediate node if
- - All children of the node has the values sent up - An α cut or a β cut is detected at the node
- · Pruning does not affect final result
- · Good move ordering improves effectiveness of pruning
- - With 'best first', time complexity = O(b m/2 )  b 1/2 breadth of search
- - With 'random walk', time complexity = O(b 3m/4 )

## Deterministic games in practice

- · Checkers: Chinook ended 40-year-reign of human world champion Marion Tinsley in 1994. Used a precomputed endgame database defining perfect play for all positions involving 8 or fewer pieces on the board, a total of 444 billion positions.
- · Chess: Deep Blue defeated human world champion Garry Kasparov in a six-game match in 1997. Deep Blue searches 200 million positions per second, uses very sophisticated evaluation, and undisclosed methods for extending some lines of search up to 40 ply.
- · Othello: human champions refuse to compete against computers, who are too good.
- · Go: AlphaGo Master defeated Ke Jie, current world No. 1 ranking player, by three to zero in 2017. In go, b &gt; 300 , so most programs use pattern knowledge bases to suggest plausible moves.

## Summary

- · Games are fun to work on!
- · They illustrate several important points about AI.
- · Perfection is unattainable  must approximate.
- · Good idea to think about what to think about.