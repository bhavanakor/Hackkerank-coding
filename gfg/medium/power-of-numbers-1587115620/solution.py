class Solution:
    def reverseExponentiation(self, n):
        p=str(n)[::-1]
        rev=int(p)
        return pow(n,rev)
        