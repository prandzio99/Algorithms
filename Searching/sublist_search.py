# a simple implementation of sublist search algorithm

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


# function finds list a in list b
def find_list(a, b):
    if not a and not b:
        return True

    if not a or not b:
        return False

    ptr_a = a
    ptr_b = b

    while ptr_b:
        ptr_b = b
        while ptr_a:
            if not ptr_b:
                return False
            elif ptr_a.value == ptr_b.value:
                ptr_a = ptr_a.next
                ptr_b = ptr_b.next
            else:
                break
        if not ptr_a:
            return True
        ptr_a = a
        b = b.next

    return False


# test code
if __name__ == '__main__':
    node_a = Node(1)
    node_a.next = Node(2)
    node_a.next.next = Node(3)
    node_a.next.next.next = Node(4)

    node_b = Node(1)
    node_b.next = Node(2)
    node_b.next.next = Node(1)
    node_b.next.next.next = Node(2)
    node_b.next.next.next.next = Node(3)
    node_b.next.next.next.next.next = Node(4)

    print(find_list(node_a, node_b))
    print(find_list(node_a, node_b.next.next.next))
