# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev(self, head: Optional[ListNode]):
        prev = None
        curr = head

        while(curr!=None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    def findMid(self, head: Optional[ListNode]):
        slow = head
        fast = head

        while(fast!=None and fast.next!=None):
            fast= fast.next.next
            slow = slow.next

        return slow
    
    def merge(self,list1,list2):
        if list1==None:
            return list2
        if list2 == None:
            return list1
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1= temp1
            list2 = temp2



    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None:
            return 

        list1 = head
        mid = self.findMid(head)
        list2 = mid.next
        list2 = self.rev(list2)
        mid.next = None

        self.merge(list1,list2)
        
        