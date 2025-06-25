#https://leetcode.com/problems/count-and-say/


class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)  # Use self. here
        result = ""
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1

        result += str(count) + prev[-1]
        return result
