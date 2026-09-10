class StackNode:

    def __init__(self, transaction):

        self.transaction = transaction
        self.next = None

class Stack:

    def __init__(self):

        self.top = None

    def push(self, transaction):

        new_node = StackNode(transaction)

        new_node.next = self.top

        self.top = new_node
    
    def pop(self):

        if self.top is None:

            return None

        transaction = self.top.transaction

        self.top = self.top.next

        return transaction
    
    def display(self):

        current = self.top

        while current:

            print(current.transaction)

            current = current.next