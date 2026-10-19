class Solution:
    def armstrongNumber (self, n):
        length=len(str(n))
        power=0
        num=n
        while n>0:
            digit=n%10
            power+=digit**length
            n//=10
        if power==num:
            return True
        else:
            return False
            