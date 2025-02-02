# 35. Search Insert Position https://leetcode.com/problems/search-insert-position/?envType=problem-list-v2&envId=binary-search

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)

        while(nums[mid] != target and left <= right):
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            mid = int((left + right) / 2)

        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return mid - 1 if mid - 1 > 0 else 0 
        return mid + 1
           