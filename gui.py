import tkinter as tk
from book_management import open_book_management
from member_management import open_member_management
from issue_management import open_issue_management
from book_management import library
from member_management import member_library
from issue_management import issue_library, waiting_queue

class LibraryGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Library Management System")
        self.root.geometry("900x720")
        self.root.configure(bg="#f5f5f5")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        heading = tk.Label(
            self.root,
            text="📚 Library Management System",
            font=("Arial",24,"bold"),
            bg="#f5f5f5",
            fg="#2c3e50"
        )

        heading.pack(pady=20)

        welcome = tk.Label(
            self.root,
            text="Welcome to Library Management System",
            font=("Arial",14),
            bg="#f5f5f5"
        )

        welcome.pack(pady=10)

        stats_frame = tk.Frame(
            self.root,
            bg="#ecf0f1",
            bd=2,
            relief="groove"
        )

        stats_frame.pack(pady=10)

        refresh_btn = tk.Button(
            self.root,
            text="🔄 Refresh Statistics",
            width=20,
            font=("Arial", 11, "bold"),
            command=self.refresh_statistics
        )

        refresh_btn.pack(pady=10)

        total_books, total_members, issued_books, available_books, waiting_members = self.get_statistics()

        self.stats_label = tk.Label(
            stats_frame,
            text=(
                f"📚 Total Books : {total_books}\n\n"
                f"👤 Total Members : {total_members}\n\n"
                f"📖 Issued Books : {issued_books}\n\n"
                f"📗 Available Books : {available_books}\n\n"
                f"⏳ Waiting Members : {waiting_members}"
            ),
            font=("Arial", 12),
            bg="#ecf0f1",
            justify="left"
        )

        self.stats_label.pack(padx=20, pady=15)

        button_frame = tk.Frame(self.root,bg="#f5f5f5")

        button_frame.pack(pady=20)

        book_btn = tk.Button(
            button_frame,
            text="📚 Book Management",
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            command=lambda: open_book_management(self.root)
        )

        book_btn.pack(pady=5)

        member_btn = tk.Button(
            button_frame,
            text="👤 Member Management",
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            command=lambda: open_member_management(self.root)
        )

        member_btn.pack(pady=5)

        issue_btn = tk.Button(
            button_frame,
            text="📖 Issue Management",
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            command=lambda: open_issue_management(self.root)
        )

        issue_btn.pack(pady=5)

        

        exit_btn = tk.Button(
            button_frame,
            text="🚪 Exit",
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            command=self.root.destroy
        )

        exit_btn.pack(pady=5)

    def count_nodes(self, head):

        count = 0

        current = head

        while current:

            count += 1
            current = current.next

        return count
    
    def get_statistics(self):

        total_books = self.count_nodes(library.head)

        total_members = self.count_nodes(member_library.head)

        issued_books = self.count_nodes(issue_library.head)

        available_books = 0

        current = library.head

        while current:

            available_books += int(current.book.quantity)

            current = current.next

        waiting_members = 0

        current = waiting_queue.front

        while current:

            waiting_members += 1

            current = current.next

        return (
            total_books,
            total_members,
            issued_books,
            available_books,
            waiting_members
        )
    
    def refresh_statistics(self):

        total_books, total_members, issued_books, available_books, waiting_members = self.get_statistics()

        self.stats_label.config(
            text=(
                f"📚 Total Books : {total_books}\n\n"
                f"👤 Total Members : {total_members}\n\n"
                f"📖 Issued Books : {issued_books}\n\n"
                f"📗 Available Books : {available_books}\n\n"
                f"⏳ Waiting Members : {waiting_members}"
            )
        )

    def run(self):
        self.root.mainloop()