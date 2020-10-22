#Given a list of integers, return whether the largest number is bigger than the second-largest number by more than two times.
#For example, given the list [3, 9, 6], you should return false, since 9 is not bigger than 12 (2 times 6).
#Given the list [6, 3, 15], you should return true, since 15 is bigger than 12 (2 times 6).

class Solution:
    def solve(self, nums):
        nums.sort()
        max1=nums[len(nums)-1]
        max2=nums[len(nums)-2]  
        if max1>max2*2:
            return True 
        else:
            return False
