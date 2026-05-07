# Holberton AI4Devs
# Task 2 Fix
# Applied AI diagnosis
# Verified and tested
# ------------------
def get_last_n_items(items, n):
    if n <= 0:
        return []
    # Fixed: Used negative slicing to correctly get last n items
    return items[-n:]

# Testing
data = [10, 20, 30, 40, 50]
print(get_last_n_items(data, 3)) # Expected: [30, 40, 50]
