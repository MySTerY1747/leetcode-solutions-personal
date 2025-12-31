# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#
# The functions get and put must each run in O(1) average time complexity.


class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value=value, prev=None, next=self.head)

        if self.head is not None:
            self.head.prev = new_node
        else:
            # list was empty
            self.tail = new_node

        self.head = new_node
        return new_node

    def delete(self, node: Node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            # node is head
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            # node is tail
            self.tail = node.prev

        node.prev = None
        node.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_capacity: int = 0
        self.last_occurence_dict: dict[int, Node] = {}
        self.order_list: DoublyLinkedList = DoublyLinkedList()
        self.values: dict[int, int] = {}

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        return_value: int = self.values[key]

        key_node: Node = self.last_occurence_dict[key]
        self.order_list.delete(key_node)
        new_key_node: Node = self.order_list.insert(key)
        self.last_occurence_dict[key] = new_key_node
        return return_value

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key] = value
            key_node: Node = self.last_occurence_dict[key]
            self.order_list.delete(key_node)
            new_key_node: Node = self.order_list.insert(key)
            self.last_occurence_dict[key] = new_key_node

        elif self.cur_capacity < self.capacity:
            self.values[key] = value
            new_key_node: Node = self.order_list.insert(key)
            self.last_occurence_dict[key] = new_key_node
            self.cur_capacity += 1

        else:
            node_to_delete: Node = self.order_list.tail
            node_value = node_to_delete.value
            self.order_list.delete(node_to_delete)
            del self.last_occurence_dict[node_value]
            del self.values[node_value]

            self.values[key] = value
            new_node: Node = self.order_list.insert(key)
            self.last_occurence_dict[key] = new_node
