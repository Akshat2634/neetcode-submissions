# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode])->bool:
        if root==None and subRoot==None:
            return True

        if subRoot==None and root!=None:
            return False

        if root==None and subRoot!= None:
            return False
        
        left = self.sameTree(root.left,subRoot.left)
        right = self.sameTree(root.right,subRoot.right)
        val = root.val == subRoot.val
        
        if left and right and val:
            return True

        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root== None and subRoot==None:
            return True
        
        if root== None and subRoot!=None:
            return False
        
        if subRoot==None and root!=None:
            return True

        if self.sameTree(root,subRoot):
            return True
        

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        