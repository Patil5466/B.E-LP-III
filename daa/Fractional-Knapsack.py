# Fractional Knapsack Problem using Greedy Method

# Importing List and Tuple for type hinting
from typing import List, Tuple

# Function to solve the Fractional Knapsack problem


def fractional_knapsack(capacity: int, items: List[Tuple[int, int]]) -> float:
    # Calculate value-to-weight ratio for each item and sort by descending ratio
    items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)

    # Initialize total value for items in knapsack
    total_value = 0.0

    # Loop over sorted items to add to knapsack
    for value, weight in items:
        if capacity >= weight:
            # Add entire item if there's enough capacity
            total_value += value
            capacity -= weight
        else:
            # Add fractional part of item to fill remaining capacity
            total_value += value * (capacity / weight)
            break  # Knapsack is full, exit loop

    # Return the maximum value that fits in the knapsack
    return total_value


# User input for knapsack capacity
capacity = int(input("Enter the capacity of the knapsack: "))

# User input for number of items
num_items = int(input("Enter the number of items: "))
items = []

# Collect value and weight for each item
for i in range(num_items):
    value = int(input(f"Enter value of item {i+1}: "))
    weight = int(input(f"Enter weight of item {i+1}: "))
    items.append((value, weight))

# Calculate maximum value that can fit in the knapsack
max_value = fractional_knapsack(capacity, items)

# Display result
print(f"Maximum value in the knapsack: {max_value:.2f}")

# Explanation:
# - The program defines `fractional_knapsack`, which calculates the maximum value of items that fit in a knapsack with given capacity.
# - Each item is represented by its value and weight.
# - The items list is sorted by value-to-weight ratio in descending order, prioritizing items with higher ratios.
# - For each item, if it can fit entirely within the remaining capacity, it is added in full.
# - If it cannot fit fully, a fraction of it is added to fill the remaining space in the knapsack.
# - The function returns the total maximum value that can be stored in the knapsack.

# Q&A Section

# Q1: What does the `fractional_knapsack` function do?
# A1: It calculates the maximum value of items that can fit in the knapsack using the fractional knapsack approach.

# Q2: Why do we sort items by value-to-weight ratio?
# A2: Sorting by ratio ensures we maximize value by prioritizing items with the highest value per unit weight.

# Q3: What is the purpose of `capacity -= weight`?
# A3: It decreases the knapsack capacity by the weight of the item added.

# Q4: How does the program handle items that can't fully fit in the knapsack?
# A4: It adds a fractional portion of the item's value to fill the remaining capacity.

# Q5: What does `value * (capacity / weight)` calculate?
# A5: It calculates the value of the fractional part of the item that can fit within the remaining capacity.

# Q6: What would happen if `capacity` were zero?
# A6: If capacity is zero, no items can be added, and the total value would remain zero.

# Q7: How are the results displayed to the user?
# A7: The program prints the maximum value that can fit in the knapsack, formatted to two decimal places.

# Q8: What is the time complexity of this algorithm?
# A8: The time complexity is O(n log n) due to sorting, where n is the number of items.

# Q9: Can this method be applied to the 0/1 knapsack problem?
# A9: No, this method only applies to the fractional knapsack problem because it allows taking fractions of items.

# Q10: Why is greedy method suitable for fractional knapsack?
# A10: The greedy method is optimal for fractional knapsack as it maximizes value by picking high-value items proportionally, unlike the 0/1 knapsack.

# Example of Input:
# Suppose the user enters:
# Knapsack capacity: 50
# Number of items: 3
# Item 1 - Value: 60, Weight: 10
# Item 2 - Value: 100, Weight: 20
# Item 3 - Value: 120, Weight: 30

# Expected Output:
# Maximum value in the knapsack: 240.00
