from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):

        if len(s)!=len(t):
            return False
        else:
            return Counter(s)==Counter(t)
