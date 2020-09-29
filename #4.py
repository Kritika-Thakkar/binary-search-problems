#Given an integer n greater than or equal to 0, return the number of 1 bits in n.

class Solution:
    def solve(self, n):
        num=bin(n).replace("0b","")
        sum=0
        for i in list(num):
            sum+=int(i)
        return sum 
