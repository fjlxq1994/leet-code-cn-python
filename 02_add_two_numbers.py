# https://leetcode-cn.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = 0
        answer = None
        tail = None
        pointer1 = l1
        pointer2 = l2
        while pointer1 is not None or pointer2 is not None:
            node = ListNode()
            num1 = 0
            num2 = 0
            if pointer1 is not None:
                num1 = pointer1.val
            if pointer2 is not None:
                num2 = pointer2.val
            total = num1 + num2 + left
            node.val = total % 10
            left = total // 10
            if answer is None:
                answer = node
            else:
                tail.next = node
            tail = node
            if pointer1 is not None:
                pointer1 = pointer1.next
            else:
                pointer1 = None
            if pointer2 is not None:
                pointer2 = pointer2.next
            else:
                pointer2 = None
        if left > 0:
            node = ListNode()
            node.val = left
            tail.next = node
        return answer
