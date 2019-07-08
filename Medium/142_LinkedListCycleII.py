# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        cur = head
        i = 0
        cur.val = str(i)

        while cur.next is not None:
            i += 1
            cur = cur.next

            if type(cur.val) == str:
                return cur

            cur.val = str(i)

        return None
