# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = cursor = ListNode()
        
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    value = list1.val
                    list1 = list1.next

                else:
                    value = list2.val
                    list2 = list2.next

            elif list1 == None:
                value = list2.val
                list2 = list2.next

            elif list2 == None:
                value = list1.val
                list1 = list1.next
            
            cursor.next = ListNode(value)
            cursor = cursor.next

        return root.next
    
    
    
# 다른 사람의 풀이
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if (not l1) or (l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1
            
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
            
        return l1
