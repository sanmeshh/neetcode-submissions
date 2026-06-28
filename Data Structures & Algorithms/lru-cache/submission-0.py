class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}#mapping the nodes
        
        self.left,self.right=Node(0,0),Node(0,0)

        self.left.next,self.right.prev=self.right,self.left #left will help us to remove lru,right will help us to insert new/recently used
        # node/val

    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    
    def insert(self,node):
        prev,nxt=self.right.prev,self.right  #in reference to our new node
        prev.next=node
        nxt.prev=node
        node.prev=prev
        node.next=nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #update its position so that it becomes the recently used node
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])#remove the old value
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])#insert it as the new node in our list

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key] #key is accessed from the node itself
            #operation is similar to delete(temp)      
