# Backtracking 

The idea of backtracking is simple. Find the solution with many small steps, for  each step, if it works then proceed, otherwise go back. Beforehead, the problem consists usually finite number of states to computation. That is backtracking is a kind of algorithm to solve problem with more space by moving from one state to another.

In general, there are few steps.

- Find what choice(s) we have at each step. What different options are there for the next step?
For each valid choice:
- Make it and explore recursively. Pass the information for a choice to the next recursive call(s).
- Undo it after exploring. Restore everything to the way it was before making this choice.
- Find our base case(s). What should we do when we are out of decisions?

Practicing types of backtracking problems
- Find all solutions
- Find any solution
- How many solutions are there?
- Does a solution exist?
- Find the best solution

## Related Coding Challenges 
### Subset Sum 

- Given a taget sum value and a array of numbers.
- Return a Boolean value to determine if there's a sum of subset is target value.

### N queens

Solution can be found at leetcode challenges.

- Place N queens at N Chessboard so that they won't attack each other.
- Return or print the places.

### Permutation

- Print or return all permutation result of a arraay or mathmatical result.

### Combination

- Print or return all combination result of a arraay or mathmatical result.

### Combination Sum
TODO

### Combination Sum two
TODO
