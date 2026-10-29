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
**Submitted:** 2026-10-29T16:50:40.813Z  

```py
class Solution:
    def nonRepeatingChar(self,s):
        dick={}
        for i in range(len(s)):
            if s[i] in dick:
                dick[s[i]]+=1
            else:
                dick[s[i]]=1
        for key,value in dick.items():
            if value==1:
                return key
        return "$"
    
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1)