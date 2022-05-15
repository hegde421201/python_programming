from typing import List


def countBits(n: int) -> List[int]:
    result = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if i == 2 * offset:
            offset = i
        result[i] = 1 + result[i - offset]

    return result


print(countBits(4))

'''

338. Counting Bits

https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 
such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 10^5

'''