#https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        seen= {}
        for i,x in enumerate(nums):
            y= target - x
            if y in seen:
                return(seen[y], i)
            seen[x]= i


#----------------OR-----------------


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return -1
