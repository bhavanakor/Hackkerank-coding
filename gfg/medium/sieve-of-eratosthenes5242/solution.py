class Solution:
    def isprime(self,n):
        
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
            
    def sieve(self, n):
        res=[]
        for i in range(2,n+1):
            if self.isprime(i):
                res.append(i)
        return res
            
        