# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    arr = list()

    while l != None:
        arr.append(l.value)
        l = l.next

    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            return False

    return True
