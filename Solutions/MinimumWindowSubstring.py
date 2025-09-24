# 14. MinimumWindowSubstring.py
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if end == 0 or right-left < end-start:
                    start, end = left, right
        return s[start:end]
