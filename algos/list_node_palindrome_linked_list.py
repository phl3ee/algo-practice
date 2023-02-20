def isPalindrome(self, head) -> bool:

    list = []

    #build list until no next=None
    while head.next != None:
        list.append(head.val)
        head = head.next
    list.append(head.val)
    #print(list)

    #if list is of one, return true
    if len(list) == 1:
        return True

    #split list, reverse second set and compare
    #we have to update slice size if list is odd length
    if (len(list) % 2) != 0:
        increment = 1
    else:
        increment = 0
    leftList = list[:len(list)//2 + increment]
    rightList = list[len(list)//2:]
    rightList.reverse()
    if(leftList == rightList):
        return True
    else:
        return False