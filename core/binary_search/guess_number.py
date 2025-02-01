# 374. Guess Number Higher or Lower : https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=problem-list-v2&envId=binary-search
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

def guess(num: int) -> int:
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = int((left + right) / 2)

        g = guess(mid)
        while(g != 0 and left <= right):
            if g == -1:
                right = mid - 1
            elif g == 1:
                left = mid + 1
            mid = int((left + right) / 2)
            g = guess(mid)
        return mid if g == 0 else -1