# Smallest window containing 0, 1 and 2

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **s**  consisting only of the characters ' **0'**, ' **1'**  and ' **2'**, determine the length of the  **smallest substring**  that contains all three characters at least once.

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

 **Constraints:** 
1 ≤ s.size() ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T05:22:52.224Z  

```py
class Solution:
    def smallestSubstring(self, s):
        left=0
        window=""
        min_len=float('inf')
        count={'0':0, '1':0,'2':0}
        for right in range(len(s)):
            count[s[right]]+=1
            while count['0'] >0 and count['1']>0 and count['2']>0:
                min_len=min(min_len,right-left+1)
                count[s[left]]-=1
                left+=1
        return min_len if min_len!=float('inf') else -1
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1)