"""
Project 2
CSE 331 F23 (Onsay)

Originally Authored By: Andrew McDonald & Alex Woodring & Andrew Haas & Matt Kight & Lukas Richters & Sai Ramesh
solution.py
"""

from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)


# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
     Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Check if DLL is empty
        :param: None
        :return: bool
        """
        return not self.head

    def push(self, val: T, back: bool = True) -> None:
        """
        Append a Node to the back or front of the SLL
        :param val: value of Node to append, back: bool to add to back or front
        :return: None
        """
        if not self.head:
            hed = Node(val)
            self.head = hed
            self.tail = hed
            self.size += 1
            return
        if back:
            nxt = Node(val, None, self.tail)
            self.tail.next = nxt
            self.tail = nxt
        else:
            pre = Node(val,self.head)
            self.head.prev = pre
            self.head = pre
        self.size += 1

    def pop(self, back: bool = True) -> None:
        """
        Remove a Node from the back or front of the SLL
        :param back: bool to remove from back or front
        :return: None
        """
        if not self.head:
            return
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return
        if back:
            pre = self.tail.prev
            pre.next = None
            self.tail = pre
        else:
            nxt = self.head.next
            nxt.prev = None
            self.head = nxt
        self.size -= 1

    def list_to_dll(self, source: List[T]) -> None:
        """
        Transforms a python list to a DLL in place
        :param self: empty DLL, list
        :return: None
        """
        if not source:
            return
        if self.head:
            self.head = self.tail = None
            self.size = 0
        self.head = Node(source[0])
        self.tail = self.head
        self.size = 1
        curr = self.head
        for i in range(1, len(source)):
            nxt = Node(source[i], None, curr)

            curr.next = nxt
            curr = curr.next
            self.tail = curr
            self.size += 1







    def dll_to_list(self) -> List[T]:
        """
        Transforms a DLL to a python list
        :param self: DLL
        :return: List representation of the DLL
        """
        res = []
        temp = self.head
        while temp:
            res.append(temp.value)
            temp = temp.next
        return res

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Construct list of Node with value val in the DLL and returns the associated Node object list
        :param val: T
        :return: List of nodes with val
        """
        res = []
        if self.head:
            temp = self.head
            while temp:
                if temp.value == val:
                    res.append(temp)
                temp = temp.next
        return res


    def find(self, val: T) -> Node:
        """
        Finds first Node with value val in the DLL and returns the associated Node object
        :param val: T
        :return: First Node with value val
        """
        nodes = self._find_nodes(val)
        if nodes:
            temp = self.head
            while temp:
                if temp == nodes[0]:
                    return temp
                temp = temp.next
        else:
            return None


    def find_all(self, val: T) -> List[Node]:
        """
        Finds all Node objects with value val in the DLL and returns a standard Python list of the associated Node objects
        :param val: T
        :return: List of nodes with val
        """
        res = []
        nodes = self._find_nodes(val)
        if nodes:
            for node in nodes:
                if node.value == val:
                    res.append(node)
        return res

    def _remove_node(self, to_remove: Node) -> None:
        """
        Remove a node in the linked list given a reference to it
        :param: to_remove: Node: Node to be removed from the DLL.
        :returns: None
        """
        nxt = to_remove.next
        pre = to_remove.prev
        if self.head == self.tail == to_remove:
            self.head = self.tail = None
            return
        if to_remove == self.head:
            self.head = nxt
        if to_remove == self.tail:
            self.tail = pre
        if to_remove.next:
            to_remove.next.prev = pre
        if to_remove.prev:
            to_remove.prev.next = nxt




    def remove(self, val: T) -> bool:
        """
        Removes first Node with value val in the DLL
        :param: to_remove: Node: Node to be removed from the DLL.
        :returns: bool
        """
        if self.head:
            len1 = self.size
            temp = self.head
            while temp:
                if temp.value == val:
                    self._remove_node(temp)
                    self.size -= 1
                    break
                temp = temp.next
            if self.size != len1:
                #self.size -= 1
                return True
        return False



    def remove_all(self, val: T) -> int:
        """
        Removes all Node objects with value val in the DLL
        :param: to_remove: Node: Node to be removed from the DLL.
        :returns: int
        """
        count = 0
        if self.head:
            curr = self.head
            while curr:
                nxt = curr.next
                if curr.value == val:
                    self._remove_node(curr)
                    count += 1
                    self.size -= 1
                curr = nxt
        return count

    def reverse(self) -> None:
        """
        Reverse DLL in place
        :param: None
        :returns: None
        """
        if self.size == 1:
            return
        if self.head:
            curr = self.head
            while curr:
                pre = curr.prev
                nxt = curr.next
                curr.prev = nxt
                curr.next = pre
                curr = curr.prev
            self.head, self.tail = self.tail, self.head



class BrowserHistory:
    def __init__(self, homepage: str):
        """
        Initialize a browser history object
        :param: homepage url: str
        :returns:
        """
        self.head = self.tail = Node(homepage)
        self.currNode = Node(homepage)
        self.current = homepage

    def get_current_url(self) -> str:
        """
        Return the current URL
        :param: None
        :returns: url: string
        """
        return self.current

    def visit(self, url: str) -> None:
        """
        Visit the URL supplied to the method
        :param: url: str
        :returns: None
        """
        if self.head and self.head == self.tail:
            urlNode = Node(url, None, self.head)
            self.head.next = urlNode
            self.tail = urlNode
            urlNode.prev = self.head
            self.current = url
            self.currNode = urlNode
            return
        curr = self.head
        while curr:
            if curr is self.currNode:
                urlNode = Node(url, None, curr)

                if urlNode.next:
                    urlNode.next = None
                urlNode.prev = curr
                curr.next = urlNode
                self.tail = urlNode
                self.current = url
                self.currNode = urlNode
                return
            curr = curr.next

    
    def backward(self) -> None:
        """
        Return to the last page in history, if there is no previous page don't go back
        :param: None
        :returns: None
        """
        if self.head:
            curr = self.head
            while curr:
                if curr.value == self.current:
                    if curr.prev is None:
                        return
                    while metrics_api(curr.prev.value):
                        curr = curr.prev
                    self.current = curr.prev.value
                    self.currNode = curr.prev
                curr = curr.next


    def forward(self) -> None:
        """
        Skip to the next page in history, if there is no next page don't go forward
        :param: None
        :returns: None
        """
        if self.head:
            curr = self.head
            while curr:
                if curr.value == self.current:
                    if curr.next is None:
                        return

                    while curr.next and metrics_api(curr.next.value):
                        curr = curr.next
                    if curr.next and not metrics_api(curr.next.value):
                        self.current = curr.next.value
                        self.currNode = curr.next

                curr = curr.next

# DO NOT MODIFY
intervention_set = set(['https://malicious.com', 'https://phishing.com', 'https://malware.com'])
def metrics_api(url: str) -> bool:
    """
    Uses the intervention_set to determine what URLs are bad and which are good. 

    :param url: The url to check.
    :returns: True if this is a malicious website, False otherwise.
    """
    if url in intervention_set:
        return True
    return False
