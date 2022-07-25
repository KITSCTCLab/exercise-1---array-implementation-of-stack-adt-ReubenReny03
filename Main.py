import os
class Stack:
    """
    this is the main stack in which all are functions will be made
    functions:
        is_empty - to check if the stack is empty or not
        is_full - to ckeck if the stack is full or not
        push - to push the data into the stack
        pop - to pop the data from the stack
        status - to print the final elements left in the stack
    """
    def __init__(self, size):
        """
        this is to make the stack and initilise the size of the stack
        """
        self.items = []
        self.size = size

    def is_empty(self):
        """
        this is to ckeck if the stack is empty or not
        """
        if len(self.items) == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        this is to ckeck if the stack is full or not
        """
        if len(self.items) == self.size:
            return True
        else:
            return False

    def push(self, data):
        """
        used to push the data into the stack
        if the stack is not full then it will append the data to the stack
        """
        if not self.is_full():
            self.items.append(data)

    def pop(self):
        """
        used to pop the data from the stack
        if the stack is not empty then it will pop the last element added in the stack
        """
        if not self.is_empty():
            self.items.pop()

    def status(self):
        """
        it will print all the elements in the stack which remains
        """
        for elements in self.items:
            print(elements)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
