# 100. Same Tree https://leetcode.com/problems/same-tree/description/?envType=problem-list-v2&envId=breadth-first-search

from typing import Optional
from queue import Queue

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = Queue(), Queue()
        if not p and not q:
            return True
        if ((not p) ^ (not q)):
            return False
        q1.put(p)
        q2.put(q)
        while q1.empty() == False and q2.empty() == False:
            node1 = q1.get()
            node2 = q2.get()

            if node1.val != node2.val:
                return False
            if (not node1.left) ^ (not node2.left):
                return False
            if (not node1.right) ^ (not node2.right):
                return False

            if node1.left:
                q1.put(node1.left)
                q2.put(node2.left)
            if node1.right:
                q1.put(node1.right)
                q2.put(node2.right)

        return True