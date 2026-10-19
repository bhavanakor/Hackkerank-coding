# Reverse Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer  **n.** Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.

 **Examples:** 

```
Input: n = 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221.

```

```
Input : n = 200
Output: 2
Explanation: By reversing the digits of number, number will change into 2.
```

```
Input : n = 12345 
Output: 54321
Explanation: By reversing the digits of number, number will change into 54321.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T15:33:35.307Z  

```py
class Solution:
	def reverseDigits(self, n):
		p=str(n)
		return int(p[::-1])
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/reverse-digit0316/1)