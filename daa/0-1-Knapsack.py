# 0-1 Knapsack Problem using Dynamic Programming

# Function to solve the 0-1 Knapsack problem
def knapsack_01(values, weights, capacity):
    # Number of items
    n = len(values)

    # Creating a 2D DP array to store the maximum value for each subproblem
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

    # Fill the DP array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Item can be included, so we choose the max value of including or excluding it
                dp[i][w] = max(values[i - 1] + dp[i - 1]
                               [w - weights[i - 1]], dp[i - 1][w])
            else:
                # Item cannot be included, keep previous max value
                dp[i][w] = dp[i - 1][w]

    # The maximum value that can be obtained with the given capacity is in dp[n][capacity]
    return dp[n][capacity]


# User input for knapsack capacity
capacity = int(input("Enter the capacity of the knapsack: "))

# User input for number of items
num_items = int(input("Enter the number of items: "))
values = []
weights = []

# Collect value and weight for each item
for i in range(num_items):
    value = int(input(f"Enter value of item {i+1}: "))
    weight = int(input(f"Enter weight of item {i+1}: "))
    values.append(value)
    weights.append(weight)

# Calculate the maximum value that can fit in the knapsack
max_value = knapsack_01(values, weights, capacity)

# Display result
print(f"Maximum value in the knapsack: {max_value}")

# Explanation:
# - The `knapsack_01` function uses dynamic programming to find the maximum value
#   that can fit in a knapsack with the given capacity.
# - `dp[i][w]` stores the maximum value that can be obtained with the first `i` items
#   and a knapsack capacity of `w`.
# - If the weight of the current item is less than or equal to the remaining capacity,
#   it checks whether including it gives a higher value than excluding it.
# - The final answer, the maximum value that can fit in the knapsack, is stored in `dp[n][capacity]`.

# Q&A Section

# Q1: What is the purpose of the `knapsack_01` function?
# A1: It finds the maximum value of items that can fit in a knapsack without exceeding its capacity.

# Q2: Why do we use a 2D array `dp`?
# A2: The 2D array `dp` stores subproblem solutions for each item and capacity combination.

# Q3: How does the program handle items with weight greater than the current capacity?
# A3: If the item’s weight is greater than the current capacity, it is skipped, keeping the previous max value.

# Q4: What does `dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])` mean?
# A4: This line chooses the maximum value between including or excluding the current item.

# Q5: What does `dp[n][capacity]` represent?
# A5: It represents the maximum value obtainable with all items and the given knapsack capacity.

# Q6: Why does the algorithm use dynamic programming?
# A6: Dynamic programming avoids recomputing subproblems, making the solution more efficient.

# Q7: Can this method handle fractional items?
# A7: No, this method only applies to the 0-1 knapsack problem where items must be included or excluded entirely.

# Q8: What is the time complexity of this algorithm?
# A8: The time complexity is O(n * capacity), where n is the number of items.

# Q9: How are the results displayed to the user?
# A9: The program prints the maximum value that can fit in the knapsack.

# Q10: What is the base case in this DP solution?
# A10: The base case is `dp[0][w] = 0` for all `w`, representing zero items giving zero value.

# Example of Input:
# Suppose the user enters:
# Knapsack capacity: 50
# Number of items: 3
# Item 1 - Value: 60, Weight: 10
# Item 2 - Value: 100, Weight: 20
# Item 3 - Value: 120, Weight: 30

# Expected Output:
# Maximum value in the knapsack: 220
