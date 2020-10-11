#Given a non-negative integer n, find a number r such that r * r = n and round down to the nearest integer.

class Solution:
    def solve(self, n):
        if (n == 0 or n == 1) : 
            return n
        start = 1
        end = n    
        while (start <= end) : 
            mid = (start + end) // 2
            if (mid*mid == n) : 
                return mid
            if (mid * mid < n) : 
                start = mid + 1
                ans = mid 
            else:
                end = mid-1
        return ans
