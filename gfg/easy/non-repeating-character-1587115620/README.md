# Non Repeating Character

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **s**  consisting of lowercase English Letters. return the first non-repeating character in  **s**. If there is no non-repeating character, return  **'$'**.

 **Examples:** 

```
Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.
```

```
Input: s = "racecar"
Output: 'e'
Explanation: In the given string, 'e' is the only character in the string which does not repeat.
```

```
Input: s = "aabbccc"
Output: '$'
Explanation: All the characters in the given string are repeating.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T16:54:47.331Z  

```py
class Solution:
    def nonRepeatingChar(self,s):
        dick={}
        for x in s:
            if x in dick:
                dick[x]+=1
            else:
                dick[x]=1
        for key,value in dick.items():
            if value==1:
                return key
        return "$"
    
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1)