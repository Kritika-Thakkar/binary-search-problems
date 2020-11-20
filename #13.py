"""
Given an integer n, return the nth (0-indexed) row of Pascal's triangle.

Pascal's triangle can be created as follows: In the top row, there is an array of 1. 
Subsequent row is created by adding the number above and to the left with the number above and to the right, treating empty elements as 0.
"""

class Solution:
    def solve(self, n):
        if n==0:
            return [1]
        if n==1:
            return [1,1]
        ls=[1,1]
        temp=[1,1]
        for i in range(2,n+1):
            ls=temp
            temp=[1]
            for i in range(len(ls)-1):
                temp.append(ls[i]+ls[i+1])
            temp.append(1)
        return temp
