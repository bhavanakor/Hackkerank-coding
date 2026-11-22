# Squares of a Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums` sorted in  **non-decreasing**  order, return  *an array of  **the squares of each number**  sorted in non-decreasing order*.

 

Original
Python3
 **Example 1:** 

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```

 **Example 2:** 

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.

 

 **Follow up:**  Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 56.10%)  
**Memory:** 21.2 MB (beats 25.50%)  
**Submitted:** 2026-11-22T05:56:00.594Z  

```py
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=n*[0]
        left=0
        right=n-1
        pos=n-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[pos]=nums[left]*nums[left]
                left+=1
                pos-=1
            else:
                result[pos]=nums[right]*nums[right]
                right-=1
                pos-=1
        return result
         

       
       

```

---

[View on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)