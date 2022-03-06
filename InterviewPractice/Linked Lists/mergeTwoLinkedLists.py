# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l1, l2):
    if l1 == None and l2 == None:
        return None

    head = ListNode(0)
    l3 = head

    while l1 != None and l2 != None:
        if l1.value < l2.value:
            l3.value = l1.value
            l1 = l1.next
        else:
            l3.value = l2.value
            l2 = l2.next

        l3.next = ListNode(0)
        l3 = l3.next
    while l1 != None:
        l3.value = l1.value
        l1 = l1.next
        if l1 != None:
            l3.next = ListNode(0)
            l3 = l3.next

    while l2 != None:
        l3.value = l2.value
        l2 = l2.next
        if l2 != None:
            l3.next = ListNode(0)
            l3 = l3.next
    return head
