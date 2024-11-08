# Non-Recursive (Iterative) Fibonacci Function

# Function to calculate Fibonacci iteratively
def fibonacci_iterative(n):
    # Base case: return n if it's 0 or 1
    if n <= 1:
        return n

    # Initialize first two Fibonacci numbers
    a, b = 0, 1

    # Loop to calculate Fibonacci for n using iterative approach
    for _ in range(2, n+1):
        a, b = b, a + b  # Update values for next Fibonacci number

    return b  # Return the nth Fibonacci number


# Recursive Fibonacci Function

# Function to calculate Fibonacci recursively
def fibonacci_recursive(n):
    # Base case: return n if it's 0 or 1
    if n <= 1:
        return n

    # Recursive call to calculate Fibonacci number
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# User input for Fibonacci number to calculate
n = int(input("Enter the Fibonacci number (n) to calculate: "))  # Example: n = 10

# Print Results for both approaches
print("Iterative Fibonacci of", n, ":",
      fibonacci_iterative(n))  # Iterative result
print("Recursive Fibonacci of", n, ":",
      fibonacci_recursive(n))  # Recursive result


# Explanation:
# - The `fibonacci_iterative` function calculates the nth Fibonacci number iteratively.
# - It initializes two variables, `a` and `b`, to hold the first two Fibonacci numbers (0 and 1).
# - Then, it uses a loop to iteratively compute the Fibonacci number for n.
#
# - The `fibonacci_recursive` function calculates the nth Fibonacci number using recursion.
# - The function calls itself recursively for `n-1` and `n-2`, which are the two previous Fibonacci numbers.


# Time and Space Complexity Analysis:
# - Time complexity (Iterative): O(n) because we loop through n elements.
# - Space complexity (Iterative): O(1) because we only store two variables, `a` and `b`.
#
# - Time complexity (Recursive): O(2^n) because each recursive call makes two additional recursive calls.
# - Space complexity (Recursive): O(n) because of the recursion stack that grows linearly with the input n.


# Q&A Section:

# Q1: What is the difference between the iterative and recursive approaches?
# A1: The iterative approach uses a loop to calculate Fibonacci numbers, while the recursive approach calls itself for smaller subproblems.

# Q2: Why does the recursive approach have exponential time complexity (O(2^n))?
# A2: The recursive approach calculates the same Fibonacci numbers multiple times for different branches, leading to redundant computations.

# Q3: How does the iterative approach improve performance over the recursive one?
# A3: The iterative approach avoids redundant calculations by directly using a loop to calculate the Fibonacci number, which is much more efficient.

# Q4: What is the base case in both the recursive and iterative solutions?
# A4: The base case is when n is 0 or 1, where the function directly returns the value of n without further calculations.

# Q5: How does the iterative solution calculate Fibonacci numbers?
# A5: It initializes two variables (0 and 1) for the first two Fibonacci numbers and uses a loop to update these values iteratively.

# Q6: How does the recursive solution calculate Fibonacci numbers?
# A6: It calls itself recursively with the values n-1 and n-2, summing them to get the nth Fibonacci number.

# Q7: What are the space complexity implications of recursion?
# A7: In recursion, the space complexity is O(n) due to the recursion stack, which stores intermediate function calls.

# Q8: Can the recursive solution be optimized?
# A8: Yes, the recursive solution can be optimized using memoization (storing previously computed Fibonacci values) to reduce time complexity to O(n).

# Q9: Why does the iterative solution have a space complexity of O(1)?
# A9: The iterative solution uses only two variables (`a` and `b`) to store the Fibonacci values, which does not depend on the size of the input.

# Q10: For large inputs, which approach would you prefer and why?
# A10: The iterative approach is preferred for large inputs due to its O(n) time complexity and O(1) space complexity, making it much more efficient than the recursive approach.


# Example Input and Output:
# Input:
# Enter the Fibonacci number (n) to calculate: 10
#
# Output:
# Iterative Fibonacci of 10 : 55
# Recursive Fibonacci of 10 : 55

