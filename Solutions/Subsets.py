def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    n = len(nums)
    def backtrack(i, path):
        if i==n:
            res.append(path.copy()); return
        # exclude
        backtrack(i+1, path)
        # include
        path.append(nums[i])
        backtrack(i+1, path)
        path.pop()
    backtrack(0, [])
    return res
