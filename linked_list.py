class Node:

    def __init__(self, book):

        self.book = book

        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None
    
    def insert(self, book):

        new_node = Node(book)

    # If list is empty
        if self.head is None:
            self.head = new_node
            return

    # Traverse to the last node
        current = self.head

        while current.next is not None:
            current = current.next

    # Insert at the end
        current.next = new_node
    
    def display(self):

        current = self.head

        while current is not None:
            print(f"Book ID : {current.book.book_id}")
            print(f"Title   : {current.book.title}")
            print(f"Author  : {current.book.author}")
            print(f"Quantity: {current.book.quantity}")
            print("-" * 30)
            current = current.next

    def search(self, book_id):

        current = self.head

        while current is not None:

            if current.book.book_id == book_id:
                return current.book

            current = current.next

        return None
    
    def delete(self, book_id):

    # If list is empty
        if self.head is None:
            return False

    # If first node is the one to delete
        if self.head.book.book_id == book_id:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next

        while current is not None:

            if current.book.book_id == book_id:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        return False
    
    def update(self, book_id, new_title, new_author, new_quantity):

        current = self.head

        while current is not None:

            if current.book.book_id == book_id:

                current.book.title = new_title
                current.book.author = new_author
                current.book.quantity = new_quantity

                return True

            current = current.next

        return False
    
    def book_exists(self, book_id):

        current = self.head

        while current is not None:

            if current.book.book_id == book_id:
                return True

            current = current.next

        return False
    
    def search_member(self, member_id):

        current = self.head

        while current:

            if current.book.member_id == member_id:
                return current.book

            current = current.next

        return None
    
    def update_member(self, member_id, new_name, new_phone, new_email):

        current = self.head

        while current:

            if current.book.member_id == member_id:

                current.book.name = new_name
                current.book.phone = new_phone
                current.book.email = new_email

                return True

            current = current.next

        return False
    
    def delete_member(self, member_id):

        if self.head is None:
            return False

        if self.head.book.member_id == member_id:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next

        while current:

            if current.book.member_id == member_id:

                previous.next = current.next

                return True

            previous = current
            current = current.next

        return False
    
    def search_issue(self, issue_id):

        current = self.head

        while current:

            if current.book.issue_id == issue_id:
                return current.book

            current = current.next

        return None
    
    def delete_issue(self, issue_id):

        if self.head is None:
            return False

        if self.head.book.issue_id == issue_id:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next

        while current:

            if current.book.issue_id == issue_id:

                previous.next = current.next

                return True

            previous = current
            current = current.next

        return False