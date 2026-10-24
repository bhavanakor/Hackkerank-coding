class Solution:
    def maxSubarraySum(self, arr, k):
        left=0
        window_sum=0
        current=0
        for right in range(len(arr)):
            window_sum+=arr[right]
            if right-left+1>k:
                window_sum-=arr[left]
                left+=1
            if right-left+1==k:
                current=max(current,window_sum)
        return current
                
                