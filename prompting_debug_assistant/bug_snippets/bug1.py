def get_last_n_items(items, n):
    # Xəta: n == len(items) olduqda boş siyahı qaytarır
    return items[len(items)-n+1:]

data = [10, 20, 30, 40, 50]
print(get_last_n_items(data, 5))
