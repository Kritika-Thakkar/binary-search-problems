#Given a non-negative integer num, return whether it is a palindrome. Bonus: Can you solve it without using strings?

class Solution:
    def solve(self, num):
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            return True
        else:
            return False
