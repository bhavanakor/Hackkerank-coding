# Perfect Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a number  **n,**  check if the number is  **perfect**  or not. A number is said to be perfect if  **sum**  of all its factors excluding the number itself is equal to the  **number**.

 **Examples:** 

```
Input: n = 6
Output: true 
Explanation: Factors of 6 are 1, 2, 3 and 6. Excluding 6 their sum is 6 which is equal to n itself. So, it's a Perfect Number.
```

```
Input: n = 10
Output: false
Explanation: Factors of 10 are 1, 2, 5 and 10. Excluding 10 their sum is 8 which is not equal to n itself. So, it's not a Perfect Number.

```

```
Input: n = 15
Output: false
Explanation: Factors of 15 are 1, 3, 5, 15. Excluding 15 their sum is 9 which is not equal to n itself. So, it's not a Perfect Number.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T17:26:00.146Z  

```py
class Solution:
    def isPerfect(self, n):
        total=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                total+=i
                if i!=n//i and n//i!=n:
                    total+=n//i
        if total==n:
            return True
        else:
            return False
            
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/perfect-numbers3207/1)