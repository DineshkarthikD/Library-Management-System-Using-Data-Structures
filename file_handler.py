from book import Book


def save_books(linked_list):

    with open("books.txt", "w") as file:

        current = linked_list.head

        while current:

            book = current.book

            file.write(
                f"{book.book_id},"
                f"{book.title},"
                f"{book.author},"
                f"{book.quantity}\n"
            )

            current = current.next

from member import Member

def save_members(member_library):

    with open("members.txt", "w") as file:

        current = member_library.head

        while current:

            member = current.book

            file.write(
                f"{member.member_id},"
                f"{member.name},"
                f"{member.phone},"
                f"{member.email}\n"
            )

            current = current.next

from issue import Issue

def save_issues(issue_library):

    with open("issued_books.txt", "w") as file:

        current = issue_library.head

        while current:

            issue = current.book

            file.write(
                f"{issue.issue_id},"
                f"{issue.book_id},"
                f"{issue.member_id}\n"
            )

            current = current.next

from linked_list import LinkedList


def load_books():

    library = LinkedList()

    try:

        with open("books.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) == 4:

                    book = Book(
                        data[0],
                        data[1],
                        data[2],
                        data[3]
                    )

                    library.insert(book)

    except FileNotFoundError:

        pass

    return library

from linked_list import LinkedList

def load_members():

    member_library = LinkedList()

    try:

        with open("members.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) == 4:

                    member = Member(
                        data[0],
                        data[1],
                        data[2],
                        data[3]
                    )

                    member_library.insert(member)

    except FileNotFoundError:
        pass

    return member_library

def load_issues():

    library = LinkedList()

    try:

        with open("issued_books.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) == 3:

                    issue = Issue(
                        data[0],
                        data[1],
                        data[2]
                    )

                    library.insert(issue)

    except FileNotFoundError:
        pass

    return library