from buy_sell_stock import Solution

class TestValidPalindrome:
    def test_Max_5Profit(self):   
        sol = Solution()
        prices = [7,1,5,3,6,4]
        result = sol.max_profit(prices)
        expected = 5
        assert result is expected