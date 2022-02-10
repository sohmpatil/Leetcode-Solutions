# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        count = 1
        num1 = 0
        num2 = 0
        final = current = ListNode(0)
        while(l1.next != None):
            num1 = num1 + (l1.val * count)
            count = count * 10
            l1 = l1.next
        num1 = num1 + (l1.val * count)
        count = 1
        while(l2.next != None):
            num2 = num2 + (l2.val * count)
            count = count * 10
            l2 = l2.next
        num2 = num2 + (l2.val * count)
        finalnum = num1 + num2
        fstr = str(finalnum)
        if finalnum == 0:
            fList = ListNode()
            return fList
        x = len(fstr)
        while x:
            current.next = ListNode(int(fstr[x-1]))
            current = current.next
            x = x - 1
        return final.next
