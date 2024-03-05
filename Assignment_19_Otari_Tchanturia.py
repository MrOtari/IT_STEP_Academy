# Node class represents a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the linked list

# LinkedList class represents the linked list data structure
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list with no nodes
    
    # Method to append a new node with data to the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        # If the linked list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse the linked list to find the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Assign the new node as the next node of the last node
        last_node.next = new_node
    
    # Method to insert a new node with data at the specified index in the linked list
    def insert(self, data, index):
        new_node = Node(data)  # Create a new node with the given data

        # If index is 0, insert the new node at the beginning of the linked list
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Traverse the linked list to find the node at the specified index
        current_node = self.head
        current_index = 0
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        
        # Insert the new node at the specified index
        new_node.next = current_node.next
        current_node.next = new_node

    # Method to remove the first occurrence of a node with the given data from the linked list
    def remove(self, data):
        # If the linked list is empty, return
        if self.head is None:
            return
        
        # If the node to be removed is the head, update the head to the next node
        if self.head.data == data:
            self.head = self.head.next
            return
        
        # Traverse the linked list to find the node with the given data
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        # If the node with the given data is found, remove it from the linked list
        if current_node.next:
            current_node.next = current_node.next.next
    


    # Remove a node at the specified index in the linked list
    def remove_index(self, index):
        if index < 0:
            return
        
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        
        current_node = self.head
        previous_node = None
        current_index = 0

        while current_node and current_index < index:
            previous_node = current_node
            current_node = current_node.next
            current_index += 1
        
        if current_node:
            previous_node.next = current_node.next



    # Method to display the data stored in each node of the linked list
    def display_info(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(2)
linked_list.append(5)
linked_list.append(4)
linked_list.append(4)
linked_list.append(11)
linked_list.append(25)
linked_list.display_info()
linked_list.insert('Otari', 3)
linked_list.insert(10.1, 5)
linked_list.display_info()
linked_list.remove("Otari")
linked_list.remove(4)
linked_list.display_info()
linked_list.remove_index(2)
linked_list.display_info()
