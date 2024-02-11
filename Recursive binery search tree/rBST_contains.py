def __r_contains(self, current_node, value):
    if current_node == None:
        return False
    if current_node == value:
        return True
    if current_node > value:
        return self.__r_contains(current_node.left, value)
    if current_node < value:
        return self.__r_contains(current_node.right, value)

def r_contains(self, value):
    return self.__r_contains(self.root, value) 