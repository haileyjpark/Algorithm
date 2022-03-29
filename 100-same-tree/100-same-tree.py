# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
                return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    
# 다른 사람의 풀이
from collections import deque

class Solution2:
    def isSameNode(self, p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return True
    
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        dq = deque([(p, q)])
        
        while dq:
            p,q = dq.popleft()
            
            if not self.isSameNode(p,q):
                return False
            
            if p:
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))
            
        return True
