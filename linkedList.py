#! /user/env/bin python

"""
    Author : Mikias Berhaun
    Date : Aug 29 2019
    Desc: Simple Linked List implementation
"""
#class Node is the main class for the linked list
class Node:
    """
    the constructor of the class contains five class variables
    data holds the data for the node , head is Node for the list which is the starting point
    , next points to the next node , tail is Node at the end of the list and length is number 
    for counting the nodes in the list
    """
    def __init__(self):
        self.data = None
        self.head = None
        self.next = None
        self.tail = None
        self.length = 0
    
    #set and get methods for the data 
    def setData(self , data):
        self.data = data 
    def getData(self):
        return self.data 
    #set and get methods for the next pointer
    def setNext(self , next):
        self.next = next 
    def getNext(self):
        return self.next 
    #get method for the length
    def getLength(self):
        return self.length 
    #return True if the node has next node not null or None
    def hasNext(self):
        return self.next != None 
    #returns count for the list nodes almost similar with the length
    def ListLength(self):
        count = 0
        current = self.head 
        while current != None:
            count += 1
            current = current.getNext() 
        return count
    #display the list
    def display(self):
        current = self.head 
        while current != None:
            print("{} -> ".format( current.getData() ) , end="")
            current = current.getNext()
        print("\n")
    #returns data which is found at a certain valid position
    def getDataPos(self , pos):
        if pos < 0 or pos > self.length:
            raise ValueError("invalid position used")
        else:
            current = self.head
            count = 0 
            while count != pos and current.getNext() != None:
                current = current.getNext()
                count += 1
            data = current.getData()
        return data

    """ 
    below are main list method , for inserting and delete data
    
    for inserting data we have three cases
        # insert at the beginning
        # insert at the end
        # insert at random position


    as well for deleting data we have three cases
        # deleting at the beginning
        # deleting at the end
        # deleting at random position
    """
    #inserting at the beginning 
    def insertHead(self , data):
        newNode = Node()  #creates a new Node
        newNode.setData(data)
        if self.length == 0:  #if the list is empty just set the head to the new node
            self.head = newNode
            self.length += 1
        else:
            newNode.setNext(self.head)  
            self.head = newNode 
            self.length += 1
    
    #inserting at the end
    def insertTail(self , data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = self.tail = newNode
            self.length += 1 
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)
            newNode.setNext(None)
            self.length += 1
    #insert at random position
    def insertRandom(self , pos , data):
        if pos < 0 or pos > self.length:
            raise ValueError("Invalid position used")
        else:
            newNode = Node()
            newNode.setData(data)
            if pos == 0:
                self.insertHead(data)
            elif pos == self.length:
                self.insertTail(data)
            else:
                count = 0
                current = self.head
                while count != pos:
                    current = current.getNext()
                    count += 1
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1
    #delete at the beginning or head
    def deleteHead(self):
        if self.length == 0:
            raise ValueError("List is Empty")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0 
        else: 
            self.head = self.head.getNext()
            self.length -= 1
    #delete at the end of the list or tail
    def deleteTail(self):
        if self.length == 0:
            raise ValueError("List is empty") 
        elif self.length == 1:
            self.head = None
            self.tail = None 
            self.length -= 1
        else:
            current = self.head
            prev = self.head
            while current.getNext() != None:
                prev = current
                current = current.getNext()
            prev.setNext(None)
            self.length -= 1
    #delete at random position given by the user / valid position
    def deleteRandom(self , pos):
        if pos < 0 or pos > self.length:
            raise ValueError("invalid position")
        if pos == 0: 
            self.deleteHead()
        elif pos == self.length:
            self.deleteTail
        else:
            current = self.head 
            prev = self.head
            count = 0
            while count < pos and current.getNext() != None:
                count += 1
                if count == pos:
                    prev.setNext(current.getNext())
                    self.length -= 1
                    return 
                else:
                    prev = current
                    current = current.getNext()        
    #set the list to empty
    def clearList(self):
        self.head = None
        self.length = 0


        
