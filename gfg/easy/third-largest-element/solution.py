class Solution:
    def thirdLargest(self,arr):
        ans=sorted(arr)
        if len(ans)<3:
            return -1
        else:
            return ans[-3]