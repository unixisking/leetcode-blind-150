# 226. Invert Binary Tree https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            tmpLeft = root.left
            root.left = root.right
            root.right = tmpLeft
            
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


        