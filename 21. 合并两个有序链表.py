"""
思路：用两个指针分别指向两个链表的待添加节点，然后比较大小添加到新链表尾节点即可。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def append_node(self, list_head, list_tail, val):
        new_node = ListNode(val=val, next=None)
        if list_tail is None:
            list_tail = new_node
            list_head = list_tail
        else:
            list_tail.next = new_node
            list_tail = new_node

        return list_head, list_tail

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        new_list_head = None
        new_list_tail = None
        while node1 is not None and node2 is not None:
            append_val = node1.val
            if node2.val < append_val:
                append_val = node2.val
                node2 = node2.next
            else:
                node1 = node1.next
            new_list_head, new_list_tail = self.append_node(new_list_head,new_list_tail, append_val)
        while node1 is not None:
            new_list_head, new_list_tail = self.append_node(new_list_head, new_list_tail, node1.val)
            node1 = node1.next
        while node2 is not None:
            new_list_head, new_list_tail = self.append_node(new_list_head, new_list_tail, node2.val)
            node2 = node2.next

        return new_list_head