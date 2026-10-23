class Solution:
    def findGCD(self, nums: list[int]) -> int:
        smallest=abs(min(nums))
        largest=abs(max(nums))
        while smallest>0:
            largest,smallest=smallest,largest%smallest
        return largest

        