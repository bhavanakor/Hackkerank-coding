class Solution:
    def isSubset(self, a, b):
        freq={}
        for x in a:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        
        for x in b:
            if x in freq and freq[x]>0:
                freq[x]-=1
            else:
                return False
        return True