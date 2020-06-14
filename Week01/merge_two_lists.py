class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        递归法
        """
        if l1 and l2:
            l1, l2 = (l2, l1) if l1.val > l2.val else (l1, l2)
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     """
    #     迭代法
    #     """
    #     head = ListNode(val=-1)
    #     tail = head
    #     while l1 and l2:
    #         l1, l2 = (l2, l1) if l1.val > l2.val else (l1, l2)
    #         tail.next, tail = l1, l1
    #         l1 = l1.next
    #     tail.next = l1 or l2
    #     return head.next