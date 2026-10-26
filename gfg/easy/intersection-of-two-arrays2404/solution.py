class Solution:
    def findIntersection(self, a: list[int], b: list[int]) -> list[int]:
        # code here
        setb=set(b)
        result=[]
        for x in a:
            if x in setb:
                result.append(x)
        return result