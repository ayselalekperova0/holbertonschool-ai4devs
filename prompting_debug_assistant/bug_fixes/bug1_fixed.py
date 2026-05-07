
def get_last_n_items(items, n):
    return items[len(items)-n:]  # düzəliş: -1 silindi

# Test
assert get_last_n_items([1, 2, 3, 4, 5], 3) == [3, 4, 5]
print(get_last_n_items([1, 2, 3, 4, 5], 3))  # [3, 4, 5]
