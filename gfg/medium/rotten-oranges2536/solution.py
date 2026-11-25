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
		          
		            