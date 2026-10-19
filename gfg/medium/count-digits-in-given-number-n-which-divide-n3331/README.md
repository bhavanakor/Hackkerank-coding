# Digits in N that Divide it

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a  **non-negative**  integer  **s**  represented as a string, count the number of digits in s that divide the number represented by s.

A digit is considered valid only if it is non-zero and the number represented by s is  **divisible**  by that digit.

If a digit appears multiple times in s, each occurrence should be counted separately.

 **Examples:** 

```
Input: s = "35"
Output: 1
Explanation: The digit 5 divides 35, but the digit 3 does not. So the answer is 1.
```

```
Input: s = "1122324"
Output: 7
Explanation: Every digit in "1122324" divides 1122324. So the answer is 7.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T15:23:55.951Z  

```py
class Solution:    
    def divisibleByDigits(self,s):
        count=0
        memo={}
        for ch in s:
            digit=int(ch)
            if digit==0:
                continue
            if digit not in memo:
                rem=0
                for c in s:
                    rem=(rem*10+int(c))%digit
                memo[digit]=(rem==0)
            if memo[digit]:
                count+=1
        return count
                
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-digits-in-given-number-n-which-divide-n3331/1)