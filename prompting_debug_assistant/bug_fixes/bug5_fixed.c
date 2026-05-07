#include <stdio.h>

int divide(int a, int b) {
    if (b == 0) {  // düzəliş: sıfıra bölmə yoxlanır
        printf("Error: Division by zero\n");
        return -1;
    }
    return a / b;
}

int main() {
    printf("%d\n", divide(10, 2));  // 5 ✅
    printf("%d\n", divide(5, 0));   // Error ✅
    return 0;
}
