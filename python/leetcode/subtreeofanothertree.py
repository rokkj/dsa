# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(p, q):
            # Both are Null
            if p is None and q is None:
                return True

            # One is Null
            if (p is None and q is not None) or (q is None and p is not None):
                return False
        
            # Compare values
            if p.val != q.val:
                return False

            return same(p.left, q.left) and same(p.right, q.right)

        def has_subtree(root):
            if root is None:
                return False

            if same(root, subRoot):
                return True

            return has_subtree(root.left) or has_subtree(root.right)
        return has_subtree(root)