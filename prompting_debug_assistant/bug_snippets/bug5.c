#include <stdio.h>

int divide(int a, int b) {
    return a / b;  // bug: b=0 olduqda crash
}

int main() {
    printf("%d\n", divide(10, 2));  // 5 ✅
    printf("%d\n", divide(5, 0));   // bug: Floating point exception
    return 0;
}
