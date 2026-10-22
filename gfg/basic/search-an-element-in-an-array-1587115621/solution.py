class Solution:
    def search(self, arr, x):
        for index,value in enumerate(arr):
            if value==x:
                return index
        return -1