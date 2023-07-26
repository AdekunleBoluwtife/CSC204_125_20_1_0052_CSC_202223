class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, data):
        self.linked_list.append(data)

    def dequeue(self):
        if not self.is_empty():
            data = self.linked_list.head.data
            self.linked_list.head = self.linked_list.head.next
            return data
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return self.linked_list.head is None

    def display(self):
        return self.linked_list.display()


def sort_queue(queue):
    temp_list = []

    # Dequeue all elements into a list
    while not queue.is_empty():
        temp_list.append(queue.dequeue())

    # Sort the list
    temp_list.sort()

    # Enqueue the sorted elements back into the queue
    for item in temp_list:
        queue.enqueue(item)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(5)
    queue.enqueue(2)
    queue.enqueue(8)
    queue.enqueue(3)

    print("Original Queue:", queue.display())  # Output: [5, 2, 8, 3]

    queue.dequeue()
    print("Queue after dequeue:", queue.display())  # Output: [2, 8, 3]

    sort_queue(queue)
    print("Sorted Queue:", queue.display())  # Output: [2, 3, 8]
