# Bug Snippets Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Should return the last `n` items from a list.
**Issue Type**: Off-by-one error in list slicing.
**Note**: The slice index calculation is incorrect.

## Bug 2 – bug2.js
**Intended Behavior**: Should mathematically add the tax to the price.
**Issue Type**: Logical / Data type misuse (Type Coercion).
**Note**: Adding a string to a number results in concatenation.

## Bug 3 – bug3.cpp
**Intended Behavior**: Should print every element in the vector.
**Issue Type**: Runtime exception (Out of bounds).
**Note**: The loop goes one index beyond the vector's size.

## Bug 4 – bug4.py
**Intended Behavior**: Should calculate the mean of a numeric list.
**Issue Type**: Runtime exception (ZeroDivisionError).
**Note**: Fails when the input list is empty.

## Bug 5 – bug5.js
**Intended Behavior**: Should print numbers 1, 2, 3 with a delay.
**Issue Type**: Logical error (Variable scoping with `var`).
**Note**: All callbacks reference the same updated variable.
