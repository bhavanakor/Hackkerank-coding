class Solution:    
    def divisibleByDigits(self,s):
        count=0
        memo={}
        for ch in s:
            digit=int(ch)
            if digit==0:
                continue
            if digit not in memo:
                rem=0
                for c in s:
                    rem=(rem*10+int(c))%digit
                memo[digit]=(rem==0)
            if memo[digit]:
                count+=1
        return count
                