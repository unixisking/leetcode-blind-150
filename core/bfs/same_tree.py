# 100. Same Tree https://leetcode.com/problems/same-tree/description/?envType=problem-list-v2&envId=breadth-first-search

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return False

        