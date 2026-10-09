class Solution:
    def maxSubarraySum(self, arr, k):
        left=0
        window=0
        array=[]
        for right in range(len(arr)):
            window+=arr[right]
            if right-left+1 >k:
                window-=arr[left]
                left+=1
            if right-left+1==k:
                array.append(window)
        return max(array)