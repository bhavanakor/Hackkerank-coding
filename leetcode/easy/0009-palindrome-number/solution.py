class Solution:
    def isPalindrome(self, x: int) -> bool:
        org=x
        reverse=0
        while x>0:
            digit=x%10
            reverse=(reverse*10)+digit
            x//=10
        if org==reverse:
            return True
        else:
            return False



        