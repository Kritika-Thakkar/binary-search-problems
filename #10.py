#Given a string s representing a phrase, return its acronym. Acronyms should be capitalized and should not include the word "and".
#Input: For Your Information
#Output: FYI

class Solution:
    def solve(self, s):
        tokens=s.split()
        string=""
        for word in tokens:
            if word != "and":
                string += str(word[0])
        return string.upper()
        
