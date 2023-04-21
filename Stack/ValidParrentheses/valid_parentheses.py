# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.

class Solution:
    def is_valid_patentheses(self, s: str) -> bool:
        is_valid = False
        s_length = len(s)
        
        if s_length <= 1:
            return False
        
        if s_length % 2 != 0:
            return False
        
        open = []
        cb_exception = False

        for char in s:
            if char == "[" or char == "(" or char == "{":
                open.append(char)
            elif len(open) > 0:
                li = open.pop()
                if (li == "[" and char == "]") or (li == "(" and char == ")")  or (li == "{" and char == "}"):   # noqa: E501
                    continue
                else:
                    is_valid = False
                    open.append(li)
                    return False
            else:
                is_valid = False
                cb_exception = True
                break
        
        # account for any unclosed brackets
        if len(open) == 0 and cb_exception is False:
            is_valid = True

        return is_valid