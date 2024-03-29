# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum(self,root,val):
        if root is None:
            return 0
        val=(val*10+root.val)
        if root.left is None and root.right is None:
            return val
        return (self.sum(root.left,val)+self.sum(root.right,val))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum(root,0)

        
        