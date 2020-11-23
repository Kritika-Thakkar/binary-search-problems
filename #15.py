"""
Given two strings s0 and s1, return the two strings interleaved, starting with s0. 
If there are leftover characters in a string they should be added to the end.

"""

class Solution:
    def solve(self, s0, s1):
        if len(s0)<=len(s1):
            res = "".join([s0[i] + s1[i] for i in range(len(s0))]) + s1[len(s0):]
            return res
        else:
            s=list(s1)
            for i,c in enumerate(s0):
                s.insert(i*2,c)
            rest="".join(s)
            return (rest)
