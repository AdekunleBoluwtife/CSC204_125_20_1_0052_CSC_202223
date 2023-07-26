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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next_node
        print("None")

    def find_max_min(self):
        if not self.head:
            print("The linked list is empty.")
            return None, None

        current = self.head
        max_data = current.data
        min_data = current.data

        while current:
            if current.data > max_data:
                max_data = current.data
            if current.data < min_data:
                min_data = current.data
            current = current.next_node

        return max_data, min_data

    def convert_to_bst(self, data_list):
        self.head = self._convert_to_bst_helper(data_list, 0, len(data_list) - 1)

    def _convert_to_bst_helper(self, data_list, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        left_child = self._convert_to_bst_helper(data_list, start, mid - 1)

        new_node = Node(data_list[mid])
        new_node.next_node = left_child

        new_node.next_node = self._convert_to_bst_helper(data_list, mid + 1, end)

        return new_node
