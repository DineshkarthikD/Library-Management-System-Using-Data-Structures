import tkinter as tk
from linked_list import LinkedList
from book import Book

from file_handler import save_books, load_books

library = load_books()

def add_book(book_id_entry, book_name_entry, author_entry, quantity_entry):

    book_id = book_id_entry.get()
    title = book_name_entry.get()
    author = author_entry.get()
    quantity = quantity_entry.get()

    if not book_id or not title or not author or not quantity:
        print("Please fill all fields.")
        return

    if library.book_exists(book_id):

        messagebox.showerror(
            "Duplicate Book ID",
            "Book ID already exists."
        )

        return
    
    if not book_id or not title or not author or not quantity:

        messagebox.showerror(
            "Input Error",
            "Please fill all fields."
        )

        return
    
    if not quantity.isdigit():

        messagebox.showerror(
            "Input Error",
            "Quantity must contain only numbers."
        )

        return
    
    if int(quantity) <= 0:

        messagebox.showerror(
            "Input Error",
            "Quantity must be greater than zero."
        )

        return
    
    if " " in book_id:

        messagebox.showerror(
            "Input Error",
            "Book ID cannot contain spaces."
        )

        return
    
    book = Book(book_id, title, author, quantity)

    library.insert(book)
    save_books(library)

    print("Book Added Successfully!")

    library.display()

    book_id_entry.delete(0, tk.END)
    book_name_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def view_books(output_box):

    output_box.delete(1.0, tk.END)

    current = library.head

    while current:

        book = current.book

        output_box.insert(
            tk.END,
            f"Book ID : {book.book_id}\n"
        )

        output_box.insert(
            tk.END,
            f"Title : {book.title}\n"
        )

        output_box.insert(
            tk.END,
            f"Author : {book.author}\n"
        )

        output_box.insert(
            tk.END,
            f"Quantity : {book.quantity}\n"
        )

        output_box.insert(
            tk.END,
            "-"*40 + "\n"
        )

        current = current.next

from tkinter import messagebox

def search_book(book_id_entry):

    book_id = book_id_entry.get()

    book = library.search(book_id)

    if book:

        messagebox.showinfo(
            "Book Found",
            f"Book ID : {book.book_id}\n"
            f"Title : {book.title}\n"
            f"Author : {book.author}\n"
            f"Quantity : {book.quantity}"
        )

    else:

        messagebox.showerror(
            "Not Found",
            "Book not found."
        )

from tkinter import messagebox

def delete_book(book_id_entry):

    book_id = book_id_entry.get()

    if library.delete(book_id):

        messagebox.showinfo(
            "Success",
            "Book deleted successfully."
        )
        save_books(library)

        book_id_entry.delete(0, tk.END)

    else:

        messagebox.showerror(
            "Error",
            "Book not found."
        )

def update_book(book_id_entry, book_name_entry, author_entry, quantity_entry):

    book_id = book_id_entry.get()
    title = book_name_entry.get()
    author = author_entry.get()
    quantity = quantity_entry.get()

    success = library.update(
        book_id,
        title,
        author,
        quantity
    )

    if success:

        messagebox.showinfo(
            "Success",
            "Book updated successfully."
        )
        save_books(library)

    else:

        messagebox.showerror(
            "Error",
            "Book not found."
        )

def open_book_management(root):

    book_window = tk.Toplevel(root)

    book_window.title("Book Management")

    book_window.geometry("700x550")

    book_window.configure(bg="#f5f5f5")

    # =========================
    # Heading
    # =========================

    heading = tk.Label(
        book_window,
        text="📚 Book Management",
        font=("Arial",20,"bold"),
        bg="#f5f5f5"
    )

    heading.pack(pady=15)

    # =========================
    # Form Frame
    # =========================

    form_frame = tk.Frame(book_window,bg="#f5f5f5")

    form_frame.pack(pady=20)

    # Book ID

    tk.Label(
        form_frame,
        text="Book ID",
        bg="#f5f5f5",
        font=("Arial",12)
    ).grid(row=0,column=0,padx=10,pady=10,sticky="w")

    book_id = tk.Entry(form_frame,width=30)

    book_id.grid(row=0,column=1,padx=10,pady=10)

    # Book Name

    tk.Label(
        form_frame,
        text="Book Name",
        bg="#f5f5f5",
        font=("Arial",12)
    ).grid(row=1,column=0,padx=10,pady=10,sticky="w")

    book_name = tk.Entry(form_frame,width=30)

    book_name.grid(row=1,column=1,padx=10,pady=10)

    # Author

    tk.Label(
        form_frame,
        text="Author",
        bg="#f5f5f5",
        font=("Arial",12)
    ).grid(row=2,column=0,padx=10,pady=10,sticky="w")

    author = tk.Entry(form_frame,width=30)

    author.grid(row=2,column=1,padx=10,pady=10)

    # Quantity

    tk.Label(
        form_frame,
        text="Quantity",
        bg="#f5f5f5",
        font=("Arial",12)
    ).grid(row=3,column=0,padx=10,pady=10,sticky="w")

    quantity = tk.Entry(form_frame,width=30)

    quantity.grid(row=3,column=1,padx=10,pady=10)

    # =========================
    # Buttons
    # =========================

    button_frame = tk.Frame(book_window,bg="#f5f5f5")

    button_frame.pack(pady=20)

    tk.Button(
        button_frame,
        text="Add Book",
        width=15,
        command=lambda: add_book(
            book_id,
            book_name,
            author,
            quantity
        )
    ).grid(row=0, column=0, padx=5, pady=5)

    tk.Button(
        button_frame,
        text="Update Book",
        width=15,
        command=lambda: update_book(
            book_id,
            book_name,
            author,
            quantity
        )
    ).grid(
        row=0,
        column=1,
        padx=5,
        pady=5
)

    tk.Button(
        button_frame,
        text="Delete Book",
        width=15,
        command=lambda: delete_book(book_id)
    ).grid(
        row=1,
        column=0,
        padx=5,
        pady=5
)

    tk.Button(
        button_frame,
        text="Search Book",
        width=15,
        command=lambda: search_book(book_id)
    ).grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )

    tk.Button(
        button_frame,
        text="View Books",
        width=32,
        command=lambda:view_books(output_box)
    ).grid(
        row=2,
        column=0,
        columnspan=2,
        pady=10
    )
    output_box = tk.Text(
        book_window,
        width=60,
        height=12
    )

    output_box.pack(pady=15)

def get_book(book_id):

    return library.search(book_id)