# DoublyLinkedList created on my own


class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def get_next(self):
        return self.next_node

    def set_next(self, next):
        self.next_node = next

    def get_prev(self):
        return self.prev_node

    def set_prev(self):
        self.prev_node = prev

    def get_value(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def to_string(self, value):
        return "Node value:" + str(self.value)

    def has_next(self):
        if self.get_next() is None:
            return True


class DoublyLinkedList(object):
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, value):
        if self.size == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value, self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        self.size += 1

    def reomove(self, value):
        this_node = self.head
        while this_node is not None:
            if this_node.get_data() == value:
                if this_node.get_prev() is not None:
                    if this_node.has_next():
                        this_node.get_prev().set_next(this_node.get_next())
                        this_node.get_next().set_prev(this_node.get_prev())
                    else:
                        this_node.get_prev().set_next(None)
                        self.tail = this_node.get_prev()
                else:
                    self.head = this_node.get_next()
                    this_node.get_next().set_prev(self.head)
                self.size -= 1
                return True
            else:
                this_node = this_node.get_next()
        return False

    def find(self, value):
        this_node = self.head
        while this_node is not None:
            if this_node.get_data() == value:
                return value
            elif this_node.get_next() == self.head:
                return False
            else:
                this_node = this_node.get_next()

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())
