from typing import Optional
from helpers.listNodeHelpers import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        parsedList = []

        def listFromListNode(head):
            #convert a ListNode into a list
            outList = []
            while head.next != None:
                outList.append(head.val)
                head = head.next
            outList.append(head.val)
            return outList

        def buildListNodeFromList(listIn):
            #convert a list into a ListNode array
            if not listIn:
                return ListNode('')
            listIn.reverse()
            output = ListNode(listIn[0])
            for i in listIn[1:]:
               output = ListNode(val=i,next=output)
            return output

        #no-ops input validation
        if not list1 and not list2:
            return buildListNodeFromList(parsedList)
        elif list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2

        parsedList = listFromListNode(list1)
        parsedList += listFromListNode(list2)
        parsedList.sort()

        return buildListNodeFromList(parsedList)

