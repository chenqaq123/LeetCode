"""
思路：遍历链表，然后用一个指针指向要删除的节点，另一个指针指向要删除节点的前一个节点
      当遍历到链表末尾时，删除节点即可
      注意：当要删除的节点为头节点时，需要特殊处理 
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        nxt = head
        delete_node = head
        pre_delete_node = None
        while nxt is not None:
            if i > n:
                delete_node = delete_node.next
                if pre_delete_node == None:
                    pre_delete_node = head
                else:
                    pre_delete_node = pre_delete_node.next
            if nxt.next is None:
                if pre_delete_node is None:
                    if head.next is not None:
                        return head.next
                    else:
                        return None
                pre_delete_node.next = delete_node.next
                del delete_node
                break
            else: 
                nxt = nxt.next
                i += 1
        return head
