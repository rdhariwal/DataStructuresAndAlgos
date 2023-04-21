from binary_search import Solution

class TestBinarySearch:
    def test_binary_search(self):
        input = [-1,0,3,5,9,12]
        target = 9
        expected = 4
        sol = Solution()
        res = sol.binary_search(input, target)

        assert expected is res

    def test_invalid_binary_search(self):
            input = [-1,0,3,5,9,12]
            target = 2
            expected = -1
            sol = Solution()
            res = sol.binary_search(input, target)

            assert expected is res

    def test_empty_binary_search(self):
            input = []
            target = 2
            expected = -1
            sol = Solution()
            res = sol.binary_search(input, target)

            assert expected is res