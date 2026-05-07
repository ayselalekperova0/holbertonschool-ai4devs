# Structured Bug Reports

## Bug Report – bug1.py
- **Summary**: Off-by-one error in slicing logic.
- **Root Cause**: The slice `items[len(items) - n + 1:]` calculated the starting index incorrectly.
- **Resolution**: Simplified to `items[-n:]` which correctly handles the tail of the list.
- **Lesson Learned**: Python's negative indexing is cleaner and less error-prone for trailing slices.

## Bug Report – bug2.js
- **Summary**: Arithmetic sum treated as string concatenation.
- **Root Cause**: The variable `tax` was a string, causing the `+` operator to concatenate.
- **Resolution**: Used `Number(tax)` to explicitly cast the value to a number.
- **Lesson Learned**: Always sanitize and cast types when performing math on dynamic inputs in JS.

## Bug Report – bug3.cpp
- **Summary**: Off-by-one / Out of bounds memory access.
- **Root Cause**: The loop condition `i <= numbers.size()` allowed accessing an index beyond the vector limit.
- **Resolution**: Changed condition to `i < numbers.size()`.
- **Lesson Learned**: Vector indices are zero-based; the size is never a valid index.

## Bug Report – bug4.py
- **Summary**: ZeroDivisionError on empty lists.
- **Root Cause**: The function didn't check if the list was empty before dividing by its length.
- **Resolution**: Added a guard clause `if not data: return 0`.
- **Lesson Learned**: Always handle edge cases like empty collections to prevent runtime crashes.

## Bug Report – bug5.js
- **Summary**: Closure scope issue in a loop.
- **Root Cause**: `var` is function-scoped, causing all callbacks to see the final value of `i`.
- **Resolution**: Replaced `var` with `let` to create block-scoped iterations.
- **Lesson Learned**: Use `let` and `const` in modern JavaScript to avoid scoping bugs.
