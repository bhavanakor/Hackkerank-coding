# Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer `n`. Your task is to find if it is a palindrome.

 **Examples:** 

```
Input: n = 555
Output: true
Explanation: The number 555 reads the same backward as forward, so it is a palindrome.
```

```
Input: n = 123
Output: false
Explanation: The number 123 reads differently backward (321), so it is not a palindrome.
```

```
Input: n = -121
Output: true
Explanation: if number is palindrome, mainly ignore sign.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T17:07:06.866Z  

```py
class Solution:
    def isPalindrome(self, n):
		rev=str(abs(n))[::-1]
		if rev==str(abs(n)):
		    return True
		else:
		    return False
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/palindrome0746/1)