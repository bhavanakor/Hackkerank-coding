# Max Subarray Sum Limited by X

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array  **arr[]**  of integers and a number  **x**, find the sum of subarray having a maximum sum less than or equal to the given value of  **x**.

 **Examples:** 

```
Input: arr[] = [1, 2, 3, 4, 5], x = 11 
Output: 10
Explanation: Subarray having maximum sum is [1, 2, 3, 4].
```

```
Input: arr[] = [2, 4, 6, 8, 10], x = 7 
Output: 6
Explanation: Subarray having maximum sum is [2, 4] or [6].
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
1 ≤ x ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T05:40:15.630Z  

```py
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
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-sum-of-subarray-less-than-or-equal-to-x4033/1)