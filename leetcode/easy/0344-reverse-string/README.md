# Reverse String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

 

Original
Python3
 **Example 1:** 

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

```

 **Example 2:** 

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s[i] is a printable ascii character.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 58.09%)  
**Memory:** 23.4 MB (beats 46.23%)  
**Submitted:** 2026-11-15T17:01:16.162Z  

```py
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-string/)