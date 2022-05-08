from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # step 1 : define a hashmap with key as the element of the List and the corresponding value as the index in the List
    hashmap = dict()
    
