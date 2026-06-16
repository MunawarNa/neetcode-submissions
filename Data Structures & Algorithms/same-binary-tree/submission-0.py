# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, output):

            if not node:
                output.append("null")
                return
            output.append(node.val)

            dfs(node.left, output)
            dfs(node.right, output)
            
        p_list = []
        q_list = []
        dfs(p, p_list)
        dfs(q, q_list)

        return p_list == q_list
            


        