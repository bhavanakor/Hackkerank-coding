# Find Numbers with Even Number of Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of integers, return how many of them contain an  **even number**  of digits.

 

 **Example 1:** 

```
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

```

 **Example 2:** 

```
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

```

 

 **Constraints:** 

- 1 <= nums.length <= 500
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 39.96%)  
**Memory:** 19.2 MB (beats 89.74%)  
**Submitted:** 2026-10-23T05:38:43.057Z  

```py
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        numb=0
        for num in nums:
            count=0
            while num>0:
                count+=1
                num//=10
            if count%2==0:
                numb+=1
        return numb


        
```

---

[View on LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)