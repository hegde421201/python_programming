def isAnagram(s: str, t: str) -> bool:
    # Step 1: If the lengths of the strings s and t are unequal then they cannot be anagrams of each other - return
    # False
    if len(s) != len(t):
        return False

    # Step 2:  define two empty dictionaries for strings s and t that holds a mapping of characters and their
    # corresponding count
    dict_s, dict_t = dict(), dict()

    # Step 3: Read each character in string s and add to the dictionary for s
    for character in s:
        dict_s[character] = dict_s.get(character, 0) + 1

    # Step 4: Ditto as step 3 but this time for string t
    for character in t:
        dict_t[character] = dict_t.get(character, 0) + 1

    # Step 5: Compare the keys and their corresponding value counts for both dictionaries and return true or false

    for key in dict_s:
        if dict_s[key] != dict_t.get(key, 0):
            return False
    return True


'''

https://leetcode.com/problems/valid-anagram/

242. Valid Anagram
----------------

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

'''

