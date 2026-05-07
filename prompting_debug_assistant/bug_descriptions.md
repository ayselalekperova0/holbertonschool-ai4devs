## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The function fails when n == len(items), returns extra element.

## Bug 2 – bug2.py
**Intended Behavior**: Count down from n to 0.
**Issue Type**: Logical error.
**Notes**: Fails with odd numbers, causes infinite loop.

## Bug 3 – bug3.js
**Intended Behavior**: Return user's age from profile object.
**Issue Type**: Runtime exception.
**Notes**: Crashes when user.profile is undefined.

## Bug 4 – bug4.js
**Intended Behavior**: Return true if number is even, false if odd.
**Issue Type**: Logical error.
**Notes**: Return values are swapped, always returns wrong result.

## Bug 5 – bug5.c
**Intended Behavior**: Divide two integers and return result.
**Issue Type**: Runtime exception.
**Notes**: Crashes with floating point exception when b is 0.
