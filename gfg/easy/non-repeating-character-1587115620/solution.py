class Solution:
    def nonRepeatingChar(self,s):
        dick={}
        for x in s:
            if x in dick:
                dick[x]+=1
            else:
                dick[x]=1
        for key,value in dick.items():
            if value==1:
                return key
        return "$"
    