# 4Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array `nums` of `n` integers, return  *an array of all the  **unique**  quadruplets*  `[nums[a], nums[b], nums[c], nums[d]]` such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

```

 **Example 2:** 

```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 200
- -109 <= nums[i] <= 109
- -109 <= target <= 109

## Solution

**Language:** Python  
**Runtime:** 400 ms (beats 48.22%)  
**Memory:** 19.1 MB (beats 94.85%)  
**Submitted:** 2026-10-26T12:03:47.008Z  

```py
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        for a in range(n-3):
            if a>0 and nums[a]==nums[a-1]:
                continue
            for b in range(a+1,n-2):
                if b>a+1 and nums[b]==nums[b-1]:
                    continue
                left=b+1
                right=n-1
                while left<right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]
                    if total==target:
                        result.append([nums[a],nums[b],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/4sum/)