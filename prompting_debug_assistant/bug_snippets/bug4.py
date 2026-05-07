# Task: Collect or Create Buggy Snippets
# Filename: bug4.py
# Language: Python
# Description: This script calculates the average of a list of numbers.
# It fails to handle the case where the list is empty, leading
# to a ZeroDivisionError during execution.
# ----------------------------------------------------------------

def compute_average(data):
    print(f"Processing data: {data}")
    total_sum = sum(data)
    # Bug: No check for empty list before division
    avg = total_sum / len(data)
    return avg

# This call will trigger the runtime exception
print("Average is:", compute_average([]))
