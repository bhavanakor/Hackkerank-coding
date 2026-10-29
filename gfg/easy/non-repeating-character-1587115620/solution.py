class Solution:
    def nonRepeatingChar(self,s):
        dick={}
        for i in range(len(s)):
            if s[i] in dick:
                dick[s[i]]+=1
            else:
                dick[s[i]]=1
        for key,value in dick.items():
            if value==1:
                return key
        return "$"
    