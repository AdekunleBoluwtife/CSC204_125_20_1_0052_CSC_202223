from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def delete(self, key):
        current = self.head
        prev = None

        while current and current.data != key:
            prev = current
            current = current.next_node

        if current is None:
            print(f"{key} not found in the linked list.")
            return

        if prev is None:
            self.head = current.next_node
        else:
            prev.next_node = current.next_node

        print(f"{key} deleted from the linked list.")

    def traversal(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_node

    def display(self):
        elements = [str(data) for data in self.traversal()]
        print(" -> ".join(elements) + " -> None")
