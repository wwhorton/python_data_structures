from node import Node


class Queue:
    def __init__(self, values):
        self.head = None
        self.tail = None
        for value in values:
            self.enqueue(value)

    def enqueue(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            cursor = self.head
            while cursor.next_node:
                cursor = cursor.next_node
            cursor.next_node = self.tail = Node(value)
        print(value)

    def dequeue(self):
        print(self.head)
        self.head = self.head.next_node

    def peek(self):
        print(self.head)
