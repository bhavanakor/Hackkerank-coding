class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            elif s[left]!=s[right]:
                option_a= s[left+1:right+1]
                option_b= s[left:right]
                if option_a == option_a[::-1] or option_b == option_b[::-1]:
                    return True
                else:
                    return False
        return True