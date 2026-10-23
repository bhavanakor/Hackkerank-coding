# Sieve of Eratosthenes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a positive integer  **n**, calculate and return all primes less than or equal to n using the Sieve of Eratosthenes algorithm.

 **Examples:** 

```
Input: n = 10
Output: [2, 3, 5, 7]
Explanation: Prime numbers less than equal to 10 are 2, 3, 5 and 7.
```

```
Input: n = 35
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
Explanation: Prime numbers less than equal to 35 are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 and 31.
```

 **Constraints:** 
1 ≤ n ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T06:58:04.899Z  

```py
class Solution:
    def isprime(self,n):
        
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
            
    def sieve(self, n):
        res=[]
        for i in range(2,n+1):
            if self.isprime(i):
                res.append(i)
        return res
            
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1)