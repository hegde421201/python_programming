def isPalindrome2(s: str) -> bool:
    # step 1: convert lower case to upper case
    s = s.lower()

    # step 2: define two pointers to scan from the left and the right of the string
    left = 0
    right = len(s) - 1

    # step 3: check whether the two indices cross-over or not. If not continue
    while left <= right:

        while left < right and not check_alpha_numeric(s[left]):
            left += 1

        while left < right and not check_alpha_numeric(s[right]):
            right -= 1

        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def check_alpha_numeric(ch) -> bool:
    return ord('a') <= ord(ch) <= ord('z') or ord('0') <= ord(ch) <= ord('9')


file = open("input125.txt","r")
# read each character and append to a single string

delimiter = ""
string = ""
for line in file:
    for chars in line:
        string += delimiter.join(chars)

print(isPalindrome2("A man, a plan, a canal: Panama"))
print(isPalindrome2("Malayalam"))
print(isPalindrome2('racecar'))
print(isPalindrome2('......a.....'))
print(isPalindrome2(" "))
print(isPalindrome2(string))