'''

https://www.lintcode.com/problem/659/
Description
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Input: ["lint","code","horse","power"]
Output: ["lint","code","horse","power"]
Explanation:
One possible encode method is: "lint:;code:;horse:;power"

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

'''

"""
   @param: strs: a list of strings
   @return: encodes a list of strings to a single string.
"""


def encode(self, strs):
    # write your code here
    result = ""
    delimiter = "$"
    for string in strs:
        result += str(len(string)) + delimiter + string
    return result


"""
@param: str: A string
@return: decodes a single string to a list of strings
"""


def decode(self, str):
    # write your code here
    result, index, delimiter = [], 0, "$"

    while index < len(str):
        p = index
        while str[p] != delimiter:
            p += 1
        length = int(str[index: p])
        result.append(str[p+1: p+1+length])
        index = p + 1 + length
    return result
