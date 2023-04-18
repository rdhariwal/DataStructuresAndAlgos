def IsStringAnagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)