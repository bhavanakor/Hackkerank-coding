class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            acc=0
            while n>0:
                digit=n%10
                acc+=digit**2
                n//=10
            n=acc
        return n==1
