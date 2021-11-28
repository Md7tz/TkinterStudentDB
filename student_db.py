from tkinter import *
from tkinter import ttk


class StudentDB:
    headers = ['ID', 'First Name', 'Last Name', 'Email', 'Street',
               'City', 'State', 'Zip', 'Phone', 'Birth', 'Sex', 'Lunch']

    student_info = [
        (1, 'Dale', 'Cooper', 'dcooper@aol.com', '123 Main St', 'Yakima', 'WA', 98901,
         '792-223-8901', '1959-2-22', 'M', 3.50),
        (2, 'Harry', 'Truman', 'htruman@aol.com', '202 South St', 'Vancouver', 'WA', 98660,
         '792-223-9810', '1946-1-24', 'M', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50)
    ]

    def __init__(self):
        self.tree = None
        self.create_widgets()

    def create_widgets(self):
        # -- 1st Row -- #
        # ID
        sid_label = Label(root, text='ID')
        sid_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        self.sid_entry_value = StringVar(root, value="")
        self.sid_entry = ttk.Entry(root, textvariable=self.sid_entry_value)
        self.sid_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        # First name
        fname_label = Label(root, text='First Name')
        fname_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        self.fname_entry_value = StringVar(root, value="")
        self.fname_entry = ttk.Entry(root, textvariable=self.fname_entry_value)
        self.fname_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)
        # Last name
        lname_label = Label(root, text='Last Name')
        lname_label.grid(row=0, column=4, padx=5, pady=10, sticky=W)
        self.lname_entry_value = StringVar(root, value="")
        self.lname_entry = ttk.Entry(root, textvariable=self.lname_entry_value)
        self.lname_entry.grid(row=0, column=5, padx=5, pady=10, sticky=W)
        # Email
        email_label = Label(root, text='Email')
        email_label.grid(row=0, column=6, padx=5, pady=10, sticky=W)
        self.email_entry_value = StringVar(root, value="")
        self.email_entry = ttk.Entry(root, textvariable=self.email_entry_value)
        self.email_entry.grid(row=0, column=7, padx=5, pady=10, sticky=W)
        # Street
        street_label = Label(root, text='Street')
        street_label.grid(row=0, column=8, padx=5, pady=10, sticky=W)
        self.street_entry_value = StringVar(root, value="")
        self.street_entry = ttk.Entry(root, textvariable=self.street_entry_value)
        self.street_entry.grid(row=0, column=9, padx=5, pady=10, sticky=W)

        # -- 2nd Row -- #
        # City
        city_label = Label(root, text='City')
        city_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        self.city_entry_value = StringVar(root, value="")
        self.city_entry = ttk.Entry(root, textvariable=self.city_entry_value)
        self.city_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)
        # State
        state_label = Label(root, text='State')
        state_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        self.state_entry_value = StringVar(root, value="")
        self.state_entry = ttk.Entry(root, textvariable=self.state_entry_value)
        self.state_entry.grid(row=1, column=3, padx=5, pady=10, sticky=W)
        # Zipcode
        zip_label = Label(root, text='Zipcode')
        zip_label.grid(row=1, column=4, padx=5, pady=10, sticky=W)
        self.zip_entry_value = StringVar(root, value="")
        self.zip_entry = ttk.Entry(root, textvariable=self.zip_entry_value)
        self.zip_entry.grid(row=1, column=5, padx=5, pady=10, sticky=W)
        # Phone
        phone_label = Label(root, text='Phone')
        phone_label.grid(row=1, column=6, padx=5, pady=10, sticky=W)
        self.phone_entry_value = StringVar(root, value="")
        self.phone_entry = ttk.Entry(root, textvariable=self.phone_entry_value)
        self.phone_entry.grid(row=1, column=7, padx=5, pady=10, sticky=W)
        # Birth Date
        birth_label = Label(root, text='Birth Date')
        birth_label.grid(row=1, column=8, padx=5, pady=10, sticky=W)
        self.birth_entry_value = StringVar(root, value="")
        self.birth_entry = ttk.Entry(root, textvariable=self.birth_entry_value)
        self.birth_entry.grid(row=1, column=9, padx=5, pady=10, sticky=W)

        # -- 3rd Row -- #
        # Sex
        sex_label = Label(root, text='Sex')
        sex_label.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        self.sex_entry_value = StringVar(root, value="")
        self.sex_entry = ttk.Entry(root, textvariable=self.sex_entry_value)
        self.sex_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)
        # Lunch
        lunch_label = Label(root, text='Lunch Cost')
        lunch_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        self.lunch_entry_value = StringVar(root, value="")
        self.lunch_entry = ttk.Entry(root, textvariable=self.lunch_entry_value)
        self.lunch_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        # -- Buttons -- #

        add_button = ttk.Button(root, text='Add Student', command=self.add_student)
        add_button.grid(row=2, column=4, columnspan=2, padx = 10, sticky=(W, E))

        update_button = ttk.Button(root, text='Update Student', command=self.update_student)
        update_button.grid(row=2, column=6, columnspan=2, padx = 10, sticky=(W, E))

        delete_button = ttk.Button(root, text='Delete Student', command=self.delete_student)
        delete_button.grid(row=2, column=8, columnspan=2, padx = 10, sticky=(W, E))

        self.tree = ttk.Treeview(root, height=15, columns=self.headers, selectmode='browse', padding=9)
        self.tree.grid(row=3, column=0, columnspan=12)
        self.tree['show'] = 'headings'

        i = 1
        for col in self.headers:
            num = f'#{i}'
            self.tree.heading(num, text=col)
            self.tree.column(num, width=105)
            i += 1

        # i = 1
        for info in self.student_info:
            num = f'#{i}'
            self.tree.insert('', 'end', values=info)
            i += 1

    def add_student(self):
        pass

    def update_student(self):
        pass

    def delete_student(self):
        pass



if __name__ == '__main__':
    root = Tk()
    root.geometry("1280x600")
    root.title("Student Database")
    student_db = StudentDB()
    root.mainloop()
