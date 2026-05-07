def countdown(n):
    while n > 0:  # düzəliş: != 0 yerine > 0
        print(n)
        n -= 2

# Test
countdown(5)  # 5, 3, 1 ✅
