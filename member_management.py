import tkinter as tk
from tkinter import messagebox

from linked_list import LinkedList
from member import Member

from file_handler import save_members, load_members

member_library = load_members()

def add_member(member_id_entry, member_name_entry, phone_entry, email_entry):

    member_id = member_id_entry.get()
    name = member_name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if not member_id or not name or not phone or not email:

        messagebox.showerror(
            "Input Error",
            "Please fill all fields."
        )

        return

    member = Member(
        member_id,
        name,
        phone,
        email
    )

    member_library.insert(member)
    save_members(member_library)

    messagebox.showinfo(
        "Success",
        "Member Added Successfully!"
    )

    member_id_entry.delete(0, tk.END)
    member_name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def view_members(output_box):

    output_box.delete(1.0, tk.END)

    current = member_library.head

    while current:

        member = current.book

        output_box.insert(
            tk.END,
            f"Member ID : {member.member_id}\n"
        )

        output_box.insert(
            tk.END,
            f"Name : {member.name}\n"
        )

        output_box.insert(
            tk.END,
            f"Phone : {member.phone}\n"
        )

        output_box.insert(
            tk.END,
            f"Email : {member.email}\n"
        )

        output_box.insert(
            tk.END,
            "-" * 40 + "\n"
        )

        current = current.next

def search_member(member_id_entry):

    member_id = member_id_entry.get()

    member = member_library.search_member(member_id)

    if member:

        messagebox.showinfo(
            "Member Found",
            f"Member ID : {member.member_id}\n"
            f"Name : {member.name}\n"
            f"Phone : {member.phone}\n"
            f"Email : {member.email}"
        )

    else:

        messagebox.showerror(
            "Not Found",
            "Member not found."
        )

def update_member(member_id_entry, member_name_entry, phone_entry, email_entry):

    member_id = member_id_entry.get()
    name = member_name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    success = member_library.update_member(
        member_id,
        name,
        phone,
        email
    )

    if success:

        messagebox.showinfo(
            "Success",
            "Member updated successfully."
        )
        save_members(member_library)

    else:

        messagebox.showerror(
            "Error",
            "Member not found."
        )

def delete_member(member_id_entry):

    member_id = member_id_entry.get()

    success = member_library.delete_member(member_id)

    if success:

        messagebox.showinfo(
            "Success",
            "Member deleted successfully."
        )
        save_members(member_library)

        member_id_entry.delete(0, tk.END)

    else:

        messagebox.showerror(
            "Error",
            "Member not found."
        )

def open_member_management(root):

    member_window = tk.Toplevel(root)

    member_window.title("Member Management")
    member_window.geometry("700x550")
    member_window.configure(bg="#f5f5f5")
    member_window.resizable(False, False)

    # ==========================
    # Heading
    # ==========================

    heading = tk.Label(
        member_window,
        text="👤 Member Management",
        font=("Arial", 20, "bold"),
        bg="#f5f5f5"
    )

    heading.pack(pady=15)

    # ==========================
    # Form Frame
    # ==========================

    form_frame = tk.Frame(member_window, bg="#f5f5f5")
    form_frame.pack(pady=20)

    # Member ID

    tk.Label(
        form_frame,
        text="Member ID",
        font=("Arial", 12),
        bg="#f5f5f5"
    ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

    member_id = tk.Entry(form_frame, width=30)
    member_id.grid(row=0, column=1, padx=10, pady=10)

    # Member Name

    tk.Label(
        form_frame,
        text="Member Name",
        font=("Arial", 12),
        bg="#f5f5f5"
    ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

    member_name = tk.Entry(form_frame, width=30)
    member_name.grid(row=1, column=1, padx=10, pady=10)

    # Phone Number

    tk.Label(
        form_frame,
        text="Phone Number",
        font=("Arial", 12),
        bg="#f5f5f5"
    ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

    phone = tk.Entry(form_frame, width=30)
    phone.grid(row=2, column=1, padx=10, pady=10)

    # Email

    tk.Label(
        form_frame,
        text="Email",
        font=("Arial", 12),
        bg="#f5f5f5"
    ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

    email = tk.Entry(form_frame, width=30)
    email.grid(row=3, column=1, padx=10, pady=10)

    # ==========================
    # Buttons
    # ==========================

    button_frame = tk.Frame(member_window, bg="#f5f5f5")
    button_frame.pack(pady=20)

    tk.Button(
        button_frame,
        text="Add Member",
        width=15,
        command=lambda: add_member(
            member_id,
            member_name,
            phone,
            email
        )
    ).grid(
        row=0,
        column=0,
        padx=5,
        pady=5
    )

    tk.Button(
        button_frame,
        text="Update Member",
        width=15,
        command=lambda: update_member(
            member_id,
            member_name,
            phone,
            email
        )
    ).grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )

    tk.Button(
        button_frame,
        text="Delete Member",
        width=15,
        command=lambda: delete_member(member_id)
    ).grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )
    
    tk.Button(
        button_frame,
        text="Search Member",
        width=15,
        command=lambda: search_member(member_id)
    ).grid(
        row=1,
        column=1,
        padx=5,
        pady=5
)
    
    tk.Button(
        button_frame,
        text="View Members",
        width=32,
        command=lambda: view_members(output_box)
    ).grid(
        row=2,
        column=0,
        columnspan=2,
        pady=10
    )

    output_box = tk.Text(
        member_window,
        width=60,
        height=12
    )

    output_box.pack(pady=15)

def get_member(member_id):

    return member_library.search_member(member_id)