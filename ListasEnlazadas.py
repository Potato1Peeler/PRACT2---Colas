class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print(f"     Customer: {self.get_customer()}")
        print(f"     Quantity: {self.get_qtty()}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def get_info(self):
        return self.data

    def get_next(self):
        return self.next_node

class Queue():
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.front_node.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next_node = new_node
            self.rear_node = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_node = self.front_node
        self.front_node = self.front_node.get_next()
        if self.front_node is None:
            self.rear_node = None
        self._size -= 1
        return removed_node.get_info()

    def dump(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size()}")
        node = self.front_node
        element_number = 1
        while node is not None:
            print(f"   ** Element {element_number}")
            node.get_info().print_order()
            node = node.get_next()
            element_number += 1
        print("******************************")

queue = Queue()
queue.enqueue(Order(20, "cust1"))
queue.enqueue(Order(30, "cust2"))
queue.enqueue(Order(40, "cust3"))
queue.enqueue(Order(50, "cust3"))

queue.dump()
