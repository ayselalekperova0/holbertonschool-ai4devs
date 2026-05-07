#include <iostream>
#include <vector>
int main() {
    std::vector<int> numbers = {1, 2, 3};
    // Xəta: i <= 3 dövrü limiti aşır (Out of bounds)
    for (int i = 0; i <= 3; i++) {
        std::cout << numbers[i] << std::endl;
    }
    return 0;
}
