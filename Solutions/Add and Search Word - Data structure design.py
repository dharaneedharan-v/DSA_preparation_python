class WordDictionary:
    def __init__(self):
        self.root = {}
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i==len(word):
                return '$' in node
            ch = word[i]
            if ch=='.':
                for k in node:
                    if k != '$' and dfs(node[k], i+1):
                        return True
                return False
            else:
                if ch not in node: return False
                return dfs(node[ch], i+1)
        return dfs(self.root, 0)
