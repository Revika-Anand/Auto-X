from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import switch_case as sc
import string
import random

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Auto-X")
        self.root.geometry("1250x650+0+0")         # defines size and coordinates of the window that will appear
        self.coord = list()
        self.number = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))

        #--------bg img---------
        self.bg = ImageTk.PhotoImage(file = "images/bg.jpg")
        bg = Label(self.root, image = self.bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
        #--------side img-------
        self.left = ImageTk.PhotoImage(file = "images/xray.jpg")
        left = Label(self.root, image = self.left).place(x = 150, y = 100, width = 400, height = 500)

        #---------frame--------
        frame1 = Frame(self.root, bg = "white")
        frame1.place(x = 550, y = 100, width = 550, height = 500)

        #--Title
        title = Label(frame1, text = "Registration Form", font = ("times new roman", 25, "bold"), bg = "white").place(x = 50, y = 30)
        text = Label(frame1, text = "Please enter the details of the patient", font = ("times new roman", 10), bg = "white").place(x = 52, y = 70)

        #--Name
        f_name = Label(frame1, text = "Name", font = ("times new roman", 15), bg = "white", fg="darkgray").place(x = 50, y = 100)
        self.txt_fname = Entry(frame1, font = ("times new roman", 15), bg = "lightgray")
        self.txt_fname.place(x = 50, y = 130, width = 200)

        p_no = Label(frame1, text = "Patient Number", font = ("times new roman", 15), bg = "white", fg="darkgray").place(x = 300, y = 100)
        self.txt_pno = Label(frame1, text = str(self.number), font = ("times new roman", 15), bg = "lightgray")
        self.txt_pno.place(x = 300, y = 130, width = 200)

        #--Contact
        contact = Label(frame1, text = "Contact No.", font = ("times new roman", 15), bg = "white", fg="darkgray").place(x = 50, y = 170)
        self.txt_contact = Entry(frame1, font = ("times new roman", 15), bg = "lightgray")
        self.txt_contact.place(x = 50, y = 200, width = 200)

        email = Label(frame1, text = "E-mail", font = ("times new roman", 15), bg = "white", fg="darkgray").place(x = 300, y = 170)
        self.txt_email = Entry(frame1, font = ("times new roman", 15), bg = "lightgray")
        self.txt_email.place(x = 300, y = 200, width = 200)

        #--Medical issue
        issue = Label(frame1, text = "Medical Issue", font = ("times new roman", 15), bg = "white", fg="darkgray").place(x = 50, y = 240)
        self.txt_issue = Entry(frame1, font = ("times new roman", 15), bg = "lightgray")
        self.txt_issue.place(x = 50, y = 270, width = 450)

        #--xray
        xray = Label(frame1, text = "X-ray required of...", font = ("times new roman", 15), bg = "white", fg="darkgray").place(x = 50, y = 310)
        self.drop_xray = ttk.Combobox(frame1, font = ("times new roman", 14), state = 'readonly')
        self.drop_xray['values'] = ("Select", "Teeth", "Chest", "Right Arm", "Left Arm", "Right Hand", "Left Hand", 
                                "Right Shoulder", "Left Shoulder", "Pelvis", "Right Thigh", "Left Thigh", "Right Leg", "Left Leg",
                                "Right Knee", "Left Knee", "Right Ankle", "Left Ankle", "Right Foot", "Left Foot")
        self.drop_xray.current(0)
        self.drop_xray.place(x = 50, y = 340, width = 450)      

        #--Submit
        self.btn_img = ImageTk.PhotoImage(file = "images/button.png")
        btn = Button(frame1, image = self.btn_img, bd = 0, cursor = "hand2", bg = "white", command = self.register_data).place(x = 200, y = 400)

    def register_data(self):
        if self.drop_xray.get() == "Select":
            messagebox.showerror("Error", "You must select the anatomy for X-ray.", parent = self.root)
        # elif len(self.txt_contact.get()) != 10:
        #     messagebox.showerror("Error", "Please enter a valid phone number", parent = self.root)
        else:
            messagebox.showinfo("Success", "Patient Information Recorded", parent = self.root)   
       
        self.coord = sc.body_coord(self.drop_xray.get())
        #print(self.coord)
      
           

# root = Tk()
# obj = Register(root)
# root.mainloop()