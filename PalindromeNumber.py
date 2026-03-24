class Solution(object):
    def isPalindrome(self, x):
        b=str(x)
        if b[::-1]==b:
            return True
        else:
            return False