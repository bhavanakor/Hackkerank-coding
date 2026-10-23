class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        string=""
        for i in b:
            string+=str(i)
        num=int(string)
        return pow(a,num,1337)
        