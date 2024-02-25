# linked_list snake case
# LinkedList PascalCase
# linkedList camelCase


# -> None shows what the thing we are returning is a str, int etc. in this case nothing because it's none
# def __init__(self) -> None: this is a constructor
# Node have a value and a pointer value = element and  pointer = next
# A method is a function inside a class
# the get_element method gets the value of the element so if we call get_element() and our element is = 10 this method will return  10
# the set_element method sets a value that we give to the element, so if we call set_element(10) this will make the element = 10

class Node:
    def __init__(self) -> None:        
        self.element = None  #value
        self.next = None  #pointer

    def get_element(self):
        return self.element
    
    def set_element(self, value):   # We pass our parameter "value" to the function  
        self.element = value        # We make self.element equal to the "value"

    def get_next(self):
        return self.next
    
    def set_next(self, pointer):
        self.next = pointer
      
     
    # The __repr__ method is a magic method that ovewrites the default print value of the object, 
    # basically when we are printing we get <__main__.Node object at 0x000001362052A1E0> but by ovewriting we can make it print whatever we want
    # In this case we are calling the get_element() method that we made and we make it a string by using the str() method

    def __repr__(self) -> str:                              
       return str(self.get_element())



# TODO is_empty(), insert_head(), delete_head(), insert_tail(), delete_tail()
    
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None  #value
        self.tail = None  #pointer
    
    def is_empty(self):
        if self.head == None and self.tail == None:  #method one
            return True
        #return self.head == None and self.tail == None   #method two

    def insert_head(self, value):
        new_node = Node()
        new_node.set_element(value)

        #we ask the head where the first value is and we set it to new_node.next
        new_node.set_next(self.head)
        #now we say to the head to point to the new value because it's the first one
        self.head = new_node

        #if the list is empty the head and tail should point to the node
        if self.is_empty():
            self.tail = new_node

    def delete_head(self):
        pass

    def insert_tail(self):
        pass

    def delete_tail(self):
        pass



new_list = SinglyLinkedList()
new_list.insert_head(10)
print(new_list)
# my_node = Node()
# my_node.set_element(5)
# print(my_node)

# print("value before setting:", end=" ")
# # print("value before setting:") # The end=" " is used to make the print function to not go to the next line
# print(my_node.get_element())


# print("value after setting:", end=" ")
# my_node.set_element(30)
# print(my_node.get_element())

