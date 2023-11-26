#!/usr/bin/python3
"""
Node class
this defines a node of a singly linked list
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): Reference to the next node in the
        list, or None if it's the last node.

    Methods:
        __init__(self, data, next_node=None): Initializes a new node
        with the specified data.
        data (int): The data to be stored in the node.
        next_node (Node or None): Reference to the next node in the
        list (default is None).
        Raises:
        TypeError: If data is not an integer.
    """

    def __init__(self, data, next_node=None):
        """
        this initializes a new node with specific data
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the data  stored in  node to a new value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Returns the reference to the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the reference to next node in list"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object or None")

        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the linked list."""
        string = ""
        temp_node = self.__head

        while temp_node is not None:
            string += str(temp_node.data) + "\n"
            temp_node = temp_node.next_node

        return string

    def sorted_insert(self, value):
        """Inserts a new node with the specified value into the sorted
        position of the linked list.

        Args:
            value (int): The value to be inserted into the linked list.

        Description:
            This method inserts a new node with the specified value into the
            linked list while maintaining ascending order based on the values of
            the nodes. If the list is initially empty, the new node
            becomes the head of the list.
        """

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        temp_node = self.__head
        while temp_node.next_node is not None and \
                temp_node.next_node.data < value:
            temp_node = temp_node.next_node

        new_node.next_node = temp_node.next_node
        temp_node.next_node = new_node
