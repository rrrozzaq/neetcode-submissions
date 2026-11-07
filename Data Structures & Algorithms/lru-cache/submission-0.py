# // so LRU cache, it means least recently used, and in this problem it says that 
# the class should support 3 operatons, so it's LRUCache with a parameter capacity
# to init the lrucace size of capacity, and get ops with a parameter return value
# of the key if the key, otherwise return -1, and finally the put ops with the parameters
# key value to update the value of the key if the key exist, otherwise we add the
# key-value pair to the cache. if the new pair cause the cache size exceed its capacity,
# we have to remote the least recently used

# ok so before i'm going to the solution, i'd like to clarify if the 'recently used' means
# accessed by either get or put right? so the key is considered used if a get or put
# operation is called.

# so yes, i think of solutions for this, there are 2 solutions for this problem.
# so the first one is brute force solution, i would store the key-value pairs into a
# dictionary and maybe an array or list to track usage order

# so for example, when we call get(key), we move that key to the end of list and 
# when capacity exist, we remove the first element that is the lru.

# but there are problems with this solution, the issue are, removing from front of the list
# is o(n) because it requires shifting elements.

# so for example we have a list [3,5,2,8], if we remove index 0 for example, it 
# would be [5,2,8], but why it's not effiecient? so because it's an array or dynamic 
# array, if we remove the index 0, the elements behind it have to move or shift 
# to the left one by one, or it's called shifting elements, so 5 to index 0
# 2 to index 1, and 8 to index 2. so imagine if we have 1mill data, if we remove the 
# index of 0, that means 999.999 have to shift. so it's gonna be a big problem. that's why
# pop(0) => o(n).

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.usage = []

#     def get(self, key: int) -> int:
#         if key not in cache:
#             return -1
        
#         self.usage.remove(key)
#         self.usage.append(key)

#         return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.usage.remove(key)
#         elif len(self.cache) == self.capacity:
#             lru_key = self.usage.pop(0)
#             del self.cache[lru_key]

#         self.cache[key] = value
#         self.usage.append(key)
        

# and yeah i'm not gonna use this solution, but instead i would use doubly linked list 
# to track the use of the data or "recently used". so to get o(1), we need a hashmap to
# find the node and doubly linked list to move the node in o(1). why doubly? we need to
# remove nodes from middle in o(1) and singly linked list can't do that effieciently.
# but why? so singly linked list is a single node right, so every single node point to
# a single node, what is single node? that means the node is only point to another single 
# node one time, singly linked list only have value and the pointer to next node. doubly
# linked list on the other hand, have value, next pointer, and previous, so the node can
# point to the next node and the previous node, which is singly linked list can't do.

# so singly linked list is like this right, for example A->B->C->D->None. every node
# only have value and the next point to the next node. there's no prev pointer.
# so for example if we would like to remove the C, we have to change B.next=D. but 
# the problem is, we should know who B is. if we only hold C and we don't know who B is,
# that means we have to start from the HEAD and running trough one by one untill we find
# the node before C, so it is o(n). and if we take a look to doubly linked list, every nodes
# have value, next pointer, and prev pointer. so if we would like to remove C, that means
# we can directly have C.prev=B and C.next=D. so we can do B.next=D and D.prev=B, that's it.
# we don't have to traversal trought all the node. that's why remove in doubly linked list
# is o(1)

# so we maintain:
# 1. HEAD = MRU
# 2. TAIL = LRU

# when:
# get(key) -> move node to the head
# put(key) -> add to head
# capacity is full -> remove the tail

# ok so let's code it up

# so first we need a class of node

# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {} // key -> value(node) pairs

#         and before we even have any values in the cache, we want to have a couple
#         dummy pointers, a couple dummy nodes, which tell us what are the most recent
#         and least recent values that we added, so we can just initialize these
#         to zero for default values, so zero, zero. 

#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)

#         so these node do not store real cache data, it only used to help manage
#         the linked list

#         and initially we want these nodes to be connected each other, because 
#         if we're inserting or putting a new node, we want to put it in the middle 
#         between head and tail, and we can do that with some pointer stuff.

#         self.head.next = self.tail
#         self.tail.prev = self.head

#         and the HEAD is gonna help us to find the LRU and TAIL is gonna be
#         most recent

#     and now let's move to the get function

