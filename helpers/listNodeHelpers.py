class ListNode:
    """Various helper functions for leetcode ListNode challenges
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def buildListNodeFromList(self, listIn):
      #convert a list into a ListNode arrray
        listIn.reverse()
        output = ListNode(listIn[0])
        for i in listIn[1:]:
          output = ListNode(val=i,next=output)
        #print("what's the nice way?", output.val, output.next.val, output.next.next.val)
        return output

    def buildListFromListNode(self, head):
      #build a simple list of the given values
        values = []
        while head.next != None:
            values.append(head.val)
            head = head.next
        values.append(head.val)
        return values

    def buildNumberFromListNode(self, head):
        values = ''
        while head.next != None:
            values = str(head.val) + values
            head = head.next
        values = str(head.val) + values
        return int(values)