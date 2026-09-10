import tkinter as tk
from tkinter import messagebox

from linked_list import LinkedList
from issue import Issue
from queue_ds import Queue

from file_handler import save_issues, load_issues, save_books

from book_management import get_book, library
from member_management import get_member
from stack_ds import Stack

transaction_stack = Stack()

issue_library = load_issues()
waiting_queue = Queue()



def issue_book(issue_id_entry, book_id_entry, member_id_entry):

    issue_id = issue_id_entry.get().strip()
    book_id = book_id_entry.get().strip()
    member_id = member_id_entry.get().strip()

    # Check empty fields
    if not issue_id or not book_id or not member_id:

        messagebox.showerror(
            "Input Error",
            "Please fill all fields."
        )
        return

    # Search Book
    book = get_book(book_id)

    if book is None:

        messagebox.showerror(
            "Error",
            "Book not found."
        )
        return

    # Search Member
    member = get_member(member_id)

    if member is None:

        messagebox.showerror(
            "Error",
            "Member not found."
        )
        return

    # Check Quantity
    if int(book.quantity) <= 0:

        waiting_queue.enqueue(book_id, member_id)

        messagebox.showinfo(
            "Waiting List",
            "Book unavailable.\nMember added to waiting queue."
        )

        return

    # Reduce Quantity
    book.quantity = str(int(book.quantity) - 1)

    # Create Issue Object
    issue = Issue(
        issue_id,
        book_id,
        member_id
    )

    # Store Issue
    issue_library.insert(issue)

    transaction_stack.push(
        f"Issue | Issue ID: {issue_id} | Book: {book_id} | Member: {member_id}"
    )

    print("Top Transaction:")
    print(transaction_stack.top.transaction)

    # Save Files
    save_books(library)
    save_issues(issue_library)

    messagebox.showinfo(
        "Success",
        "Book Issued Successfully!"
    )

    # Clear Entry Boxes
    issue_id_entry.delete(0, tk.END)
    book_id_entry.delete(0, tk.END)
    member_id_entry.delete(0, tk.END)

def view_issued_books(output_box):

    output_box.delete(1.0, tk.END)

    current = issue_library.head

    while current:

        issue = current.book

        output_box.insert(
            tk.END,
            f"Issue ID : {issue.issue_id}\n"
        )

        output_box.insert(
            tk.END,
            f"Book ID : {issue.book_id}\n"
        )

        output_box.insert(
            tk.END,
            f"Member ID : {issue.member_id}\n"
        )

        output_box.insert(
            tk.END,
            "-" * 40 + "\n"
        )

        current = current.next

def return_book(issue_id_entry):

    issue_id = issue_id_entry.get().strip()

    issue = issue_library.search_issue(issue_id)

    if issue is None:

        messagebox.showerror(
            "Error",
            "Issue ID not found."
        )

        return

    # Find Book
    book = get_book(issue.book_id)

     # Delete Issue
    issue_library.delete_issue(issue_id)

    # Increase Quantity
    book.quantity = str(int(book.quantity) + 1)
    
    next_member = waiting_queue.dequeue_for_book(book.book_id)

    if next_member:

        new_issue = Issue(
            f"AUTO{len(str(issue_library.head))}",
            book.book_id,
            next_member
        )

        issue_library.insert(new_issue)

        book.quantity = str(int(book.quantity) - 1)

        transaction_stack.push(
            f"Auto Issue | Book: {book.book_id} | Member: {next_member}"
        )

        messagebox.showinfo(
            "Waiting Queue",
            f"Book automatically issued to Member {next_member}"
        )

   

    transaction_stack.push(
        f"Return | Issue ID: {issue_id} | Book: {book.book_id} | Member: {issue.member_id}"
    )

    # Save Files
    save_books(library)
    save_issues(issue_library)

    messagebox.showinfo(
        "Success",
        "Book Returned Successfully!"
    )

    issue_id_entry.delete(0, tk.END)

def open_issue_management(root):

    issue_window = tk.Toplevel(root)

    issue_window.title("Issue Book")

    issue_window.geometry("700x550")

    issue_window.configure(bg="#f5f5f5")

    issue_window.resizable(False, False)

    # Heading

    heading = tk.Label(
        issue_window,
        text="📖 Issue Book",
        font=("Arial",20,"bold"),
        bg="#f5f5f5"
    )

    heading.pack(pady=15)

    # Form

    form_frame = tk.Frame(issue_window,bg="#f5f5f5")

    form_frame.pack(pady=20)

    # Issue ID

    tk.Label(
        form_frame,
        text="Issue ID",
        bg="#f5f5f5",
        font=("Arial",12)
    ).grid(row=0,column=0,padx=10,pady=10,sticky="w")

    issue_id = tk.Entry(form_frame,width=30)

    issue_id.grid(row=0,column=1,padx=10,pady=10)

    # Book ID

    tk.Label(
        form_frame,
        text="Book ID",
        bg="#f5f5f5",
        font=("Arial",12)
    ).grid(row=1,column=0,padx=10,pady=10,sticky="w")

    book_id = tk.Entry(form_frame,width=30)

    book_id.grid(row=1,column=1,padx=10,pady=10)

    # Member ID

    tk.Label(
        form_frame,
        text="Member ID",
        bg="#f5f5f5",
        font=("Arial",12)
    ).grid(row=2,column=0,padx=10,pady=10,sticky="w")

    member_id = tk.Entry(form_frame,width=30)

    member_id.grid(row=2,column=1,padx=10,pady=10)

    # Buttons

    button_frame = tk.Frame(issue_window,bg="#f5f5f5")

    button_frame.pack(pady=20)

    tk.Button(
        button_frame,
        text="Issue Book",
        width=18,
        command=lambda: issue_book(
            issue_id,
            book_id,
            member_id
        )
    ).grid(
        row=0,
        column=0,
        padx=10
    )

    tk.Button(
        button_frame,
        text="View Issued Books",
        width=18,
        command=lambda: view_issued_books(output_box)
    ).grid(
        row=0,
        column=1,
        padx=10
    )

    tk.Button(
        button_frame,
        text="Return Book",
        width=18,
        command=lambda: return_book(issue_id)
    ).grid(
        row=1,
        column=0,
        pady=10
    )
    tk.Button(
        button_frame,
        text="View Transactions",
        width=18,
        command=lambda: view_transactions(output_box)
    ).grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    tk.Button(
        button_frame,
        text="View Waiting Queue",
        width=18,
        command=lambda: view_waiting_queue(output_box)
    ).grid(
        row=2,
        column=0,
        columnspan=2,
        pady=10
    )

    output_box = tk.Text(
        issue_window,
        width=60,
        height=12
    )

    output_box.pack(pady=15)

def view_transactions(output_box):

    output_box.delete(1.0, tk.END)

    current = transaction_stack.top

    while current:

        output_box.insert(
            tk.END,
            current.transaction + "\n"
        )

        output_box.insert(
            tk.END,
            "-" * 50 + "\n"
        )

        current = current.next

def view_waiting_queue(output_box):

    output_box.delete(1.0, tk.END)

    if waiting_queue.is_empty():

        output_box.insert(tk.END, "No members are waiting.\n")
        return

    current = waiting_queue.front

    while current:

        output_box.insert(
            tk.END,
            f"Book ID : {current.book_id}\n"
        )

        output_box.insert(
            tk.END,
            f"Member ID : {current.member_id}\n"
        )

        output_box.insert(
            tk.END,
            "-" * 40 + "\n"
        )

        current = current.next