class QueueNode:
    def __init__(self, book_id, member_id):

        self.book_id = book_id
        self.member_id = member_id
        self.next = None
        
class Queue:

    def __init__(self):

        self.front = None

        self.rear = None

    def enqueue(self, book_id, member_id):

        new_node = QueueNode(book_id, member_id)

        if self.rear is None:

            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node

        self.rear = new_node

    def dequeue(self):

        if self.front is None:

            return None

        member_id = self.front.member_id

        self.front = self.front.next

        if self.front is None:

            self.rear = None

        return member_id
    
    def display(self):

        if self.front is None:

            print("Queue is Empty")

            return

        current = self.front

        while current:

            print(current.member_id)

            current = current.next

    def is_empty(self):

        return self.front is None
    
    def dequeue_for_book(self, book_id):

        if self.front is None:
            return None

    # First node
        if self.front.book_id == book_id:

            member_id = self.front.member_id

            self.front = self.front.next

            if self.front is None:
                self.rear = None

            return member_id

        previous = self.front
        current = self.front.next

        while current:

            if current.book_id == book_id:

                member_id = current.member_id

                previous.next = current.next

                if current == self.rear:
                    self.rear = previous

                return member_id

            previous = current
            current = current.next

        return None