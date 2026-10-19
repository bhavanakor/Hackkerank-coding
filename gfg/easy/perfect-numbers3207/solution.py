class Solution:
    def isPerfect(self, n):
        total=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                total+=i
                if i!=n//i and n//i!=n:
                    total+=n//i
        if total==n:
            return True
        else:
            return False
            
        