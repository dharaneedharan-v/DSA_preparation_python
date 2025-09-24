class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node
        # double linked list
        class Node:
            __slots__ = ('k','v','prev','next')
            def __init__(self,k,v):
                self.k=k; self.v=v; self.prev=None; self.next=None
        self.Node = Node
        self.head = Node(0,0); self.tail = Node(0,0)
        self.head.next = self.tail; self.tail.prev = self.head
    def _remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    def _add(self, node):
        # add right after head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.v
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.v = value
            self._remove(node)
            self._add(node)
        else:
            node = self.Node(key,value)
            self.cache[key] = node
            self._add(node)
            if len(self.cache) > self.cap:
                # remove tail.prev
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.k]
