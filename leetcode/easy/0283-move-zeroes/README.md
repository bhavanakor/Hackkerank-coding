# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

Original
Python3
 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 84.41%)  
**Memory:** 20.3 MB (beats 74.12%)  
**Submitted:** 2026-11-15T17:01:25.234Z  

```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for num in range(len(nums)):
            if nums[num]!=0:
                nums[num],nums[pos]=nums[pos],nums[num]
                pos+=1
        
        

```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)