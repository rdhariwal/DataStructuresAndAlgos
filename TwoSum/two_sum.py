# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums: list[int], target: int):
    numList = {}
    i1 = 0
    i2 = 0
    for i in range(len(nums)):
        if nums[i] not in numList:
         numList[nums[i]] = [i]
        else:
           numList[nums[i]].append(i)

    for i in range(len(nums)):
       num2 = target - nums[i]
       if num2 == nums[i]:
        if len(numList[nums[i]]) > 1:
          i1 = i
          i2 = numList[nums[i]][1]
          break
        else:
          continue
       if num2 not in numList:
          continue
       else:
          i1 = i
          i2 = numList[num2][0]
          break
    return (i1,i2)