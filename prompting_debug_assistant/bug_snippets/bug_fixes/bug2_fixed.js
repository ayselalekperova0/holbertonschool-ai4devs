function calculateTotal(price, tax) {
    // Fixed: Converted tax to a Number to avoid string concatenation
    const total = price + Number(tax);
    console.log("Total price is: " + total);
    return total;
}

calculateTotal(100, "10"); // Expected: 110
