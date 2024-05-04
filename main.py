import tkinter as tk
import backend as bc


bg_color = "#8E7AB5"


window = tk.Tk()
window.title('Project BDD')
# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()
width = 700
height = 700
print(window.winfo_screenheight())
window.geometry(f'{width}x{height}')
window.configure(bg=bg_color)



def start_mongo():

    # Page 1
    frame_1 = tk.Frame(window, bg=bg_color)
    label_1 = tk.Label(frame_1, text="Welcome to Mongo Part", bg=bg_color, font=("Arial", 26, "bold"), fg='#EEA5A6')
    label_1.grid(row=0, column=0, pady=30)
    label_2 = tk.Label(frame_1, text="Comments", bg=bg_color, font=("Arial", 20, "bold"), fg='white')
    label_2.grid(row=1, column=0, padx=20)

    # 1 - Displaying all comments (Get)
    comments = bc.getComments()
    k = 2
    for c in comments:
        text = f"Comment Number {c['commentID']} -- {c['date']} -- {c['comment']} "
        label = tk.Label(frame_1, text=text, bg=bg_color, font=("Arial", 14), fg='white', justify="left")
        label.grid(row=k, column=0, pady=10, sticky='w')
        k += 1
    frame_1.pack()
    def manipulate():
        frame = tk.Frame(window, bg=bg_color)
        frame_1.destroy()
        CRUD(frame, k+1)

    b1 = tk.Button(frame_1, text = "Manipulataion", font=("Arial", 12),bg='#FDF0D1' ,command=manipulate)
    b1.grid(row=k+4, column=0, pady=5)





def CRUD(frame_1,k) :
    label = tk.Label(frame_1, text = "Manipulation",  bg=bg_color, font=("Arial", 26, "bold"), fg='white')
    label.grid(row=k-1, column=1,pady=20)
    # 2 - Add a comment (Post)
    label_3 = tk.Label(frame_1, text = "Add new comment",  bg=bg_color, font=("Arial", 14, "bold"), fg='white')
    label_3.grid(row=k, column=1, padx=20,pady=20)
    # Comment_ID
    label_4 = tk.Label(frame_1, text = "Comment ID",  bg=bg_color, font=("Arial", 10), fg='white')
    label_4.grid(row=k+1, column=0, sticky='w',pady=5)
    label_ID = tk.Entry(frame_1)
    label_ID.grid(row=k+1, column=1, pady=5)
    # Comment
    label_5 = tk.Label(frame_1, text = "Comment",  bg=bg_color, font=("Arial", 10), fg='white')
    label_5.grid(row=k+2, column=0,sticky='w',pady=5)
    label_COM = tk.Text(frame_1, height = 4, width = 20)
    label_COM.grid(row=k+2, column=1, pady=5)
    # Function 01
    def add():
        data = []
        data.append(int(label_ID.get()))
        data.append(label_COM.get("1.0", tk.END).strip())
        print(data)
        bc.addComment(data[0], data[1])
        label_ID.delete(0, tk.END)
        label_COM.delete("1.0", tk.END)
        frame_1.destroy()
        start_mongo()
    # Add button
    b1 = tk.Button(frame_1, text = "Add", command=add)
    b1.grid(row=k+3, column=1, pady=10)

    # 3 - Update a comment (Put)
    label_6 = tk.Label(frame_1, text = "Update comment",  bg=bg_color, font=("Arial", 14, "bold"), fg='white')
    label_6.grid(row=k+4, column=1, padx=20,pady=5)
    # Comment_ID
    label_7 = tk.Label(frame_1, text = "Comment ID",  bg=bg_color, font=("Arial", 10), fg='white')
    label_7.grid(row=k+5, column=0, sticky='w',pady=5)
    label_ID_Up = tk.Entry(frame_1)
    label_ID_Up.grid(row=k+5, column=1, pady=5)
    # Comment
    label_8 = tk.Label(frame_1, text = "Comment",  bg=bg_color, font=("Arial", 10), fg='white')
    label_8.grid(row=k+6, column=0, sticky='w',pady=5)
    label_COM_Up = tk.Text(frame_1, height = 4, width = 20)
    label_COM_Up.grid(row=k+6, column=1, pady=5)
    # Function 02
    def update():
        data = []
        data.append(int(label_ID_Up.get()))
        data.append(label_COM_Up.get("1.0", tk.END).strip())
        print(data)
        bc.updateComment(data[0], data[1])
        label_ID_Up.delete(0, tk.END)
        label_COM_Up.delete("1.0", tk.END)
        frame_1.destroy()
        start_mongo()
    # Update button
    b2 = tk.Button(frame_1, text = "Update", command=update)
    b2.grid(row=k+7, column=1, pady=5)


    # 4 - Delete a comment (Delete)
    label_9 = tk.Label(frame_1, text = "Delete comment",  bg=bg_color, font=("Arial", 14, "bold"), fg='white')
    label_9.grid(row=k+8, column=1, padx=20,pady=5)
    # Comment_ID
    label_10 = tk.Label(frame_1, text = "Comment ID",  bg=bg_color, font=("Arial", 10), fg='white')
    label_10.grid(row=k+9, column=0, sticky='w',pady=5)
    label_ID_Del = tk.Entry(frame_1)
    label_ID_Del.grid(row=k+9, column=1, pady=5)
    # Function 03
    def delete():
        data = int(label_ID_Del.get())
        print(data)
        bc.deleteComment(data)
        label_ID_Del.delete(0, tk.END)
        frame_1.destroy()
        start_mongo()
    # Delete button
    b3 = tk.Button(frame_1, text = "Delete", command=delete)
    b3.grid(row=k+10, column=1, pady=5)

    frame_1.pack()
    def start_mysql_Fun(): 
        frame_1.destroy()
        start_mysql(window)

    # Page 2
    b4 = tk.Button(frame_1, text = "MySQL Part", command=start_mysql_Fun)
    b4.grid(row=k+11, column=1, pady=5)

    def cancel():
        frame_1.destroy()
        start_mongo()

    b5 = tk.Button(frame_1, text = "Cancel", command=cancel)
    b5.grid(row=k+12, column=1, pady=5)



