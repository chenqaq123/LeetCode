# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        46ms
        81.21%
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        working_node = None

        # 进位标志
        carry = 0
        sum = 0
        while l1 is not None or l2 is not None or carry is not 0:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            sum = sum % 10

            if result is None:
                result = ListNode(sum)
                working_node = result
            else:
                working_node.next = ListNode(sum)
                working_node = working_node.next

        return result
    

if __name__ == '__main__':
    l1 = ListNode(9, ListNode(9, ListNode(1)))
    l2 = ListNode(1)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result is not None:
        print(result.val)
        result = result.next





