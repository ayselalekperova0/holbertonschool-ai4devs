function isEven(n) {
    if (n % 2 == 0) {
        return true;   // düzəliş: false → true
    } else {
        return false;  // düzəliş: true → false
    }
}

// Test
console.log(isEven(4));  // true ✅
console.log(isEven(3));  // false ✅

