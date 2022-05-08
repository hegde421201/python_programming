'''

49. Group Anagrams

https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

'''


def groupAnagrams(strings: list[str]) -> list[list[str]]:

    # step 1: define a dictionary
    result = dict()  # map the character count to the list of Anagrams

    # constant defining total letters in english (lowercase)
    TOTAL_ALPHABETS = 26

    # the list to be returned as an answer
    emptyList = []

    # we define for loop that contains the count of each english lowercase letter
    for element in strings:
        array = [0] * TOTAL_ALPHABETS

        # above array is populated using the ascii value obtained from the ord function
        for character in element:
            array[ord(character) - ord('a')] += 1

        # dictionary requires hashable key --- so we convert array to tuple
        tuples = tuple(array)

        # the default value for the key is an empty list if the key were to be inserted for the first time
        result.setdefault(tuples, []).append(element)

    # iterating over the key-value pairs in the dictionary
    for key, value in result.items():
        emptyList.append(value)

    return emptyList


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
