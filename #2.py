#Given an integer n, return whether it is equal to the sum of its own digits raised to the power of the number of digits.

class Solution:
    def solve(self, n):
        sum=0
        temp=n
        while temp>0:
            digit=temp%10
            temp//=10
            sum+=digit**digits(n)
        return(sum==n)
def digits(n):
    count = 0
    while n != 0: 
        n //= 10
        count+= 1
    return count
