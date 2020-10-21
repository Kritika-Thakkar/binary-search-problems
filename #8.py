#Given a lowercase alphabet string s, return a string with all the vowels of s in sorted order followed by all the consonants of s in sorted order.
#Note: vowels are ["a", "e", "i", "o", "u"] and consonants are all other characters.
#Example: extraordinary
#output: aaeiodnrrtxy

class Solution:
    def solve(self, s):
        vowels = ['a','e','i','o','u'] 
        k = ''
        t = ''
        for c in s:
            if c in vowels:
                k = k + c
            else :
                t = t + c
        k = ''.join(sorted(k))
        t = ''.join(sorted(t))
        return k + t
