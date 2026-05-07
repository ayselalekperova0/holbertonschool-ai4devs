/*
 * Task: Collect or Create Buggy Snippets
 * Filename: bug3.cpp
 * Language: C++
 * Description: Iterates through a vector to print its contents.
 * The loop condition i <= numbers.size() causes a runtime error
 * because it tries to access an index that does not exist.
 */

#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    std::cout << "Printing vector elements:" << std::endl;

    // Bug: i <= 5 is out of bounds for a vector of size 5
    for (int i = 0; i <= 5; i++) {
        std::cout << "Element at index " << i << ": " << numbers[i] << std::endl;
    }

    return 0;
}
