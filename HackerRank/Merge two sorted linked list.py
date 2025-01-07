import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the mergeLists function below.


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    merged = []

    curr_h1 = head1
    while curr_h1 != None:
        merged.append(curr_h1.data)
        curr_h1 = curr_h1.next

    curr_h2 = head2
    while curr_h2 != None:
        merged.append(curr_h2.data)
        curr_h2 = curr_h2.next

    merged.sort()
    result = SinglyLinkedList()

    for i in merged:
        result.insert_node(i)

    return result.head


# list1 = [1, 2, 3]
# llist1 = SinglyLinkedList()
# for i in list1:
#     llist1.insert_node(i)

# llist2 = SinglyLinkedList()
# list2 = [3, 4]
# for i in list2:
#     llist2.insert_node(i)

# print(mergeLists(llist1.head, llist2.head))

list1 = [4, 5, 6]
llist1 = SinglyLinkedList()
for i in list1:
    llist1.insert_node(i)

list2 = [1, 2, 10]
llist2 = SinglyLinkedList()
for i in list2:
    llist2.insert_node(i)

print(mergeLists(llist1.head, llist2.head))
