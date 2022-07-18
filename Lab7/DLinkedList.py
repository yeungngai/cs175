#----------------------------------------------------
# Lab 7, Exercise 2: Doubly Linked Lists
# TO DO: complete mandatory methods in DLinkedList class
# TO DO (optional): complete optional methods in DLinkedList class
# to get better understanding of manipulating linked lists
#
# Author: Yi Yang
# Collaborators/references:
#   - CMPUT 175 provided complete DLinkedListNode
#   - CMPUT 175 provided init, search, index methods for DLinkedList
#   - CMPUT 175 provided tests for DLinkedList
#----------------------------------------------------


class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious

class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def search(self, item):
        current = self.__tail
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getPrevious()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1

        return index        

    def insert(self, pos, item):
        # inserts an item at a given position to the linked list
        if pos == 0:
            self.add(item)
        elif pos >= self.__size:
            self.append(item)
        else:
            new_node = DLinkedListNode(item, None, None)
            current = self.__head
            tempPos = 0
            while tempPos != pos - 1:
                current = current.getNext()
                tempPos = tempPos + 1
            new_node.setPrevious(current)
            new_node.setNext(current.getNext())
            current.setNext(new_node)
            next_node = current.getNext()
            next_node.setPrevious(new_node)
            self.__size = self.__size + 1

    def searchLarger(self, item):
        # Return the position of the first element that is larger than the given item, if no there is no larger item,
        # the method returns -1
        current = self.__head
        for i in range(self.__size):
            if current.getData() > item:
                return i
            current = current.getNext()
        return -1

    def getSize(self):
        # returns the size of the list
        return self.__size
    
    def getItem(self, pos):
        # return the item at the given position, an exception will be raised if the position outside of the list
        if pos > self.__size - 1:
            raise Exception('Position is outside of the list')
        else:
            current = self.__head
            if pos < 0:
                pos = pos + self.__size
            for i in range(self.__size):
                if pos == i:
                     return current.getData()
                current = current.getNext()

    def __str__(self):
        # returns a string representation of the list
        current = self.__head
        string = ''
        while current != None:
            string = string + str(current.getData()) + " "
            current = current.getNext()
        string = string[0:len(string)-1]
        return string

    def add(self, item):
        # adds an item to list at the beginning
        new_node = DLinkedListNode(item, self.__head, None)
        if self.__head != None:  # there is a head
            self.__head.setPrevious(new_node)
        else:  # adding to empty list
            self.__tail = new_node
        self.__head = new_node
        self.__size += 1

    def remove(self, item):
        # search for the item and remove it
        # the method assumes the item exists
        current = self.__head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:  # removing first node
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if (current.getNext() != None):
            current.getNext().setPrevious(previous)
        else:  # removing last node
            self.__tail = previous
        self.__size -= 1

    def append(self, item):
        # adds the item to the end of the list
        new_node = DLinkedListNode(item, None, None)
        if (self.__head == None):
            self.__head = new_node
        else:
            self.__tail.setNext(new_node)
            new_node.setPrevious(self.__tail)

        self.__tail = new_node
        self.__size += 1

    def pop1(self):
        # optional exercise
        pass

    def pop(self, pos=None):
        # optional exercise
        # Hint - incorporate pop1 when no pos argument is given
        pass


def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.insert(0, "Hello")
    linked_list.insert(1, "World")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    '''
    OPTIONAL TESTS FOR OPTIONAL EXERCISE - do not need to demo
    '''
    '''
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
    '''
                    
    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(9, -1, -1):
        int_list.insert(0,i)

    is_pass = (int_list.getSize() == 10)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(8) == 9)
    assert is_pass == True, "fail the test"

    int_list.insert(7,801)

    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-1) == 9)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 801)
    assert is_pass == True, "fail the test"

                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")
                
if __name__ == '__main__':
    test()
