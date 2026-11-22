class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)-1):
            j=i
            while j>=0 and nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                j-=1

                    