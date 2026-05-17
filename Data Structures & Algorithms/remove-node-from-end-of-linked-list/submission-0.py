# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def size(self,head):
        if head==None:
            return 0
        temp = head
        length = 0
        while(temp!=None):
            temp=temp.next
            length+=1
        return length
            

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head==None:
            return 
        

        sz = self.size(head)

        toRem = sz-n

        if toRem==0:
            return head.next
            
        temp = head

        for i in range(toRem-1):
            temp = temp.next
        
        temp.next= temp.next.next

        return head