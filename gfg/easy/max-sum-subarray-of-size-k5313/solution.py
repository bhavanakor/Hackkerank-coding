class Solution:
    def maxSubarraySum(self, arr, k):
        left=0
        maximum=float('-inf')
        window=0
        n=len(arr)
        for right in range(n):
            window+=arr[right]
            if right-left+1>k:
                window-=arr[left]
                left+=1
            if right-left+1==k:
                maximum=max(maximum,window)
        return maximum