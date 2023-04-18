from valid_anagram import IsStringAnagram

class TestValidAnagram:
    def test_anagram_nagaram(self):
        s = "anagram"
        t = "nagaram"
        assert True is IsStringAnagram(s, t)

    def test_rat_cat(self):
        s = "rat"
        t = "cat"
        assert False is IsStringAnagram(s, t)