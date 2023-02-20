# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #build a simple list of the given values
        values = []
        while head.next != None:
            values.append(head.val)
            head = head.next
        values.append(head.val)

        #split the values list to return second half,
        #then reverse it to build a linked list
        flipList = values[len(values)//2:]
        flipList.reverse()

        #initialise ListNode output with first result value (next defaults to None)
        #then iterate remaining values to build linked list
        output = ListNode(flipList[0])
        for i in flipList[1:]:
          output = ListNode(val=i,next=output)

        return output