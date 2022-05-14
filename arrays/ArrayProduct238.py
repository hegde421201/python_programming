from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    pre_product, post_product = 1, 1
    LENGTH = len(nums)
    # result array
    result = [1] * LENGTH

    # step 1: We calculate the products on the prefix side (for all indices starting 0 till index - 1)
    for pre_index in range(1, LENGTH):
        pre_product *= nums[pre_index - 1]
        result[pre_index] = pre_product

    for post_index in range(LENGTH - 2,-1,-1):
        post_product *= nums[post_index+1]
        result[post_index] *= post_product
    return result


arrays = [2, 3, 4, 5]
print(productExceptSelf(arrays))

arrays = [-1,1,0,-3,3]
print(productExceptSelf(arrays))

'''

https://leetcode.com/problems/product-of-array-except-self/


238. Product of Array Except Self
-----------------------------------

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


'''