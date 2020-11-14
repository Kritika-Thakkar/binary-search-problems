#Given three numbers, a, b, and c, return their product, but if any two numbers are the same, they do not count.

class Solution:
    def solve(self, a, b, c):
        product = 0

        if a == b == c:
            product = 1
        elif a == b:
            product = c
        elif a == c:
            product = b
        elif b == c:
            product = a
        else:
            product = a * b * c
        return product
