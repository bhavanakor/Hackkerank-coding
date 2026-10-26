class Solution:
	def twoSum(self, arr, target):
		left=0
		find=set()
		for a in arr:
		    b=target-a
		    if b in find:
		        return True
		    find.add(a)
		return False
		    