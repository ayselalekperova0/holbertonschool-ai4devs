function isEven(n) {
    if (n % 2 == 0) {
        return false;  // bug: true olmalıdır
    } else {
        return true;   // bug: false olmalıdır
    }
}

console.log(isEven(4));  // Gözlənilən: true, Alınan: false
console.log(isEven(3));  // Gözlənilən: false, Alınan: true