#     and these helper function are going to be applied on the linked list, so we
#     are going to pass in the node that we want to remove from doubly linked list

#     def _remove(self, node):
#         so if we have three nodes, and we wanna remove the middle node, we have to change
#         the pointer between previous and next node with the current node

#         because this is a doubly linked list, and each node has pointers to both its previous
#         and next nodes, so i can acces them directly without any traversal
#         so we can acces the previous of the node, and save it to the variable prev_node
#         prev_node = node.prev 
#         next_node = node.next

#         and then i just update the previous node so it skips the current node and points directly
#         to the next node
#         so the next of prev_node is next_node
#         prev_node.next = next_node
#         and i also update the next node to point back to the previous node
#         so the previous of the next_node is prev_node
#         next_node.prev = prev_node

#         and after this, the current not is fully disconnected from the list, which means
#         it already removed
#         notice that i dont neet any check condition here. this works for any node because of
#         the dummy head and tail nodes

#     def _add(self, node):
#         so first, i would connect the new node to the nodes around the head. beacuse 
#         the function adds a node right after the head dummy node, which represent
#         the mru position
#         so i would connect the next of the node with the first node right after head
#         so i make the new node point to the current first real node
#         node.next = self.head.next
#         and then i connect the previous of new node with head
#         node.prev = self.head

#         so we finish connect the new node to the node around the head, but it's not over yet
#         because the head is still point to the next of the head, and the next of the head
#         which is firsl node still point to the head. so we have to change the connection
#         between this too
#         self.head.next.prev = node
#         self.head.next = node

#         so yeah it's finished, let me try to run it


#     ini penjelasan setelah dari get, trus nanti lanjut ke put operations dulu
#     and when we add, we gonna add it at front
#     and the remove is just gonna remove from the list
#     so these are going to be a pointer function, we're going to manipulating some pointer

#     def get(self, key: int) -> int:
#         so if the key exist we wanna return value, otherwise return -1
#         if key not in self.cache:
#             return -1
#         and it's o(1), this lookup is o(1) because dictionaty in python is
#         constant time on average
#         and if the key exist, i retrieve the corresponding node directly from the dictionary
#         so if key is in the cache we return value
#         return self.cache[key].value

#         but since this in an LRU cache,
#         accessing a key, or call the operation either it's get or put, in this context 
#         is get ops, it's considered as MRU. sowe also need to remove the node and move 
#         it to the front of the list. so i need a helper function to remove and 
#         add it to the front of the list

#         so since we're getting the helper function, we gonna remove and insert
#         node = self.cache[key] // so im gonna save that to the variable node so it looks clean
#         since the key is accessed, it becomes mru. so i remove it from its current
#         position in the doubly linked list
#         self._remove(node)
#         self._add(node) // now i insert the node right after the HEAD, which represent
#         the most recently used position

#         return node.value //return the value that stored in the node

#     and now let's move to the put function. so for the put operation, i need to insert
#     or update the key-value pair in the cache. if the key already exist, i should
#     update the value and mark it as mru. but if the key doesn't exist and the cache
#     capacity is full, then i must remove the LRU item before inserting the new one

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache: // so first i check whether the key already exist in cache
#             if the key exist, same with get ops, i get the node directly from dictionary
#             node = self.cache[key] //and im gonna save that to the variable node
#             then i also remove it from its current position in the linked list
#             self._remove(node)
#             so why remove it? because later i will insert it again at the front as the MRU item

#         and if the doesn't exist, i need to check if the cache capacity has reached its
#         size of capacity
#         else:
#             if len(self.cache) == self.capacity:
#                 so if the cache is full, i remove or evict the lru item. 
#                 and the lru node is always right before the tail dummy node
#                 lru = self.tail.prev
                
#                 and then i remove this node from the linked list
#                 self._remove(lru)

#                 and then delete its key from the dictionary
#                 del self.cache[lru.key]

#                 so i must remove it from both data structures, removing
#                 only from the list is not enough because the dict would sill hold
#                 a reference to it
        
#         now i would create a new node with the given key, value
#         new_node = Node(key, value)

#         and then i store it in the dictionary for o(1) access
#         self.cache[key] = new_node

#         and i add it right after the head to mark it as MRU
#         self._add(new_node) 

#     and now we have to fill out the 2 helper function


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
