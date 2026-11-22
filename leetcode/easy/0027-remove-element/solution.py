class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pos=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[pos],nums[i]=nums[i],nums[pos]
                pos+=1
        count=0
        for x in nums:
            if x!=val:
                count+=1
            else:
                return count
            
            