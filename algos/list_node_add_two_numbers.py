from typing import Optional
from helpers.listNodeHelpers import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #build a single number from the given node values
        def buildNumberFromListNode(head):
            values = ''
            while head.next != None:
                values = str(head.val) + values
                head = head.next
            values = str(head.val) + values
            return int(values)

        num1 = buildNumberFromListNode(l1)
        num2 = buildNumberFromListNode(l2)
        print("got numbers:",num1,num2)

        total = [int(i) for i in str(num1 + num2)]
        print("got total:", total)

        output = ListNode(total[0])
        for i in total[1:]:
          output = ListNode(val=i,next=output)

        return output
