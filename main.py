

class Node:
    def __init__(self, value=None, node=None):
        self.value = value
        self.next_node = node

# Ex 1
class LinkedList:
    def __init__(self):
        self._first = Node(value=None, node=None)
        self._last = None
        self.count = 0

    def append(self, number):
        self.count += 1
        new_node = Node(value=number, node=None)
        if self._first.next_node is None:
            self._first.next_node = new_node

        if self._last is None:
            self._last = new_node
        else:
            temp = self._last
            temp.next_node = new_node
            self._last = new_node

            # 34 -> 45 -> 56
            # new_node => t = 56, nn -> 34
            # 34 -> 45 -> 56 -> 34

    def print(self):
        printval = self._first
        while printval:
            print(printval.value)
            printval = printval.next_node

    def __getitem__(self, item):
        current = self._first.next_node
        for i in range(self.count):
            if current.value == item:
                return current
            current = current.next_node

        raise ValueError('Element not found')

    def __setitem__(self, key, value):
        if key == 0 or key > self.count:
            raise IndexError('Index out of range')

        current = self._first.next_node
        for i in range(key-1):
            current = current.next_node
        current.value = value

        # key = 3
        # None -> 12 -> 23 -> 45
        # None -> 12 -> 23 -> 44

    def insert(self, key, value):
        if key == 0 or key > self.count + 1:
            raise IndexError('Index out of range')
        self.count += 1

        new_node = Node(value, None)

        current = self._first
        for i in range(key-1):
            current = current.next_node

        temp = current.next_node
        current.next_node = new_node
        new_node.next_node = temp


        # None -> 12 -> 23 -> 45
        # temp = 23
        # temp.next(12) = new (30)
        # new (60).next = temp (23)
        # None -> 12 -> 30 -> 23 -> 45

    def __contains__(self, item):
        current = self._first
        while current:
            if current.value == item:
                return True
            current = current.next_node

        return False

    def __eq__(self, other):
        if self.count != other.count:
            return False

        current1 = self._first.next_node
        current2 = other._first.next_node

        while current1 and current2:
            if current1.value != current2.value:
                return False

            current1 = current1.next_node
            current2 = current2.next_node

            if (current1 and not current2) or (current2 and not current1):
                return False

        return True

if __name__ == '__main__':
    # lis = [12, 45, 23, 56]
    lst = LinkedList()

    # Ex 2
    lst.append(12)
    print(f"{lst._first.value} and {lst._last.value}") # None 12
    lst.append(24)
    print(f"{lst._first.value} and {lst._last.value}") # None 12 24
    lst.append(34)
    print(f"{lst._first.value} and {lst._last.value}")  # None 12 24 34

    # Ex 3
    x = lst[24]
    if x is not None:
        print(f'Found x : {x.value}')
    else:
        print('x is not found')

    x = None
    try:
        x = lst[2]
    except ValueError:
        pass
    if x is not None:
        print(f'Found x : {x.value}')
    else:
        print('x is not found')


    # Ex 4
    print('--------------')
    lst.print()
    print('--------------')

    lst[3] = 44
    lst.print()

    # Ex 5
    print('--------------')
    lst.print()
    print('--------------')
    lst.insert(1, 60)
    lst.print()

    # Part B

    # Ex 1
    if 12 in lst:
        print('Yes')
    else:
        print('No')

    if 121 in lst:
        print('Yes')
    else:
        print('No')

    # Ex 2
    lst2 = LinkedList()
    if lst == lst2:
        print('Equal')
    else:
        print('Not equal')

    lst2 = lst
    if lst == lst2:
        print('Equal')
    else:
        print('Not equal')


