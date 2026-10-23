class Solution:
    def frequencyCount(self, arr):
        freq={}
        for i in range(1,len(arr)+1):
            freq[i]=0
        for x in arr:
            if x in freq:
                freq[x]+=1
        return list(freq.values())
            
