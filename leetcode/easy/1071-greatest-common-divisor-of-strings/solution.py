class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        if len(str1)<len(str2):
            a=len(str2)
            b=len(str1)
        else:
            a=len(str1)
            b=len(str2)
        while b>0:
            a,b=b,a%b
        return str1[:a]        