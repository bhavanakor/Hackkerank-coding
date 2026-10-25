# Check if Permutation is Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings  **txt** and  **pat** having lowercase letters, the task is to check if any permutation of  **pat**  is a substring of  **txt**.

 **Examples:** 

```
Input: txt = "geeks", pat = "eke"
Output: true
Explanation: "eek" is a permutation of "eke" which exists in "geeks".
```

```
Input: txt = "programming", pat = "rain"
Output: false
Explanation: No permutation of "rain" exists as a substring in "programming".

```

 **Constraints:** 
1 ≤ txt.size() ≤ 105
1 ≤ pat.size() ≤ txt.size()
Both the strings consist of lowercase English alphabets.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T03:40:35.435Z  

```py
from collections import Counter
class Solution:
    def search(self, txt, pat):
        left=0
        k=len(pat)
        patc=Counter(pat)
        winc=Counter()
        for right in range(len(txt)):
            winc[txt[right]]+=1
            if right-left+1>k:
                winc[txt[left]]-=1
                left+=1
            if right-left+1==k:
                if winc==patc:
                    return True
        return False
            
            
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-permutation-is-substring/1)