# Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` if `x` is a  **palindrome**, and `false` otherwise.

 

Original
Python3
 **Example 1:** 

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

 **Example 2:** 

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

 **Example 3:** 

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

 

 **Follow up:**  Could you solve it without converting the integer to a string?

## Solution

**Language:** Python  
**Runtime:** 19 ms (beats 16.99%)  
**Memory:** 19.3 MB (beats 11.77%)  
**Submitted:** 2026-11-22T07:35:50.475Z  

```py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        org=x
        reverse=0
        while x>0:
            digit=x%10
            reverse=(reverse*10)+digit
            x//=10
        if org==reverse:
            return True
        else:
            return False



        
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-number/)