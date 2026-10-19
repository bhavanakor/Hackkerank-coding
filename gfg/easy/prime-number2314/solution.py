class Solution:
    def isPrime(self, n):
        flag=True
        if n==1:
            flag=False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                flag=False
        return flag
                