from contains_duplicate import ContainsDuplicate

class TestContainsDuplicate:
    def test_dupes(self):
        nums = [1,2,3,1]
        assert True is ContainsDuplicate(nums)

    def test_nodupes(self):
        nums = [1,2,3,4]
        assert False is ContainsDuplicate(nums)

    def test_multidupes(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        assert True is ContainsDuplicate(nums)