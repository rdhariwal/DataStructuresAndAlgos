# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from two_sum import twoSum

class TestTwoSum:
    def test_two_1sum(self):
        s = [3,2,4]
        t = 6
        expected = (1,2)
        result = twoSum(s, t)
        assert expected == result

    def test_two_2sum(self):
        s = [3,3]
        t = 6
        expected = (0,1)
        result = twoSum(s, t)
        assert expected == result

    def test_two_3sum(self):
        s = [2,7,11,15]
        t = 9
        expected = (0,1)
        result = twoSum(s, t)
        assert expected == result