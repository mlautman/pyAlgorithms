

class DLLNode():
    data = None
    next_node = None
    prev_node = None

    def __init__(self, data):
        self.data = data


class DLL(object):
    head = None
    tail = None

    def __init__(self):
        pass

    def append(self, data):
        newNode = DLLNode(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.prev_node = self.tail
            self.tail.next_node = newNode
            self.tail = newNode

    def prepend(self, data):
        newNode = DLLNode(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next_node = self.head
            self.head.prev_node = newNode
            self.head = newNode


    def add_after(self, node, data):
        newNode = DLLNode(data)

        if node.next_node is None:
            node.next_node = newNode
            newNode.prev_node = node
            self.tail = newNode

        else:
            newNode.next_node = node.next_node
            newNode.prev_node = node

            node.next_node.prev_node = newNode
            node.next_node = newNode


    def search(self, data):
        currNode = self.head
        while not currNode is None:
            if currNode.data == data:
                return currNode
            else:
                currNode = currNode.next_node

    def remove(self, node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None

        elif node == self.head:
            node.next_node.prev_node = None
            self.head = node.next_node

        elif node == self.tail:
            node.prev_node.next_node = None
            self.tail = node.prev_node

        else:
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
