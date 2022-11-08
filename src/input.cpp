#include <iostream>
#include <vector>

extern class Solution{};

Solution sol;

int main()
{
    std::vector<int> Pippo = sol.twoSum(std::vector<int>{2,7,11,15}, 9);
    std::vector<int> Franco = sol.twoSum(std::vector<int>{3,2,4}, 6);

    for (auto i: Pippo)
        std::cout << i << std::endl;

    for (auto i: Franco)
        std::cout << i << std::endl;
}