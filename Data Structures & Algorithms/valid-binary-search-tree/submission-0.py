# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode],ans: List[int])-> List[int] :

        if root== None:
            return ans


        self.inorder(root.left,ans)
        ans.append(root.val)
        self.inorder(root.right,ans)

        return ans
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root==None:
            return False

        ans = []

        inord = self.inorder(root,ans)

        n = len(inord)

        for i in range(n-1):
            if inord[i]<inord[i+1]:
                continue
            else:
                return False
        return True



        

        