#https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen= {}
        for i,x in enumerate(nums):
            y= target - x
            if y in seen:
                return(seen[y], i)
            seen[x]= i
