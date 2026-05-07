# Fix Validation Report

## Bug 1 – bug1_fixed.py
- **Input**: [10, 20, 30, 40, 50], n=3
- **Expected Output**: [30, 40, 50]
- **Actual Output**: [30, 40, 50] ✅
- **Manual Tweaks**: None. Used negative slicing as it's cleaner.

## Bug 2 – bug2_fixed.js
- **Input**: price=100, tax="10"
- **Expected Output**: 110
- **Actual Output**: 110 ✅
- **Manual Tweaks**: Used `Number()` for explicit conversion.

## Bug 3 – bug3_fixed.cpp
- **Input**: Vector {1, 2, 3, 4, 5}
- **Expected Output**: Elements at index 0 to 4
- **Actual Output**: Elements at index 0 to 4 ✅
- **Manual Tweaks**: None.

## Bug 4 – bug4_fixed.py
- **Input**: [] (Empty list)
- **Expected Output**: 0
- **Actual Output**: 0 ✅
- **Manual Tweaks**: None.

## Bug 5 – bug5_fixed.js
- **Input**: Loop 1 to 3 with delay
- **Expected Output**: Step: 1, Step: 2, Step: 3
- **Actual Output**: Step: 1, Step: 2, Step: 3 ✅
- **Manual Tweaks**: Replaced `var` with `let`.
