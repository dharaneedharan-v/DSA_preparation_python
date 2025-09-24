def diameterOfBinaryTree(root) -> int:
    ans = 0
    def depth(node):
        nonlocal ans
        if not node: return 0
        L = depth(node.left)
        R = depth(node.right)
        ans = max(ans, L+R)
        return 1 + max(L,R)
    depth(root)
    return ans
