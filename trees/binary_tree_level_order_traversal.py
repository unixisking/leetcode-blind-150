# 102. Binary Tree Level Order Traversal https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List, Dict
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node: Optional[TreeNode], level: int, output: Dict[int, List[int]]) -> List[List[int]]:
            if not node:
                return output
            output[level].append(node.val)
            output = traverse(node.left, level + 1, output)
            return traverse(node.right, level + 1, output)
            

        result = traverse(root, 0, defaultdict(list))
        return [nodes for nodes in result.values()]



        