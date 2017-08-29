class MyValueError(ValueError):
    pass

class Node():
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
        
        
    def setData(self, data):
        self.data = data
        return self.data

    def setNext(self, next_el):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None    
        
    def __str__(self):
        print(self.element)
        
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_front(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.next.prev = node						
            self.head = node
    def append(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            node.prev = self.tail
            node.prev.next = node						
            self.tail = node
                      
    def get(self, i):
        assert i >= 0, "Index must be 0 or positive integer"
        ind = 0
        node = self.head
        while node:
            if ind == i:
                return node.data
                break
            node = node.next
            ind += 1
        return "Index out of range"
        
    def put(self, i, data):
        if i <= 0:
            raise MyValueError("Index must be > 0 or positive integer, to put in front use add_front")
        new_node = Node(data)
        ind = 0
        node = self.head
        while node:
            if ind == i:
                node.prev.next = new_node
                new_node.prev = node.prev
                new_node.next = node
                node.prev = new_node
                return None
            node = node.next
            ind += 1
        return "Index out of range"
        
    def delete(self, i):
        assert i >= 0, "Index must be 0 or positive integer"
        ind = 0
        node = self.head
        while node:
            if ind == i:
                node.prev.next = node.next
                node.next.prev = node.prev
                return None
            node = node.next
            ind += 1
        return "Index out of range"
        
    def size(self):
        node = self.head
        ind = 0
        while node:
            node = node.next
            ind += 1
        return ind
    
    def indexOf(self, element):
        node = self.head
        ind = 0
        while node:
            if node.data == element:
                return ind
            node = node.next
            ind += 1
        return "No elemet: %s in the list" % element
    
    def __str__(self):
        show = "["
        node = self.head
        if node != None:		
            while node.next != None:
                show += str(node.data) + ", "
                node = node.next
            show += str(node.data)
        show += "]"
        return show
    
    
    
if __name__ == "__main__":
    mylist = LinkedList()
    mylist.add_front(5)
    mylist.add_front(4)
    mylist.add_front(3)
    mylist.add_front(2)
    mylist.add_front(1)
    print(mylist)
    
    
    
    
    
    
    
    
        