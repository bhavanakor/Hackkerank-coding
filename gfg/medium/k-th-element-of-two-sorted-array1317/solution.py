class Solution:
    def kthElement(self, a, b, k):
        cl=a+b
        cl[:]=sorted(cl)
        return cl[k-1]