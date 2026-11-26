class Solution(object):
    def canAliceWin(self, n):
        i = 0
        while n > 0:
            n -= (10 - i)

            if n < 0:
                return i % 2 != 0
            elif n == 0:
                return i % 2 == 0

            i += 1