# Node , LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def append(self, new_data):
        node = Node(new_data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def prepend(self, new_data):
        node = Node(new_data)

        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def middle_add(self, prev_node: Node, new_data: str):
        if prev_node is None:
            print("The previous node is None")
            return
        node = Node(new_data)
        node.next = prev_node.next
        prev_node.next = node

    def delete(self):
        pass



node1 = Node('Monday')
node2 = Node('Tuesday')
node3 = Node('Wednesday')

llist = LinkedList()

llist.head = node1
node1.next = node2
node2.next = node3
llist.append('Thursday')
llist.prepend('Sunday')
prev_node = llist.head.next.next.next  # Payshanba
llist.middle_add(llist.head.next, 'asdasdasd')
llist.display()

# print(node2.next.data)
