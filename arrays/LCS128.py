'''
https://leetcode.com/problems/longest-consecutive-sequence/

LEETCODE

128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:
--------------
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    numset = set(nums)  # step 1 create a set from the list of numbers
    longest = 0
    # step 2 : For each number in the list, check whether it has a left neighbour in the set. If yes then it is not
    # start of sequence else it is!
    for number in nums:
        if (number - 1) not in numset:
            length = 0 # length is calculated
            while (number + length) in numset: # check the right neighbour for the current number
                length += 1
            longest = max(longest,length)
    return longest
