#!/usr/bin/python3
"""this is a module for a singly linked list"""


class Node:
    """A class representing a node in a singly linked list.

        Attributes:
            data (int): The data stored in the node.
            next_node (Node): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initialize a Node object.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the list.
                                        Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node.

            Args:
                value (int): The new data to be stored in the node.

            Raises:
                TypeError: If value is not an integer.
        """
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list.

            Returns:
                Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.

            Args:
                value (Node): The new next node in the list.

            Raises:
                TypeError: If value is not a Node object or None.
        """
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """A class representing a singly linked list.

        Attributes:
            head (Node): The head of the list.
        """

    def __init__(self):
        """Initialize a SinglyLinkedList object."""
        self.head = None

    def __str__(self):
        """Return a string representation of the list.

            Returns:
                str: A string representation of the list.
        """
        node_str = ""
        node_location = self.head
        while node_location:
            node_str += str(node_location.data) + "\n"
            node_location = node_location.next_node
        return node_str[:-1]

    def sorted_insert(self, value):
        """Insert a new node with the given value into the sorted list.

            Args:
                value (int): The value to be stored in the new node.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new_node.next_node = location.next_node
        location.next_node = new_node
