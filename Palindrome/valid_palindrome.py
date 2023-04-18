# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters
# , it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
import re

def valid_plaindrome(s: str) ->bool:
    """ Check if string is Palindrome; return true id string is 
        palindrome otherwise false
    """
    result = True
    loop_count = 0
    formatted_s = re.sub(r'[^a-z0-9]+', '', s, flags=re.IGNORECASE).lower()
    s_len = len(formatted_s)
    if s_len <= 1:
        return True
    elif s_len % 2 == 0:
        # account for even char string
        loop_count = int(s_len / 2)
    else:
        # account for odd number of chars in string
        loop_count = int(s_len / 2) + 1
    
    for i in range(loop_count):
        if formatted_s[i] != formatted_s[s_len-i-1]:
            result = False
            break
    return result