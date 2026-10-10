class Solution:
    def maxSum(self, arr, x):
        left=0
        window_sum=0
        maximum=0
        for right in range(len(arr)):
            window_sum+=arr[right]
            while window_sum>x:
                window_sum-=arr[left]
                left+=1
            maximum=max(maximum,window_sum)
        return maximum
            