def start_mysql(window):
    # Page 2
    frame_2 = tk.Frame(window, bg=bg_color)
    label_1 = tk.Label(frame_2, text="Welcome to Mysql Part", bg=bg_color, font=("Arial", 26, "bold"), fg='#EEA5A6')
    label_1.grid(row=0, column=0, padx=20,pady=20)
    label_2 = tk.Label(frame_2, text="Users", bg=bg_color, font=("Arial", 14, "bold"), fg='white')
    label_2.grid(row=1, column=0, padx=20, pady=10)

    # 1 - Displaying all comments (Get)
    users = bc.getUsers()
    k = 2
    for u in users:
        text = f"User Id {u[0]} -- Name : {u[1]} -- Email : {u[2]}"
        label = tk.Label(frame_2, text=text, bg=bg_color, font=("Arial", 10), fg='white')
        label.grid(row=k, column=0, sticky='w', pady=10)
        k += 1
    frame_2.pack()
    def manipulate():
        frame = tk.Frame(window, bg=bg_color)
        frame_2.destroy()
        CRUD_mysql(frame, k+1)

    b1 = tk.Button(frame_2, text = "Manipulataion", font=("Arial", 12),bg='#FDF0D1' ,command=manipulate)
    b1.grid(row=k+4, column=0, pady=5)



