/**
 * Task: Collect or Create Buggy Snippets
 * Filename: bug5.js
 * Language: JavaScript
 * Description: Uses a loop with setTimeout to print numbers.
 * Because 'var' is function-scoped, the final value of 'i' 
 * is captured by all closures, causing incorrect output.
 */

console.log("Starting countdown...");

for (var i = 1; i <= 3; i++) {
    setTimeout(function() {
        // Bug: Will print "Step: 4" three times instead of 1, 2, 3
        console.log("Step: " + i);
    }, 1000);
}

console.log("Loop finished, waiting for timeouts...");
