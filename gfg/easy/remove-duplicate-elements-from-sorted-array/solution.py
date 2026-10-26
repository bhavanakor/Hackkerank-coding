class Solution:
    def removeDuplicates(self, arr):
        a=set(arr)
        return sorted(list(a))