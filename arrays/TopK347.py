'''
347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/


Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

'''
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # step 1: The total size of the list is len(nums). The worst case that only one element is present in the
    # element and that occurs in each cell of the list. We define a list called frequency that takes care of this
    # We create a vector named frequency consisting of one row and columns equal to (size of array + 1)

    ROWS = 1
    COLUMNS = len(nums) + 1
    frequency = []
    for i in range(COLUMNS):
        row = [] * ROWS
        frequency.append(row)

    # step 2: hashmap with key as the element and the corresponding value is the frequency of its occurrence in List
    countMap = dict()

    # step 3 : Update the hashmap or dictionary
    for element in nums:
        # increment the hashmap value by 1 if the element is encountered again ( default value is 0 if key is absent)
        DEFAULT = 0
        countMap[element] = countMap.get(element, DEFAULT) + 1

    for key, value in countMap.items():
        frequency[value].append(key)

    length = len(frequency)
    result = []

    while length >= 0:

        length -= 1

        if len(frequency[length]) != 0:
            for x in frequency[length]:
                result.append(x)
                if len(result) == k:
                    return result

    return result


print(topKFrequent([1, 1, 1, 2, 2, 2, 4, 4, 4, 6, 6, 100], 3))
print(topKFrequent([1, 1, 1, 2, 2, 4, 4, 6, 6, 100], 2))
