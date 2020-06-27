class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

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
        # create a previous node and set value to None
        previous_node = None
        # create a variable to store the current node
        # set it to the current head
        current_node = self.head
        # create a while loop that runs while the list
        # is not empty or the value of None
        while current_node is not None:
            # set the next node to the currents next 
            # which is technically the head's next node
            next_node = current_node.next_node
            # reset the value of the current next node to
            # the previous node
            current_node.next_node = previous_node
            # the previous node becomes the next node 
            previous_node = current_node
            # the current node then becomes the next node
            current_node = next_node
        # the new head becomes the previous node
        # thus reversing the order of the linked list
        self.head = previous_node
