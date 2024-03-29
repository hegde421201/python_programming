from typing import List


def containsDuplicate(nums: List[int]) -> bool:

    # Step 1: We define a hsh set whose characteristic is to hold unique elements only
    nums_set = set()

    # We iterate over each element in the list and check whether that element exists in the set already. If yes,
    # then we have found the list which contains duplicate elements.
    for n in nums:
        if n in nums_set:
            return True
        # We add the element to the set if it is not present already
        nums_set.add(n)
    return False

# Time complexity is O(n)
# Space complexity O(n)

'''
https://leetcode.com/problems/contains-duplicate/

Problem 217 Leetcode
--------------------
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 10^5
-109 <= nums[i] <= 10^9




'''