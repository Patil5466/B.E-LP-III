# Binomial Coefficients using Dynamic Programming

# Function to compute binomial coefficient C(n, k)
def binomial_coefficient(n, k):
    # Create a 2D DP array to store values of binomial coefficients
    dp = [[0 for x in range(k + 1)] for y in range(n + 1)]

    # Calculate the binomial coefficients using DP
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base cases: C(i, 0) = 1 and C(i, i) = 1
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                # Use previously computed values to fill in dp array
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    # The binomial coefficient C(n, k) is stored in dp[n][k]
    return dp[n][k]


# User input for values of n and k
n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

# Calculate the binomial coefficient C(n, k)
result = binomial_coefficient(n, k)

# Display result
print(f"Binomial Coefficient C({n}, {k}) is {result}")

# Explanation:
# - The `binomial_coefficient` function uses dynamic programming to compute
#   the value of binomial coefficient C(n, k), which represents the number
#   of ways to choose k elements from a set of n elements.
# - `dp[i][j]` stores the value of C(i, j).
# - For each row, the base cases are set such that C(i, 0) = 1 and C(i, i) = 1.
# - For other values, the function uses Pascal's identity: C(i, j) = C(i-1, j-1) + C(i-1, j).
# - The final result, C(n, k), is stored in dp[n][k].

# Q&A Section

# Q1: What is the purpose of the `binomial_coefficient` function?
# A1: It calculates the binomial coefficient C(n, k), which is the number of ways to choose k elements from n elements.

# Q2: Why do we use dynamic programming for this calculation?
# A2: Dynamic programming avoids redundant calculations by storing values in a table, making the process more efficient.

# Q3: What does `dp[i][j] = 1` mean when j == 0 or j == i?
# A3: It sets the base cases for binomial coefficients where choosing 0 or all elements results in 1 way.

# Q4: What is Pascal's identity, and how is it used here?
# A4: Pascal's identity states that C(i, j) = C(i-1, j-1) + C(i-1, j), used here to fill the DP table.

# Q5: What would happen if k > n?
# A5: If k > n, C(n, k) is 0 because you cannot choose more elements than are available.

# Q6: What is the time complexity of this algorithm?
# A6: The time complexity is O(n * k) because each entry in the DP table is calculated once.

# Q7: How are the results displayed to the user?
# A7: The program prints the binomial coefficient C(n, k).

# Q8: Can this method handle large values of n and k?
# A8: Yes, it can handle relatively large values, but for extremely large values, it may become slow or run out of memory.

# Q9: What does the `min(i, k)` do in the loop?
# A9: It limits the inner loop to avoid unnecessary calculations, as values of j beyond k are not needed.

# Q10: Why do we initialize the DP array with zeros?
# A10: Initializing with zeros provides a base structure, and specific values are assigned based on conditions and calculations.

# Example of Input:
# Suppose the user enters:
# n = 5
# k = 2

# Expected Output:
# Binomial Coefficient C(5, 2) is 10
