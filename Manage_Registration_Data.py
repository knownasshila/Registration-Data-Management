from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class student:
    def __init__(self, root):

        self.root = root

        self.root.geometry("1370x700+0+0")
        self.root.title("Data Management System")
        Label(self.root, text=" Registration Data Management", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), fg="#ffff66",
              bg="#17823b").pack(side=TOP, fill=X)



        self.id = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.status = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        


        # ========================1stframe=======================
        manage_frame = Frame(self.root, bg="#2c2727", relief=RIDGE, bd=4)
        manage_frame.place(x=20, y=100, width=530, height=585)
        Label(manage_frame, text="Registration Data", font=("times new roman", 40, "bold"), bg="#2c2727",
              fg="white").grid(row=0, columnspan=2, pady=20)

        id = Label(manage_frame, text=" Student ID", font=("times new roman", 20, "bold"), bg="#2c2727", fg="white")
        id.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_id = Entry(manage_frame, textvariable=self.id, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        txt_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        name = Label(manage_frame, text=" Student Name", font=("times new roman", 20, "bold"), bg="#2c2727", fg="white")
        name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(manage_frame, textvariable=self.name, font=("times new roman", 12, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        mail = Label(manage_frame, text=" Email ", font=("times new roman", 20, "bold"), bg="#2c2727", fg="white")
        mail.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_mail = Entry(manage_frame, textvariable=self.email, font=("times new roman", 12, "bold"), bd=5,
                         relief=GROOVE)
        txt_mail.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        course = Label(manage_frame, text="List of Courses", font=("times new roman", 20, "bold"), bg="#2c2727",
                       fg="white")
        course.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        self.txt_course = Text(manage_frame, font=("times new roman", 10, "bold"), width=30, height=6)
        self.txt_course.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        status = Label(manage_frame, text="Registration Status", font=("times new roman", 20, "bold"), bg="#2c2727",
                       fg="white")
        status.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        combo_status = ttk.Combobox(manage_frame, textvariable=self.status, font=("times new roman", 13, "bold"),
                                    state='readonly')
        combo_status['values'] = ("Pending", "Partially Complete", "Complete")
        combo_status.grid(row=5, column=1, pady=10, padx=20)




        # ========Button=================================
        btn_frame = Frame(manage_frame, bg="black", relief=RIDGE, bd=3)
        btn_frame.place(x=20, y=480, width=480)

        addbtn = Button(btn_frame, text="Add", width=10, command=self.add_student)
        addbtn.grid(row=0, column=0, padx=18, pady=16)
        updatebtn = Button(btn_frame, text="Update", width=10, command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=18, pady=16)
        deletebtn = Button(btn_frame, text="Delete", width=10, command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=18, pady=16)
        clearbtn = Button(btn_frame, text="Clear", width=10, command=self.clear)
        clearbtn.grid(row=0, column=3, padx=18, pady=16)




        # ==========2ndframe======================================
        detail_frame = Frame(self.root, bg="#2c2727", relief=RIDGE, bd=4)
        detail_frame.place(x=560, y=100, width=780, height=585)

        search = Label(detail_frame, text=" Search by", font=("times new roman", 20, "bold"), bg="#2c2727", fg="white")
        search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        combo_search = ttk.Combobox(detail_frame, textvariable=self.search_by,font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("id")
        combo_search.grid(row=0, column=1, pady=10, padx=10)

        txt_search = Entry(detail_frame, textvariable=self.search_txt,font=("times new roman", 10, "bold"), width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(detail_frame, text="Search", width=10, pady=5,command=self.search)
        searchbtn.grid(row=0, column=3, padx=8, pady=8)
        showbtn = Button(detail_frame, text="Show All", width=10, pady=5,command=self.fetch_data)
        showbtn.grid(row=0, column=4, padx=8, pady=8)



        # =======tableframe=============================
        table_frame = Frame(detail_frame, bg="white", relief=RIDGE, bd=4)
        table_frame.place(x=10, y=70, width=760, height=500)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("id", "name", "email", "courses", "status"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("courses", text="List of Couses")
        self.student_table.heading("status", text="Registration Status")

        self.student_table['show'] = 'headings'
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("courses", width=200)
        self.student_table.column("status", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    def add_student(self):
        if self.id.get()=="" or self.name.get()=="":
            messagebox.showerror("Error","Fields are required!")
            
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="sms3")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s)", (self.id.get(),
                                                                    self.name.get(),
                                                                    self.email.get(),

                                                                    self.txt_course.get("1.0", END),
                                                                    self.status.get()

                                                                    ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Info","Data Added")



    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms3")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()



    def clear(self):
        self.id.set("")
        self.name.set("")
        self.email.set("")
        self.txt_course.delete("1.0", END)
        self.status.set("")


    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']

        self.id.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.txt_course.delete("1.0", END)
        self.txt_course.insert(END, row[3])
        self.status.set(row[4])



    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms3")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,courses=%s,status=%s where id=%s", (
            self.name.get(),
            self.email.get(),
            self.txt_course.get("1.0", END),
            self.status.get(),
            self.id.get()

        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Info","Data Updated")



    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms3")
        cur = con.cursor()
        cur.execute("delete from students where id=%s", self.id.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Info","Data Deleted")



    def search(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms3")
        cur=con.cursor()
        cur.execute("select * from students where id  LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:

                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


root = Tk()
obj = student(root)
root.mainloop()