"""
Given an integer n, return a list with each number from 1 to n, except if it's a multiple of 3 or has a 3, 6, or 9 in the number, 
it should be the string "clap".

Note: return the number as a string.
"""

class Solution:
    def solve(self, n):
        string = "clap"
        ls=[str(i) for i in range(1,n+1)]
        for i in range(len(ls)):
            if int(ls[i])%3==0:
                ls[i]=string
            elif '3' in ls[i]:
                ls[i]=string
            elif '6' in ls[i]:
                ls[i]=string
            elif '9' in ls[i]:
                ls[i]=string
        return ls
