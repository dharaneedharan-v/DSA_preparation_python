def isBalanced(root) -> bool:
    def helper(node):
        if not node: return 0
        left = helper(node.left)
        if left == -1: return -1
        right = helper(node.right)
        if right == -1: return -1
        if abs(left-right)>1: return -1
        return 1 + max(left,right)
    return helper(root) != -1
