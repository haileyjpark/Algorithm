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
