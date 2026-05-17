# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode], ans: List[int])-> List[int]:
        if root==None:
            return ans

        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)

        return ans

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root==None:
            return 
        
        ans = []

        inord = self.inorder(root,ans)

        return inord[k-1]
        