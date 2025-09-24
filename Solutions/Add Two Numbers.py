def addTwoNumbers(l1, l2):
    carry = 0
    dummy = ListNode(0); cur = dummy
    while l1 or l2 or carry:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        s = a + b + carry
        carry = s // 10
        cur.next = ListNode(s % 10)
        cur = cur.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next
