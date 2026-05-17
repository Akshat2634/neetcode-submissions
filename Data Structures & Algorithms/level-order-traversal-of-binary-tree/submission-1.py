# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root ==None:
            return []

        q = deque()
        res = []

        q.append(root)

        while q:
            level = len(q)
            ans = []

            for i in range(level):
                front = q[0]
                q.popleft()
                ans.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            res.append(ans)

        return res

        