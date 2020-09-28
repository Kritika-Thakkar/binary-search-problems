#Given a positive integer num, return the sum of its digits.

class Solution:
    def solve(self, num):
        sum=0
        self=0
        while(num!=0):
            sum = sum + int(num%10)
            num = int(num/10)
        return sum
    num=123
    print(solve(0,num))