def CRUD_mysql(frame_2, k):
    label = tk.Label(frame_2, text = "Manipulation",  bg=bg_color, font=("Arial", 26, "bold"), fg='white')
    label.grid(row=k-1, column=1,pady=20)
    # 2 - Add a User (Post)
    label_3 = tk.Label(frame_2, text = "Add new user",  bg=bg_color, font=("Arial", 14, "bold"), fg='white')
    label_3.grid(row=k, column=1, padx=20,pady=10)
    # Name
    label_4 = tk.Label(frame_2, text = "Name",  bg=bg_color, font=("Arial", 10), fg='white')
    label_4.grid(row=k+1, column=0, sticky='w',pady=5)
    label_Name = tk.Entry(frame_2)
    label_Name.grid(row=k+1, column=1, pady=5)
    # Email
    label_5 = tk.Label(frame_2, text = "Email",  bg=bg_color, font=("Arial", 10), fg='white')
    label_5.grid(row=k+2, column=0, sticky='w',pady=5)
    label_Em = tk.Entry(frame_2)
    label_Em.grid(row=k+2, column=1, pady=5)
    # Password
    label_6 = tk.Label(frame_2, text = "Password",  bg=bg_color, font=("Arial", 10), fg='white')
    label_6.grid(row=k+3, column=0, sticky='w',pady=5)
    label_PW = tk.Entry(frame_2)
    label_PW.grid(row=k+3, column=1, pady=5)
    # Function 01
    def add():
        data = []
        data.append(label_Name.get())
        data.append(label_Em.get())
        data.append(label_PW.get())
        print(data)
        bc.addUser(data[0], data[1], data[2])
        label_Name.delete(0, tk.END)
        label_Em.delete(0, tk.END)
        label_PW.delete(0, tk.END)

        frame_2.destroy()
        start_mysql(window)
    # Add button
    b1 = tk.Button(frame_2, text = "Add", command=add)
    b1.grid(row=k+4, column=1, pady=10)

    # 3 - Update a user (Put)
    label_6 = tk.Label(frame_2, text = "Update user",  bg=bg_color, font=("Arial", 14, "bold"), fg='white')
    label_6.grid(row=k+5, column=1, padx=20,pady=5)
    # Name
    label_7 = tk.Label(frame_2, text = "Name",  bg=bg_color, font=("Arial", 10), fg='white')
    label_7.grid(row=k+6, column=0, sticky='w',pady=5)
    label_Name_Up = tk.Entry(frame_2)
    label_Name_Up.grid(row=k+6, column=1, pady=5)
    # Email
    label_8 = tk.Label(frame_2, text = "Email",  bg=bg_color, font=("Arial", 10), fg='white')
    label_8.grid(row=k+7, column=0,sticky='w',pady=5)
    label_Email_Up = tk.Entry(frame_2)
    label_Email_Up.grid(row=k+7, column=1, pady=5)
    # Password
    label_8 = tk.Label(frame_2, text = "Password",  bg=bg_color, font=("Arial", 10), fg='white')
    label_8.grid(row=k+8, column=0,sticky='w',pady=5)
    label_PW_Up = tk.Entry(frame_2)
    label_PW_Up.grid(row=k+8, column=1, pady=5)
    # Function 02
    def update():
        data = []
        data.append(label_Name_Up.get())
        data.append(label_Email_Up.get())
        data.append(label_PW_Up.get())
        print(data)
        bc.updateUser(data[0], data[1], data[2])
        label_Name_Up.delete(0, tk.END)
        label_Email_Up.delete(0, tk.END)
        label_PW_Up.delete(0, tk.END)
        frame_2.destroy()
        start_mysql(window)
    # Update button
    b2 = tk.Button(frame_2, text = "Update", command=update)
    b2.grid(row=k+9, column=1, pady=5)


    # 4 - Delete user (Delete)
    label_9 = tk.Label(frame_2, text = "Delete user",  bg=bg_color, font=("Arial", 14, "bold"), fg='white')
    label_9.grid(row=k+10, column=1, padx=20,pady=5)
    # Name
    label_10 = tk.Label(frame_2, text = "Name",  bg=bg_color, font=("Arial", 10), fg='white')
    label_10.grid(row=k+11, column=0, padx=20,pady=5)
    label_Name_Del = tk.Entry(frame_2)
    label_Name_Del.grid(row=k+11, column=1, pady=5)
    # Function 03
    def delete():
        data = label_Name_Del.get()
        print(data)
        bc.deleteUser(data)
        label_Name_Del.delete(0, tk.END)
        frame_2.destroy()
        start_mysql(window)
    # Delete button
    b3 = tk.Button(frame_2, text = "Delete", command=delete)
    b3.grid(row=k+12, column=1, pady=5)

    frame_2.pack()
    # Page 1
    def start_mongo_Fun():
        frame_2.destroy()
        start_mongo()

    b4 = tk.Button(frame_2, text = "Mongo Part", command=start_mongo_Fun)
    b4.grid(row=k+13, column=1, pady=5)

    def cancel():
        frame_2.destroy()
        start_mysql(window)

    b5 = tk.Button(frame_2, text = "Cancel", command=cancel)
    b5.grid(row=k+14, column=1, pady=5)



start_mongo()



window.mainloop()



