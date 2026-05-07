/*
 * Holberton AI4Devs
 * Task 2 Fix
 * Applied AI diagnosis
 * Verified and tested
 */
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    // Fixed: Changed loop condition to i < numbers.size()
    for (int i = 0; i < numbers.size(); i++) {
        std::cout << "Index " << i << ": " << numbers[i] << std::endl;
    }
    return 0;
}
