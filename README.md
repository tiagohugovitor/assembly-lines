# Assembly Lines Algorithms Comparison

This project implements and compares different algorithms for assembly line scheduling problem. It includes a recursive algorithm using brute force and other algorithm using dynamic programming technique.

## Project Context

This project was part of an assignment for the Analysis of Algorithms course in the Master's program in Computer Science at the Federal University of Uberlândia (UFU). The presentation file can be found in 'assembly-lines.pdf' (presentation in Portuguese).

## Algorithms Implemented

1. **Recursive Algorithm with Brute Force**
   - Calculates the best path between two assembly lines to get to the end of the line faster.

2. **Dynamic Programming Algorithm**
   - Uses dynamic programming to calculate the best path between two assembly lines, adding a new structure to avoid recalculating subproblems.

## Files

- **assemblyLinesBruteForce.py**: Implementation of the recursive brute force algorithm.
- **assemblyLinesDynamicProgramming.py**: Implementation of the dynamic programming algorithm.
- **compareAlgorithms.py**: Script to compare the execution time of all algorithms across a range of input sizes.

## Running the Code

1. Clone the repository:
   ```bash
   git clone https://github.com/tiagohugovitor/assembly-lines.git
   cd assembly-lines
   ```

2. Run the comparison script:
    ```bash
    python compareAlgorithms.py
    ```

3. Results:
    - Execution time graphs saved in the results directory.
    - Dataframe with execution times saved as results/dataframe-{inputSize}.xlsx.

## Algorithms Analysis

### Time Complexity
 - **Recursive Algorithm with brute force**: O(2^n)
 - **Dynamic Programming Algorithm**: O(n)

### Conclusion
The brute force recursive algorithm has a time complexity of O(2^n) which is due to the recalculation of subproblems. This approach quickly becomes infeasible to execute due to its high execution time.

By utilizing dynamic programming, we achieve a linear time complexity algorithm. However, this technique increases the space complexity as it requires storing the already calculated subproblems, resulting in a linear space complexity as well.

## Dependencies
    - Python 3.x
    - matplotlib
    - pandas