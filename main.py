INDEX_ERROR_MESSAGE = "LinkedList: assignment index out of range"


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"Node(value={self.value}, next_node={'Node' if self.next_node else None})"


class LinkedList:
    def __init__(self, lis=()):
        self._first = Node()  # dummy node
        self._last = None
        self._num_items = 0  # This is length of array excluding dummy node

        for number in lis:
            self.append(number)

    def print(self):
        print('Linked List', end=" : ")
        current = self._first
        while current:
            print(current.value, end=' ')
            current = current.next_node

        print()

    def append(self, number):
        """
        Example:
            # 34 -> 45 -> 56
            # new_node => t = 56, nn -> 34
            # 34 -> 45 -> 56 -> 34
        """
        new_node = Node(value=number)
        if self._last is None:
            self._first.next_node = new_node
        else:
            self._last.next_node = new_node
        self._last = new_node
        self._num_items += 1

    def __getitem__(self, index):
        if index < 0 or index >= self._num_items:
            raise IndexError(INDEX_ERROR_MESSAGE)

        current = self._first.next_node
        for _ in range(index):
            current = current.next_node

        return current

    def __setitem__(self, index, value):
        """
        Example:
            # key = 3
            # None -> 12 -> 23 -> 45
            # None -> 12 -> 23 -> 44
        """

        if index < 0 or index >= self._num_items:
            raise IndexError(INDEX_ERROR_MESSAGE)

        current = self._first.next_node
        for _ in range(index):
            current = current.next_node

        current = self[index]
        current.value = value

    def insert(self, index, value):
        """
        Example:
            # None -> 12 -> 23 -> 45
            # temp = 23
            # temp.next(12) = new (30)
            # new (60).next = temp (23)
            # None -> 12 -> 30 -> 23 -> 45
        """
        if index < 0:
            raise IndexError(INDEX_ERROR_MESSAGE)

        # Here we used self._first as current node because we want one node before given index node
        current = self._first
        for _ in range(index):
            current = current.next_node
            if current is None:
                raise IndexError(INDEX_ERROR_MESSAGE)

        next_node = current.next_node

        new_node = Node(value=value)
        current.next_node = new_node
        new_node.next_node = next_node

        if current == self._last:
            self._last = new_node

        self._num_items += 1

    def __contains__(self, value):
        current = self._first.next_node
        while current:
            if current.value == value:
                return True
            current = current.next_node

        return False

    def __eq__(self, other_linked_list):
        if self._num_items != other_linked_list._num_items:
            return False

        current1 = self._first.next_node
        current2 = other_linked_list._first.next_node
        for _ in range(self._num_items):
            if current1.value != current2.value:
                return False

            current1 = current1.next_node
            current2 = current2.next_node

        return True

    def __delitem__(self, index):
        if index < 0 or index >= self._num_items:
            raise IndexError(INDEX_ERROR_MESSAGE)

        previous = self._first
        for _ in range(index):
            previous = previous.next_node
            if previous is None:
                raise IndexError(INDEX_ERROR_MESSAGE)

        current_node = previous.next_node

        if current_node == self._last:
            self._last = previous
        else:
            previous.next_node = current_node.next_node

    def remove(self, value):
        previous = self._first
        while previous:
            if previous.next_node and previous.next_node.value == value:
                break
            previous = previous.next_node
        else:
            raise ValueError('LinkedList.remove(x): x not in list')

        current_node = previous.next_node

        if current_node == self._last:
            self._last = previous
        else:
            previous.next_node = current_node.next_node


if __name__ == '__main__':
    # Part A

    # Ex 1
    empty_list = LinkedList()
    print(f"_first :: {empty_list._first}")
    print(f"_last :: {empty_list._last}")
    empty_list.print()

    lst = LinkedList([1, 2, 3, 2, 1])
    print(f"_first :: {lst._first}")
    print(f"_last :: {lst._last}")
    lst.print()

    del empty_list
    del lst
    print('############################################################')

    # Ex 2
    lst = LinkedList()
    lst.append(12)
    print(f"_first :: {lst._first}")
    print(f"_last :: {lst._last}")

    lst.append(22)
    print(f"_first :: {lst._first}")
    print(f"_last :: {lst._last}")

    lst.append(50)
    print(f"_first :: {lst._first}")
    print(f"_last :: {lst._last}")

    lst.print()

    del lst
    print('############################################################')

    # Ex 3
    lst = LinkedList([1, 2, 3, 2, 1])
    print(lst[0])
    print(lst[1])
    print(lst[2])
    print(lst[3])
    print(lst[4])
    # print(lst[5])  # raises IndexError

    print('############################################################')

    # Ex 4
    lst.print()
    lst[3] = 45
    lst.print()

    print('############################################################')

    # Ex 5
    lst.print()

    lst.insert(5, 100)
    lst.print()
    print(f"_first :: {lst._first}")
    print(f"_last :: {lst._last}")

    lst.insert(0, 100)
    lst.print()
    print(f"_first :: {lst._first}")
    print(f"_last :: {lst._last}")

    del lst
    print('############################################################')

    # Part B

    # Ex 1
    lst = LinkedList([1, 2, 3, 2, 1])
    if 3 in lst:
        print('Yes 3 is present in linked-list')
    else:
        print('No, 3 is not present in linked-list')

    if 30 in lst:
        print('Yes 30 is present in linked-list')
    else:
        print('No, 30 is not present in linked-list')

    print('############################################################')

    # Ex 2
    lst1 = LinkedList([1, 2, 3, 2, 1])
    lst2 = LinkedList([1, 2, 3, 2, 1])

    if lst1 == lst2:
        print('Equal linked-list')
    else:
        print('Not equal linked-list')

    lst1 = LinkedList([1, 2, 3, 1])
    lst2 = LinkedList([1, 2, 3, 2, 1])

    if lst1 == lst2:
        print('Equal linked-list')
    else:
        print('Not equal linked-list')

    del lst1
    del lst2
    print('############################################################')

    # Ex 3
    lst = LinkedList([1, 2, 3, 1])
    lst.print()
    del lst[2]
    lst.print()
    # del lst[10]  # Raises IndexError
    # lst.print()

    print('############################################################')

    # Ex 4
    lst = LinkedList([1, 2, 3, 1])
    lst.print()
    lst.remove(1)
    lst.print()
    # lst.remove(1)  # raises ValueError

    print('############################################################')
