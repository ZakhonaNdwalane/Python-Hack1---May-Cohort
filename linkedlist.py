class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        """Find the maximum element in the linked list."""
        if self.head is None:
            raise ValueError("The linked list is empty.")
        
        max_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Test the LinkedList class
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(30)
linked_list.append(20)
linked_list.append(50)
linked_list.append(40)

print("Maximum element in the linked list:", linked_list.find_max())  # Output: 50
