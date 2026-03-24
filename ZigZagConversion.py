class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows 
        flag = 1 
        row = 0

        for char in s:
            rows[row] += char

            if row == 0:
                flag = 1
            elif row == numRows - 1:
                flag = -1

            row += flag

        return ''.join(rows)