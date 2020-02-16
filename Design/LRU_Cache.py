'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


'''

class Node:
    
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict_ = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        
        if key in self.dict_:
            node = self.dict_[key]
            self.remove(node)
            self.add(node)
            return node.data
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict_:
            self.remove(self.dict_[key])
            del self.dict_[key]
            
        if(len(self.dict_)<self.capacity):
            node = Node(key,value)
            self.dict_[key] = node
            self.add(node)
        else:
            delNode = self.head.next
            self.remove(delNode)
            node = Node(key,value)
            self.dict_[key] = node
            self.add(node)
            del self.dict_[delNode.key]

    def remove(self, node):
        
        nextNode = node.next
        prevNode = node.prev
        
        prevNode.next = nextNode
        nextNode.prev = prevNode

        
    def add(self,node):
        
        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode
        
        node.next = self.tail
        self.tail.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


