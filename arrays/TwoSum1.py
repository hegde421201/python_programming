from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # step 1 : define a hashmap with key as the element of the List and the corresponding value as the index in the List
    hashmap = dict()

    # step 2: We require both index and the actual number for the hashmap created in step 1 above.
    # We use enumerate() method in python on the list
    for index, num in enumerate(nums):
        difference = target - num  # check whether the difference is in the hashmap
        if difference in hashmap:
            return [index, hashmap[difference]]  # return the indices pair of index and the dictionary element key
        hashmap[num] = index


# time complexity O(n)
# space complexity O(n)

lists = [2, 7, 11, 15]
target = 9

print(twoSum(lists, target))

lists = [3, 4, 2]
target = 6
print(twoSum(lists, target))

lists = [3, 3]
target = 6
print(twoSum(lists, target))

'''
https://leetcode.com/problems/two-sum/

1.Two Sum
---------

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

'''
