# Rotten Oranges

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a matrix  **mat[][]**, where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
 **0** : Empty cell
 **1**  : Cell have fresh oranges
 **2**  : Cell have rotten oranges

Determine the minimum time required so that all the oranges become rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

 **Note**  **:**  If it is impossible to rot every orange then simply return -1.

 **Examples:** 

```
Input: mat[][] = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
Output: 2
Explanation: 

Oranges at positions (0,0), (0,3), (1,3), and (2,3) will rot adjacent fresh oranges in successive time frames.
All fresh oranges become rotten after 2 units of time.
```

```
Input: mat[][] = [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
Output: -1
Explanation: Oranges at positions (0,0), (0,3), (1,3), and (2,3) rot some fresh oranges,
but the fresh orange at (2,0) can never be reached, so not all oranges can rot.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-25T07:29:05.384Z  

```py
from collections import deque
class Solution:
	def orangesRot(self, mat):
	    queue=deque()
	    fresh=0
		for i in range(len(mat)):
		    for j in range(len(mat[0])):
		        if mat[i][j]==2:
		            queue.append((i,j))
		        elif mat[i][j]==1:
		            fresh+=1
		directions=[
		    (-1,0),
		    (1,0),
		    (0,-1),
		    (0,1)
		    ]
		minutes=0
		while queue and fresh>0:
		    size=len(queue)
		    for _ in range(size):
		        r,c=queue.popleft()
		        for dr,dc in directions:
		            nr=r+dr
		            nc=c+dc
		            if 0<=nr<len(mat) and 0<=nc<len(mat[0]) and mat[nr][nc]==1:
		                mat[nr][nc]=2
		                fresh-=1
		                queue.append((nr,nc))
		    minutes+=1
		return minutes if fresh==0 else -1
		          
		            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/rotten-oranges2536/1)