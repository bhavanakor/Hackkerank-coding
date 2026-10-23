class Solution:
    def checkPermutation(self, a: list[int], b: list[int]) -> bool:
        if sorted(a)==sorted(b):
            return True
        else:
            return False