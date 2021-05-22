# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                leftTreeHead = curr.left
                while leftTreeHead.right:
                    leftTreeHead = leftTreeHead.right
                leftTreeHead.right = curr.right
                leftTree = curr.left
                curr.left = None
                curr.right = leftTree
            print(curr.val)
            curr = curr.right
        return root