# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if root is None:
            return out
        self.helper(root, out)
        return out
    
    def helper(self, root, out):
        if root is None:
            return
        self.helper(root.left, out)
        out.append(root.val)
        self.helper(root.right, out)