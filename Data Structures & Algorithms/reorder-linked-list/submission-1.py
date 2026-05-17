# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMid(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nextptr = curr.next
            curr.next = prev
            prev = curr
            curr = nextptr
        return prev

    def merge(self, list1, list2):
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            if not temp1:
                break
            list2.next = temp1

            list1 = temp1
            list2 = temp2

    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list
        mid = self.findMid(head)
        list1 = head
        list2 = mid.next
        mid.next = None

        # Step 2: Reverse the second half
        list2 = self.reverse(list2)

        # Step 3: Merge the two halves
        self.merge(list1, list2)
        