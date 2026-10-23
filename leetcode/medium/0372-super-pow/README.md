# Super Pow

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Your task is to calculate `ab` mod `1337` where `a` is a positive integer and `b` is an extremely large positive integer given in the form of an array.

 

 **Example 1:** 

 **Input:**  a = 2, b = [3]

 **Output:**  8

 **Explanation:** 

The array `b = [3]` represents the exponent 3. Therefore, `a3 = 23 = 8`, so the result is 8.

 **Example 2:** 

 **Input:**  a = 2, b = [1,0]

 **Output:**  1024

 **Explanation:** 

The array `b = [1, 0]` represents the exponent 10. Therefore, `a10 = 210 = 1024`, so the result is 1024.

 **Example 3:** 

 **Input:**  a = 1, b = [4,3,3,8,5,2]

 **Output:**  1

 **Explanation:** 

The array `b = [4, 3, 3, 8, 5, 2]` represents a positive exponent. Since `a = 1`, any positive power of 1 is 1. Therefore, the result is 1.

 

 **Constraints:** 

- 1 <= a <= 231 - 1
- 1 <= b.length <= 2000
- 0 <= b[i] <= 9
- b does not contain leading zeros.

## Solution

**Language:** Python  
**Runtime:** 9 ms (beats 76.17%)  
**Memory:** 19.1 MB (beats 98.89%)  
**Submitted:** 2026-10-23T07:56:18.384Z  

```py
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        string=""
        for i in b:
            string+=str(i)
        num=int(string)
        return pow(a,num,1337)
        
```

---

[View on LeetCode](https://leetcode.com/problems/super-pow/)