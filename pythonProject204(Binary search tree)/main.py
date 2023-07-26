from linked import SinglyLinkedList

if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    # to reate a new linked list and insert data_list elements
    sll = SinglyLinkedList()
    for data in data_list:
        sll.insert(data)

    # to display the maximum and minimum data in the linked list
    max_data, min_data = sll.find_max_min()
    print(f"Maximum data: {max_data}")
    print(f"Minimum data: {min_data}")

    # to convert the linked list into a binary search tree
    bst_data_list = sorted(data_list)  # Sorting the list to create a valid binary search tree
    sll.convert_to_bst(bst_data_list)

    print("Linked List after converting to BST:")
    sll.display()
