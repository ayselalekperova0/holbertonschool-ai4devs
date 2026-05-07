# Task: Collect or Create Buggy Snippets
# Filename: bug1.py
# Language: Python
# Description: This function is intended to return the last n items 
# from a given list. However, it contains an off-by-one error 
# in the slicing logic which causes it to return incorrect results.
# ----------------------------------------------------------------

def get_last_n_items(items, n):
    # Bug: The +1 in the slice index causes it to skip one element
    if n <= 0:
        return []
    return items[len(items) - n + 1:]

# Test case
my_list = [10, 20, 30, 40, 50]
result = get_last_n_items(my_list, 3)
print(f"Last 3 items: {result}")
