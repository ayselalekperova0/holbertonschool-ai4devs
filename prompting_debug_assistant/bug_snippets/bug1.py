def get_last_n_items(items, n):
    return items[len(items)-n-1:]  # bug: -1 əlavədir

print(get_last_n_items([1, 2, 3, 4, 5], 3))
# Gözlənilən nəticə: [3, 4, 5]
# Alınan nəticə:     [2, 4, 5]
