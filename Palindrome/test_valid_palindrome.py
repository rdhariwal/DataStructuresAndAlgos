from valid_palindrome import valid_plaindrome

class TestValidPalindrome:
    def test_valid_palindrome_string(self):
        expected = True
        s = "A man, a plan, a canal: Panama"
        result = valid_plaindrome(s)
        # "amanaplanacanalpanama" is a palindrome.
        assert expected == result

    def test_2_palindrome_string(self):
        expected = False
        s = "race a car"
        result = valid_plaindrome(s)
        # "raceacar" is not a palindrome.
        assert expected == result

    def test_3_palindrome_string(self):
        expected = True
        s = " "
        result = valid_plaindrome(s)
        # s is an empty string "" after removing non-alphanumeric characters.
        # Since an empty string reads the same forward and backward, it is a palindrome.
        assert expected == result
    