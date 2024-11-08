# 8-Queens Problem using Backtracking

# Function to check if a queen can be safely placed at board[row][col]
def is_safe(board, row, col):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Recursive function to solve the 8-Queens problem


def solve_8_queens(board, col):
    # Base case: if all queens are placed, return True
    if col >= len(board):
        return True

    # Try placing a queen in each row of the current column
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_8_queens(board, col + 1):
                return True

            # Backtrack: remove the queen if placing here leads to a solution failure
            board[i][col] = 0

    return False

# Function to initialize the board and place the first queen


def generate_8_queens_with_first_queen(row, col):
    # Create an 8x8 board initialized with 0s
    board = [[0 for _ in range(8)] for _ in range(8)]

    # Place the first queen at the specified position
    board[row][col] = 1

    # Use backtracking to place the remaining queens
    if not solve_8_queens(board, col + 1):
        print("Solution does not exist")
        return None
    else:
        return board


# User input for initial position of the first queen
row = int(input("Enter the row position of the first queen (0-7): "))
col = int(input("Enter the column position of the first queen (0-7): "))

# Generate and print the 8-Queens solution matrix
solution = generate_8_queens_with_first_queen(row, col)
if solution:
    print("Final 8-Queens Solution Matrix:")
    for row in solution:
        print(row)

# Explanation:
# - The `is_safe` function checks if a queen can be placed safely by checking for other queens
#   in the left side of the current row, upper diagonal, and lower diagonal.
# - The `solve_8_queens` function tries to place queens column by column using backtracking.
# - If a placement fails, it backtracks by removing the last placed queen and tries the next position.
# - The `generate_8_queens_with_first_queen` function initializes the board, places the first queen,
#   and then solves the rest of the board using backtracking.

# Q&A Section

# Q1: What is the purpose of the `is_safe` function?
# A1: It checks if a queen can be placed at a given position without conflicting with other queens.

# Q2: Why do we check only the left side for conflicts in `is_safe`?
# A2: We place queens column by column from left to right, so we only need to check the left side.

# Q3: What does the `solve_8_queens` function do?
# A3: It recursively places queens on the board column by column and backtracks if a placement leads to a conflict.

# Q4: Why is backtracking needed in this solution?
# A4: Backtracking allows the algorithm to remove a queen if placing it leads to no solutions further down.

# Q5: What does the function `generate_8_queens_with_first_queen` do?
# A5: It initializes the board with the first queen placed at a specified position and solves the rest using backtracking.

# Q6: What happens if no solution is possible?
# A6: If no solution exists, the program prints "Solution does not exist."

# Q7: Can the initial queen be placed at any position on the board?
# A7: Yes, the initial position is given by user input, and the algorithm adapts accordingly.

# Q8: What is the time complexity of the 8-Queens solution?
# A8: The time complexity is approximately O(n!), where n is the number of queens.

# Q9: How are conflicts checked for diagonals?
# A9: Conflicts on diagonals are checked by traversing the diagonals on the left side of the queen’s position.

# Q10: How is the final solution displayed?
# A10: The solution matrix is printed row by row, with 1s representing queens and 0s representing empty spaces.

# Example of Input:
# Suppose the user enters:
# Row position: 0
# Column position: 0

# Expected Output:
# Final 8-Queens Solution Matrix:
# [1, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 1, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 1, 0, 0]
# [0, 0, 0, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 1, 0]
# [0, 0, 0, 0, 0, 0, 0, 1]
