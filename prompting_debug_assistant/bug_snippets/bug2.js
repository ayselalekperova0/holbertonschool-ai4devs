function calculateTotal(price, tax) {
    // Xəta: tax string kimi gələrsə concatenation baş verir
    const total = price + tax;
    console.log("Total price is: " + total);
}
calculateTotal(100, "10");
