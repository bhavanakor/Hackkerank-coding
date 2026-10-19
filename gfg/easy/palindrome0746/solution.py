class Solution:
    def isPalindrome(self, n):
		rev=str(abs(n))[::-1]
		if rev==str(abs(n)):
		    return True
		else:
		    return False