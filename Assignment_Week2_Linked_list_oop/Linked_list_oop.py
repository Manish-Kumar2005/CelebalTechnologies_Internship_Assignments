# Name: Manish Kumar
# Task Week2: Implement Singly Linked List using OOP with exception handling.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise IndexError("List is empty. Cannot delete.")

            if n <= 0:
                raise ValueError("Invalid index. Must be 1 or higher.")

            if n == 1:
                deleted = self.head.data
                self.head = self.head.next
                print(f"Deleted node at position {n}: {deleted}")
                return

            current = self.head
            for _ in range(n - 2):
                if current.next is None:
                    raise IndexError("Index out of range.")
                current = current.next

            if current.next is None:
                raise IndexError("Index out of range.")

            deleted = current.next.data
            current.next = current.next.next
            print(f"Deleted node at position {n}: {deleted}")

        except (IndexError, ValueError) as e:
            print(e)

# Sample Test Code

if __name__ == "__main__":
    ll = LinkedList()

    # Add sample nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Original Linked List:")
    ll.print_list()

    ll.delete_nth_node(2)

    print("Linked List after deleting 2nd node:")
    ll.print_list()

    ll.delete_nth_node(10)  # out of range

    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    ll.delete_nth_node(1)  # list is empty
