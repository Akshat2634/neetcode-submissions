# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p==None and q is not None:
            return False

        if q==None and p is not None:
            return False
        
        if p is None and q is None:
            return True

        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
        val = p.val==q.val

        if left and right and val:
            return True

        return False        
        