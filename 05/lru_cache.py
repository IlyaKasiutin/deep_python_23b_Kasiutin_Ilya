"""LRU Cache class"""


class LRUCache:
    """LRU Cache implementation"""
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """Get value by key"""
        if key not in self.cache:
            return None

        node = self.cache[key]
        self.__move_to_front(node)
        return node.value

    def set(self, key, value):
        """Set key-value"""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.__move_to_front(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.__add_to_front(node)

            if len(self.cache) > self.limit:
                self.__remove_last()

    def __add_to_front(self, node):
        """Add to the beginning of the list"""
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def __remove_last(self):
        """Remove the eldest element"""
        if not self.tail:
            return

        del self.cache[self.tail.key]

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def __move_to_front(self, node):
        """Replace element"""
        if node == self.head:
            return

        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node


class Node:
    """Subclass for LRUCache"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
