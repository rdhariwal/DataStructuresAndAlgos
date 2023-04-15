# Given an integer array `nums`, return `true` if any value appears at least twice in the array, 
# and return `false` if every element is distinct.

def ContainsDuplicate(nums):
    result = False
    dict = {}
    for num in nums:
        if num in dict:
            return True
        else:
            dict[num] = True
    return result


# True
nums = [1,2,3,1]
print(ContainsDuplicate(nums))

# False
nums = [1,2,3,4]
print(ContainsDuplicate(nums))

# True
nums = [1,1,1,3,3,4,3,2,4,2]
print(ContainsDuplicate(nums))

