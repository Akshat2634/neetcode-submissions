# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self,root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root ==None and subRoot is not None:
            return False
        if root == None and subRoot == None:
            return True
        
        if root !=None and subRoot==None:
            return False

        left = self.isSameTree(root.left,subRoot.left)
        right  =  self.isSameTree(root.right,subRoot.right)

        val = root.val == subRoot.val

        if left and right and val:
            return True

        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot is None:
            return False

        if subRoot== None and root is not None:
            return True

        if subRoot is not None and root==None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



        
        