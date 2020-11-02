# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = {0}
        node = head

        while node is not None:
            if node in visited:
                return True
            else:
                visited.add(node)

            node = node.next

        return False