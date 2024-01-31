class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next_node): # is not None: can aslo be used
            pre = temp
            temp = temp.next_node
        self.tail = pre
        self.tail.next_node = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next_node
        temp.next_node = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def  get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next_node
        return temp
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    