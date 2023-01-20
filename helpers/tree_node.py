"""
TreeNode Implementation notes
https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-
"""
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelorder(self, root):
        output = []
        Q = Queue()
        Q.put(root)
        while (not Q.empty()):
            node = Q.get()
            if node == None:
                continue
            #print(node.val)
            output.append(node.val)
            Q.put(node.left)
            Q.put(node.right)
        return output
