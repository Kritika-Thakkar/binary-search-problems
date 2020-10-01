#Given two sorted lists of integers, merge them into one large sorted list. For example, given these two lists:
#lst0 = [5, 10, 15]
#lst1 = [3, 8, 9]
#Return [3, 5, 8, 9, 10, 15].

class Solution:
    def solve(self, lst0, lst1):
        lst2=lst0+lst1
        return sorted(lst2)
