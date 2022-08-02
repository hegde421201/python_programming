from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index - 1]:
            continue


    return result
