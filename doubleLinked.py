"""
    Author: Mikias Berhanu
    Date: Sept 1 2019
    Simple implementation of double linked list
"""

#main class LinkedList Node
class Node:
    #constructor
    def __init__(self):
        self.head = None
        self.tail = None 
        self.next = None
        self.prev = None 
        self.data = None
        self.length = 0
    """
    set and get methods for the next , prev pointers and data
    """
    def setData(self , data):
        self.data = data 
    def getData(self):
        return self.data 
    
    def setNext(self , next):
        self.next = next 
    def getNext(self):
        return self.next 
    
    def setPrev(self , prev):
        self.prev = prev 
    def getPrev(self):
        return self.prev 
    
    def getLength(self):
        return self.length

    """
    utility methods hasNext , ListLength and display
    """
    def hasNext(self):
        return self.next != None 
    
    #ListLength returns length of the list 
    def listLength(self):
        count = 0 
        current = self.head 
        while current.getNext() != None:
            count += 1
            current = current.getNext()
        return count 
    #getDataPos method returns data stored at a particular position
    def getDataPos(self , pos):
        if pos < 0 or pos > self.length:
            raise ValueError("Invalid Position")
        elif pos == 0:
            return self.head.getData()
        else: 
            current = self.head  
            count = 0
            while current.getNext() != None and pos != count:
                count += 1
                current = current.getNext()
            return current.getData()
    #display method traverse and display the list 
    def display(self):
        current = self.head 
        while current != None:
            print("{} -> ".format(current.getData()) , end="")
            current = current.getNext()
        print("\n")
    """
    Node main methods insert delete nodes
    """
    #insertHead method inserts data at the beginning of the list or the head
    def insertHead(self , data):
        newNode = Node() #creates new Node
        newNode.setData(data)
        #check if the list is empty
        if self.head == None:
            self.head = self.tail = newNode
            self.length += 1
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
            self.length += 1
    #insertTail method insert data at the end of the list or tail
    def insertTail(self , data):
        newNode = Node()
        newNode.setData(data)
        #check if the list is empty
        if self.head == None and self.tail == None:
            self.insertHead(data)
        else:
            current = self.head 
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)
            newNode.setPrev(current)
            newNode.setNext(None)
            self.length += 1 
    #insertRandom position insert data in the list at any given valid position
    """
    takes two arguments position where to be inserted and data that is going to be
    inserted
    """
    def insertRandom(self , pos , data):
        if pos < 0 or pos > self.length:
            raise ValueError("Invalid Position")
        elif pos == 0:
            self.insertHead(data)
        elif pos == self.length:
            self.insertTail(data)
        else:
            newNode = Node()
            newNode.setData(data)
            count = 0
            current = self.head 
            prev = self.head 
            while count != pos and current.getNext() != None:
                count += 1
                prev = current 
                current = current.getNext()
            prev.setNext(newNode)
            current.setPrev(newNode)
            newNode.setPrev(prev)
            newNode.setNext(current)
            self.length += 1 
    #deleteHead delete data from the head or beginning of the list
    def deleteHead(self):
        if self.head == None:
            raise ValueError("List is empty")
        elif self.length == 1:
            self.head = self.tail = None
            self.length = 0
        else:
            self.head = self.head.getNext()
            self.length -= 1
    #deleteTail delete data from the end of the list or tail
    def deleteTail(self):
        if self.head == None:
            raise ValueError("List is empty")
        elif self.length == 1:
            self.deleteHead()
        else:
            current = self.head 
            prev = self.head 
            while current.getNext() != None:
                prev = current 
                current = current.getNext()
            prev.setNext(None)
            self.length -= 1
    #deleteRandom deletes data at random position
    def deleteRandom(self , pos):
        if pos < 0 or pos > self.length:
            raise ValueError("Invalid Position")
        elif pos == 0:
            self.deleteHead()
        elif pos == self.length:
            self.deleteTail()
        else:
            current = self.head 
            prev = self.head 
            count = 0
            while count != pos and current.getNext() != None:
                count += 1
                prev = current 
                current = current.getNext() 
            prev.setNext(current.getNext())
            current.getNext().setPrev(prev)
            self.length -= 1
    #clearList method makes the entire list empty
    def clearList(self):
        self.head = None
    
