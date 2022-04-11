# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            rightSide = None
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val) 
        return res

    
    def gettingSideSideView(self, root: TreeNode) -> List[int]:
#         O(n)
        def rightSideView(root, depth=0, res=[]):
            if root is not None:
                if depth == len(res):
                    res.append(root.val)
                rightSideView(root.right, depth+1, res)
                rightSideView(root.left, depth+1, res)
                
        return rightSideView(root)
        
        
