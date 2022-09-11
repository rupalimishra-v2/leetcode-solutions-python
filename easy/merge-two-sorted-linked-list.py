# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        temp = self.next
        while (temp):
            print(temp.val)
            temp = temp.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or list2 and list1.val > list2.val:
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


if __name__ == "__main__":

    list1 = ListNode(1)
    second1 = ListNode(2)
    third1 = ListNode(4)
    list1.next = second1
    second1.next = third1

    list2 = ListNode(1)
    second2 = ListNode(3)
    third2 = ListNode(4)
    list2.next = second2
    second2.next = third2

    Solution().mergeTwoLists(list1, list2).printList()
