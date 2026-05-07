/**
 * Task: Collect or Create Buggy Snippets
 * Filename: bug2.js
 * Language: JavaScript
 * Description: Calculates the total cost by adding tax to the price.
 * The bug occurs when the tax is passed as a string, leading to
 * string concatenation instead of mathematical addition.
 */

function calculateTotal(price, tax) {
    console.log("Initializing calculation...");
    // The following line has a logical flaw due to JS type coercion
    const total = price + tax;
    
    console.log("Price: " + price);
    console.log("Tax: " + tax);
    console.log("Computed Total: " + total);
    return total;
}

// Example of the bug: result will be "10010" instead of 110
calculateTotal(100, "10");
