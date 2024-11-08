import random

# Deterministic Quick Sort


def quick_sort_deterministic(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # Choose the first element as the pivot
    left = [x for x in arr[1:] if x < pivot]  # Elements less than pivot
    # Elements greater than or equal to pivot
    right = [x for x in arr[1:] if x >= pivot]

    # Recursively apply the same logic to left and right subarrays
    return quick_sort_deterministic(left) + [pivot] + quick_sort_deterministic(right)


# Randomized Quick Sort
def quick_sort_randomized(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Randomly choose a pivot element and move it to the front
    pivot_index = random.randint(0, len(arr) - 1)
    # Swap pivot with the first element
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    pivot = arr[0]

    # Partition the array into two subarrays
    left = [x for x in arr[1:] if x < pivot]  # Elements less than pivot
    # Elements greater than or equal to pivot
    right = [x for x in arr[1:] if x >= pivot]

    # Recursively apply the same logic to left and right subarrays
    return quick_sort_randomized(left) + [pivot] + quick_sort_randomized(right)


# User input for array
# Example: 10 7 8 9 1 5
arr = list(map(int, input("Enter a list of numbers separated by space: ").split()))

# Print Results for both approaches
print("Sorted Array using Deterministic Quick Sort:",
      quick_sort_deterministic(arr))  # Deterministic result
print("Sorted Array using Randomized Quick Sort:",
      quick_sort_randomized(arr))  # Randomized result


# Explanation:
# - The `quick_sort_deterministic` function sorts the array by choosing the first element as the pivot.
# - It divides the array into two subarrays: one with elements less than the pivot and one with elements greater than or equal to the pivot.
# - Then it recursively sorts the two subarrays and combines them to get the sorted array.
#
# - The `quick_sort_randomized` function is similar but chooses a pivot randomly, making it less likely to encounter worst-case scenarios in the sorting process.

# Time and Space Complexity Analysis:
# - Time complexity (Deterministic): O(n^2) in the worst case (e.g., if the array is already sorted), but O(n log n) on average.
# - Space complexity (Deterministic): O(log n) because of the recursion stack used in the sorting process.
#
# - Time complexity (Randomized): O(n log n) on average and O(n^2) in the worst case, but the probability of hitting the worst case is low.
# - Space complexity (Randomized): O(log n) for the recursion stack.

# Q&A Section:

# Q1: What is the difference between deterministic and randomized quick sort?
# A1: The deterministic quick sort chooses the first element as the pivot, while the randomized quick sort chooses a pivot randomly from the array.

# Q2: Why is randomized quick sort often preferred over deterministic quick sort?
# A2: Randomized quick sort is less likely to encounter the worst-case time complexity of O(n^2) because the pivot is chosen randomly, avoiding sorted or nearly sorted inputs.

# Q3: What are the base cases for both quick sort variants?
# A3: The base case is when the array has 1 or 0 elements, in which case it is already sorted.

# Q4: Why do we partition the array in quick sort?
# A4: We partition the array around a pivot to divide it into two smaller subarrays that can be sorted recursively.

# Q5: How does the deterministic quick sort handle the pivot?
# A5: The deterministic quick sort always picks the first element as the pivot and partitions the array based on that.

# Q6: How does the randomized quick sort handle the pivot?
# A6: The randomized quick sort picks a random index in the array and swaps the element at that index with the first element to use as the pivot.

# Q7: What are the time complexities of both algorithms?
# A7: The time complexity of deterministic quick sort is O(n^2) in the worst case and O(n log n) on average, while randomized quick sort has O(n log n) on average and O(n^2) in the worst case.

# Q8: When should you prefer deterministic quick sort?
# A8: Deterministic quick sort may be preferred when you know the input array is not sorted or nearly sorted, or you have a good pivot strategy (e.g., median-of-three).

# Q9: Why does quick sort have such good average performance?
# A9: Quick sort has good average performance because it divides the array into smaller subarrays and sorts them independently, leading to O(n log n) time complexity on average.

# Q10: Can we make deterministic quick sort faster?
# A10: Yes, deterministic quick sort can be optimized by choosing a better pivot (e.g., median-of-three) or using hybrid algorithms like introsort.

# Example Input and Output:
# Input:
# Enter a list of numbers separated by space: 10 7 8 9 1 5
#
# Output:
# Sorted Array using Deterministic Quick Sort: [1, 5, 7, 8, 9, 10]
# Sorted Array using Randomized Quick Sort: [1, 5, 7, 8, 9, 10]

