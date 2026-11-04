# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        count = 0
        temp = head
        while(temp!=None):
            temp = temp.next
            count +=1
        temp = head
        if(count == n):
            return temp.next
        for i in range(count - n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head
        


        
            
        