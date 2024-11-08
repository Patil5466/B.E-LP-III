# Job Sequencing with Deadlines using Greedy Method

# Import necessary libraries
from typing import List, Tuple

# Function to perform job sequencing


def job_sequencing(jobs: List[Tuple[int, int, int]]) -> Tuple[List[int], int]:
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline to define the schedule array size
    max_deadline = max(job[1] for job in jobs)

    # Initialize schedule array to store job IDs with slots up to max_deadline
    schedule = [-1] * (max_deadline + 1)
    total_profit = 0

    # Loop over each job to try to schedule it within its deadline
    for job in jobs:
        job_id, deadline, profit = job
        # Attempt to schedule job in the last possible slot within its deadline
        for slot in range(deadline, 0, -1):
            if schedule[slot] == -1:
                schedule[slot] = job_id
                total_profit += profit
                break  # Exit once job is scheduled

    # Filter out unassigned slots (-1) and return job sequence and total profit
    job_sequence = [job_id for job_id in schedule if job_id != -1]
    return job_sequence, total_profit


# User input for job details
num_jobs = int(input("Enter the number of jobs: "))
jobs = []

# Collect job details
for i in range(num_jobs):
    job_id = int(input(f"Enter Job ID for job {i+1}: "))
    deadline = int(input(f"Enter Deadline for job {i+1}: "))
    profit = int(input(f"Enter Profit for job {i+1}: "))
    jobs.append((job_id, deadline, profit))

# Calculate job sequence and maximum profit
job_sequence, max_profit = job_sequencing(jobs)

# Display result
print(f"Optimal job sequence: {job_sequence}")
print(f"Maximum profit: {max_profit}")

# Explanation:
# - The program defines the `job_sequencing` function, which accepts a list of jobs (each defined by job ID, deadline, and profit).
# - It sorts jobs by profit in descending order for the greedy selection.
# - `schedule` array tracks job IDs in their assigned slots based on their deadlines.
# - For each job, the function attempts to place it in the latest available slot before its deadline.
# - Once all jobs are checked, it returns the job sequence and total profit.

# Q&A Section

# Q1: What does the `job_sequencing` function do?
# A1: It finds the optimal sequence of jobs to maximize profit, respecting deadlines.

# Q2: Why do we sort the jobs by profit in descending order?
# A2: Sorting by profit ensures that higher-profit jobs are considered first, following the greedy approach.

# Q3: How is `max_deadline` determined?
# A3: `max_deadline` is the maximum deadline among all jobs, used to define the `schedule` array size.

# Q4: Why do we initialize `schedule` with -1?
# A4: `-1` represents an unassigned slot in the schedule array.

# Q5: What is the purpose of the inner `for` loop with `slot`?
# A5: It attempts to assign each job to the latest available slot before its deadline.

# Q6: What happens if no slot is available for a job within its deadline?
# A6: The job is skipped, as it cannot be scheduled without missing its deadline.

# Q7: Why do we add the profit of scheduled jobs to `total_profit`?
# A7: To calculate the maximum possible profit from the scheduled jobs.

# Q8: How are the results displayed to the user?
# A8: The optimal job sequence and maximum profit are printed to the console.

# Q9: What is the time complexity of this job sequencing algorithm?
# A9: The time complexity is O(n log n) due to sorting, where n is the number of jobs.

# Q10: What input validation is necessary for this program?
# A10: Input should be integers for job ID, deadline, and profit, and the number of jobs should be a positive integer.

# Example of Input:
# Suppose the user enters:
# Number of jobs: 3
# Job IDs: 1, 2, 3
# Deadlines: 2, 1, 2
# Profits: 100, 50, 200

# Expected Output:
# Optimal job sequence: [3, 1]
# Maximum profit: 300
