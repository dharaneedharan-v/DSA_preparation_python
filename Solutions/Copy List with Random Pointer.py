def copyRandomList(head):
    if not head: return None
    # Step1: interleave copied nodes
    cur = head
    while cur:
        nxt = cur.next
        copy = Node(cur.val)
        cur.next = copy
        copy.next = nxt
        cur = nxt
    # Step2: assign randoms
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    # Step3: separate lists
    cur = head
    new_head = head.next
    while cur:
        copy = cur.next
        cur.next = copy.next
        cur = cur.next
        if copy.next:
            copy.next = copy.next.next
    return new_head
