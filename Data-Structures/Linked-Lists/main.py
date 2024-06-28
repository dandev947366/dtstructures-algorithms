class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> " if temp.next is not None else "\n")
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)    
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index==0:
            return self.pop_first()
        if index==self.length - 1:
            return self.pop()   
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
my_linked_list5 = LinkedList(1)
my_linked_list5.append(2)
my_linked_list5.append(3)
my_linked_list5.append(4)

my_linked_list5.print_list()
my_linked_list5.reverse()
print('Reversed linked list')
my_linked_list5.print_list()

# my_linked_list4 = LinkedList(0)
# my_linked_list4.append(2)

# my_linked_list4.insert(1,1)
# my_linked_list4.print_list()

# print(my_linked_list4.remove(2))
# my_linked_list4.print_list()
# my_linked_list3 = LinkedList(0)
# my_linked_list3.append(1)
# my_linked_list3.append(2)
# my_linked_list3.append(3)
# node = my_linked_list3.get(2)
# if node:
#     print("Value at index 2:", node.value)
# else:
#     print("Index 2 is out of bounds")
# print(my_linked_list3.get(2))
# my_linked_list3.set(1, 4)


# print("Updated list:")
# my_linked_list3.print_list()

# my_linked_list = LinkedList(2)
# my_linked_list.append(3)

# print('Before prepend():')
# print('----------------')
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length, '\n')
# print('Linked List:')
# my_linked_list.print_list()


# my_linked_list.prepend(1)


# print('\n\nAfter prepend():')
# print('---------------')
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length, '\n')
# print('Linked List:')
# my_linked_list.print_list()



# """
#     EXPECTED OUTPUT:
    
#     Before prepend():
#     ----------------
#     Head: 2
#     Tail: 3
#     Length: 2 

#     Linked List:
#     2
#     3


#     After prepend():
#     ---------------
#     Head: 1
#     Tail: 3
#     Length: 3 

#     Linked List:
#     1
#     2
#     3   

# """

# my_linked_list2 = LinkedList(2)
# my_linked_list2.append(1)
# # (2) Items - Returns 2 Node
# print(my_linked_list2.pop_first().value)
# # (1) Item -  Returns 1 Node
# print(my_linked_list2.pop_first().value)
# # (0) Items - Returns None
# print(my_linked_list2.pop_first())


# """
#     EXPECTED OUTPUT:
#     ----------------
#     2
#     1
#     None

# """