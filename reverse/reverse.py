from copy import copy


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return
        
        else:
            # if there is no next node
            if node.next is None:
                # current node = head
                self.head = node
                # next node the previous
                node.next = prev
                return

            # assigning new_node to next node
            new_node = node.next
            # changing the next pointer to previous
            node.next = prev
            # calls function again with recursive on the node
            # passing in new_node and node
            self.reverse_list(new_node, node)