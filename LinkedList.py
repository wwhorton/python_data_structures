from node import Node


class LinkedList:
    def __init__(self, values):
        self.count = 0
        self.head = None
        self.tail = None
        for value in values:
            self.add_last(value)

    def add_first(self, value):
        old_head = None

        if self.head:
            old_head = value.head

        self.head = Node(value, old_head)
        self.count = self.count + 1

        if self.count == 1:
            self.tail = self.head

    def add_last(self, value):
        node = Node(value)

        if self.count == 0:
            self.head = node
        else:
            self.tail.next_node = node

        self.tail = node
        self.count = self.count + 1

    def remove_first(self):
        if self.head:
            self.head = self.head.next_node
            self.count = self.count - 1

    def remove_last(self):
        second_to_last = None
        current = self.head

        while current.next_node:
            second_to_last = current
            current = current.next_node

        self.tail = second_to_last
        self.tail.next_node = None
        self.count = self.count - 1

    def print_list(self):
        node = self.head

        while node.next_node:
            print(node)
            node = node.next_node

        if self.tail != self.head:
            print(self.tail)

        print("----------------------------")
