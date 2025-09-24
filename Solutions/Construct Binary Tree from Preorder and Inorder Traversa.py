def buildTree(preorder: list[int], inorder: list[int]):
    if not preorder: return None
    idx_map = {val:i for i,val in enumerate(inorder)}
    def helper(p_lo, p_hi, i_lo, i_hi):
        if p_lo>p_hi: return None
        root_val = preorder[p_lo]
        root = TreeNode(root_val)
        mid = idx_map[root_val]
        left_size = mid - i_lo
        root.left = helper(p_lo+1, p_lo+left_size, i_lo, mid-1)
        root.right = helper(p_lo+left_size+1, p_hi, mid+1, i_hi)
        return root
    return helper(0, len(preorder)-1, 0, len(inorder)-1)
