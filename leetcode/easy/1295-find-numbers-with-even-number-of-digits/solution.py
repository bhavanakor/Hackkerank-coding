class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        numb=0
        for num in nums:
            count=0
            while num>0:
                count+=1
                num//=10
            if count%2==0:
                numb+=1
        return numb


        