class Solution:
    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        if a<b:
            l=b
            s=a
        else:
            l=a
            s=b
        while s>0:
            l,s=s,l%s
        gcd=l
        
        lcm=(a*b)//gcd
        
        return [lcm,gcd]
            