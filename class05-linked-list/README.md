# Linked List

**Author:** Emad Almajdalawi

**Date:** 11/03/2022

**Application Vesrsion:** 0.1.0

**Python Verstion:** 3.9.5

## Overview:

This application creates a linked list, which is a list of nodes, each node has a value and a pointer to the next node if exists. The benefit of this over ordinary list is the freedom in creation location inside the memory.

Singly linked list has three methods:

- `insert`: to add a node to the head of the linked list. The time complexity of it is O(1)

- `append`: to add a node to the end of the linked list. The time complexity of it is O(n)

- `includes`: to search for a node's value in the linked list. The time complexity of it is O(n)

- `insert_after`: to add a node after a specific node. The time complexity of it is O(n)

- `insert_before`: to add a node before a specific node. The time complexity of it is O(n)

- `insert_after`: to remove a node from the linked list. The time complexity of it is O(n)

 Doubly linked list has one method, which is `insert` to add a node to the head of the linked list. The time complexity of it is O(1)

 <br>

 This application has been created as a solution to the code challenge 5. You can test the file by running (pytest), I recommend you install (poetry) package before that.

PR: https://github.com/e97m/data-structures-and-algorithms/pull/10

- [x] Create a singly node class
- [x] Create a singly linked list class
- [x] Create insert method to the linked list class
- [x] Create includes method to the linked list class
- [x] Create to string method (__str__) to the linked list class
- [x] Handle possible errors
- [x] Create a doubly node class
- [x] Create a doubly linked list class
- [x] Create insert method to the linked list class
- [x] Create a test file
- [x] Create (insert before) method to the linked list classes
- [x] Create (insert after) method to the linked list classes
- [x] Create (delete) method to the linked list classes
- [x] Update the test file

<br>

# White Boards

## append

![append white board]()

<br>

## insret_after

![insert_after white board]()

<br>

## insret_before

![insert_before white board]()
