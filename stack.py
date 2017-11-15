from node import Node


class Stack:
    def __init__(self, values=None):
        self.top = None

        for value in values:
            self.push(value)

    def push(self, value):
        next_node = None

        if self.top:
            next_node = self.top

        self.top = Node(value, next_node)

    def pop(self):
        print(self.top)
        print("----------")
        self.top = self.top.next_node

    def peek(self):
        print(self.top)
        print("----------")

    def print_stack(self):
        current = self.top
        while current.next_node:
            print(current)
            current = current.next_node

        print("----------")
