class Solution:
    def gcd(self, a, b):
        while b:
            a,b=b,a%b
        return a