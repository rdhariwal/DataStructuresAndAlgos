from valid_parentheses import Solution

class TestValidParentheses:
    def test_valid_string(self):
        sol = Solution()
        input = "()"
        result = sol.is_valid_patentheses(input)

        assert result is True

    def test_valid2_string(self):
        sol = Solution()
        input = "()[]{}"
        result = sol.is_valid_patentheses(input)

        assert result is True

    def test_invalid_string(self):
        sol = Solution()
        input = "(}"
        result = sol.is_valid_patentheses(input)

        assert result is False

    def test_invalid1_string(self):
        sol = Solution()
        input = "({"
        result = sol.is_valid_patentheses(input)

        assert result is False