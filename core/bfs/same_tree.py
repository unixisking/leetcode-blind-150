# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from queue import Queue

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = Queue()
        if not p and not q:
            return True
        if ((not p) ^ (not q)):
            return False
        queue.put((p, q))
        while queue.empty() == False:
            node1, node2 = queue.get()

            if node1.val != node2.val:
                return False
            if (not node1.left) ^ (not node2.left):
                return False
            if (not node1.right) ^ (not node2.right):
                return False

            if node1.left:
                queue.put((node1.left, node2.left))
            if node1.right:
                queue.put((node1.right, node2.right))

        return True

        