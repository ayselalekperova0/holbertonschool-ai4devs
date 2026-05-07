def average(numbers):
    # Xəta: Siyahı boşdursa ZeroDivisionError verəcək
    total = sum(numbers)
    return total / len(numbers)

print(average([]))
