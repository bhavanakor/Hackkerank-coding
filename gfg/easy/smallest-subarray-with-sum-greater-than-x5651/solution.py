class Solution:
    def smallestSubWithSum(self, x, arr):
        left=0
        window_sum=0
        min_len=float('inf')
        best_s=float('-inf')
        best_e=float('-inf')
        for right in range(len(arr)):
            window_sum+=arr[right]
            while window_sum>x:
                if right-left+1<min_len:
                    min_len=right-left+1
                    best_s=left
                    best_e=right
                window_sum-=arr[left]
                left+=1
        if min_len==float('inf'):
            return 0
        return min_len