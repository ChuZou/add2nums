# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0) #set up a new link list
        cur = ret #set this new linklist as cur
        add = 0 #this var. represent carry
        
        while l1 or l2 or add:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add #add coresponding value
            add = val / 10 #calculate carry
            cur.next = ListNode(val % 10) #keep the remainder as the value of corresponding location
            cur = cur.next # ???
            l1 = l1.next if l1 else None #keep going
            l2 = l2.next if l2 else None #keep going
        
        return ret.next^ #???
