# Linked List

Date: 11/03/2022

Application Vesrsion: 0.1.0

Python Verstion: 3.9.5

Overview:

This application creates a linked list, which is a list of nodes, each node has a value and a pointer to the next node if exists. The benefit of this over ordinary list is the freedom in creation location inside the memory.

Singly linked list has three methods:

 - `insert`: to add a node to the head of the linked list. The time complexity of it is O(1)

 - `append`: to add a node to the end of the linked list. The time complexity of it is O(n)

 - `includes`: to search for a node's value in the linked list. The time complexity of it is O(n)

 Doubly linked list has one method, which is `insert` to add a node to the head of the linked list. The time complexity of it is O(1)

 <br>

 This application has been created as a solution to the code challenge 5. You can test the file by running (pytest), I recommend you install (poetry) package before that.

singly linked list: https://github.com/e97m/data-structures-and-algorithms/pull/6

doubly linked list: https://github.com/e97m/data-structures-and-algorithms/pull/7

- [x] Creat a singly node class
- [x] Creat a singly linked list class
- [x] Creat insert method to the linked list class
- [x] Creat includes method to the linked list class
- [x] Creat to string method (__str__) to the linked list class
- [x] Handle possible errors
- [x] Creat a doubly node class
- [x] Creat a doubly linked list class
- [x] Creat insert method to the linked list class
- [x] Creat a test file