# Smallest Window With 0, 1 and 2

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **s**  consisting only of the characters ' **0'**, ' **1'**  and ' **2'**, determine the length of the smallest substring that contains all three characters at least once.

If no such substring exists, return  **-1**.

 **Examples :** 

```
Input: s = "10212"
Output: 3
Explanation: The substring "102" is the shortest substring that contains all three characters '0', '1', and '2', so the answer is 3.
```

```
Input: s = "12121"
Output: -1
Explanation: The character '0' is not present in the string, so no substring can contain all three characters '0', '1', and '2'. Hence, the answer is -1.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-24T06:33:43.801Z  

```py
class Solution:
    def smallestSubstring(self, s):
        seen={'0':-1,'1':-1,'2':-1}
        left=0
        min_len=float('inf')
        for right in range(len(s)):
            seen[s[right]]=right
            if seen['0']!=-1 and seen['1']!=-1 and seen['2']!=-1:
                left=min(seen['0'],seen['1'],seen['2'])
                current=right-left+1
                min_len=min(min_len,current)
        return min_len if min_len!=float('inf') else -1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1)