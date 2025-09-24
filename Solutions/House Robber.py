def rob(nums: list[int]) -> int:
    if not nums: return 0
    prev, curr = 0, 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr
