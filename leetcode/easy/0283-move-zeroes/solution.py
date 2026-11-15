class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for num in range(len(nums)):
            if nums[num]!=0:
                nums[num],nums[pos]=nums[pos],nums[num]
                pos+=1
        
        
