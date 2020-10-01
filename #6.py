#Given a list of integers nums, find the most frequently occurring element and return the number of occurrences of that element. For example, given the list [1, 4, 1, 7, 1, 7, 1, 1], return 5 since the the element 1 appears 5 times.

class Solution:
    def solve(self, nums):
        count = 0
        temp=nums[0]
        for i in nums:
            freq=nums.count(i)
            if(freq>count):
                count = freq
                temp=i
        return count
