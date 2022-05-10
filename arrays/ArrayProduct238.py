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
