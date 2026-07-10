# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        temp=head
        n=1
        while(temp.next!=None):
            temp=temp.next
            n += 1
        k=k%n
        while k>0:
            temp=head
            while(temp.next.next!=None):
                temp=temp.next
            last = temp.next      
            temp.next = None      
            last.next = head      
            head = last           
            k-=1
        return head
            

        