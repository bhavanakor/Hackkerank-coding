class Solution:
    def findIntersection(self, a: list[int], b: list[int]) -> list[int]:
        find={}
        result=[]
        for i in range(len(b)):
            find[b[i]]=i
        for j in a:
            if j in find.keys():
                result.append(j)
        return result
                
                
        
                
                
            