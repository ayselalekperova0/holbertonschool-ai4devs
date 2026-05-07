def countdown(n):
    while n != 0:
        print(n)
        n -= 2  # bug: tək ədədlərdə sonsuz loop

countdown(5)
# Gözlənilən: 5, 3, 1
# Alınan: sonsuz sayda loop (5, 3, 1, -1, -3, ...)
