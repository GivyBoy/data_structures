"""
 Implementation of a Singly Linked List
 """


class Node:

    def __init__(self, data):  # constructor
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):  # constructor
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        # ^ set to the first element of the LL and will be used to traverse all elements, hence why insertions are O(n)

        # used to traverse the entire LL until 'last_node.next returns None and is therefore False. When it is False,
        # it indicates that we are currently at the last element in the LL, and it is now time to add the new element
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def len_iterative(self):

        count = 0

        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def len_recursive(self, node):

        if node is None:
            return 0

        return 1 + self.len_recursive(node)

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None

        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):

        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0

            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def print_ll(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def __str__(self) -> str:
        nodes = []
        cur_node = self.head
        while cur_node:
            nodes.append(str(cur_node.data))
            cur_node = cur_node.next

        return ' -> '.join(nodes)


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(2)
    ll.append(3)

    ll.prepend(7)
    ll.insert_after_node(ll.head.next, 8)

    print(ll)

