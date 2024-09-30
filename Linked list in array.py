class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListArray:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return "[" + ", ".join(elements) + "]"

# Example usage:
arr = LinkedListArray()
arr.add(10)
arr.add(20)
arr.add(30)
print(arr)  # Output: [10, 20, 30]
print(arr.get(1))  # Output: 20
