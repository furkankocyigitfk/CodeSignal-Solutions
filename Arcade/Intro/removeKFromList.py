# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    temp = l
    prev = None

    while temp != None and temp.value == k:
        l = l.next
        temp = l

    while temp != None:
        while temp != None and temp.value != k:
            prev = temp
            temp = temp.next

        if temp == None:
            return l

        prev.next = temp.next
        temp = temp.next

    return l
