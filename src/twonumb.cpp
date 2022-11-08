#include <iostream>
#include <vector>


class Solution 
{
public:
    std::vector<int> twoSum(const std::vector<int>& nums, int target) {
        int first_numb = nums[0];
        int second_numb = nums[1];
        for(int i = 0; i < nums.size(); i++)
        {
            first_numb = nums[i];

            for(int j = 0; j < nums.size(); j++)
            {
                second_numb = nums[j];
                if(first_numb + second_numb == target && i != j)
                    return std::vector<int>{i,j};
            }
        }
        return {};
    }
};
