from linked import SinglyLinkedList

if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    sll = SinglyLinkedList()

    for data in data_list:
        sll.insert(data)

    print("Linked List:")
    sll.display()
