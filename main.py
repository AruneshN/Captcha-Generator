import tkinter as tk
from tkinter import*
from captcha.image import ImageCaptcha
from PIL import ImageTk,Image
import random
from tkinter import messagebox
import string

import phonenumbers

root=tk.Tk()
root.geometry("600x600+250+50")

# _______________________________________FRAME_______________________________________________
def generate_captcha():
    global img
    captcha_obj=ImageCaptcha(height=140,width=200)
    captcha_obj.write(chars=cap_ent.get(),output="_captcha.png")
    img=tk.PhotoImage(file="_captcha.png")
    captcha_lab.config(image=img)

    # while False:
    #     raise ZeroDivisionError(messagebox.showerror("log","check details"))
def auto():
    global rand_cap
    word = "abcdefghijklmnopqrstuvwxyz"
    WORDS=(word.upper())
    words=WORDS
    string = word + words
    leng = 6
    rand_cap = ''.join(random.sample(string, leng))
    global img
    captcha_obj = ImageCaptcha(height=140, width=200)
    captcha_obj.write(chars=rand_cap, output="_captcha.png")
    img = tk.PhotoImage(file="_captcha.png")
    captcha_lab.config(image=img)
    print(rand_cap)

frame=tk.Frame(root,highlightbackground="black",highlightthickness=3,bg="white")
frame.pack(pady=30)
frame.pack_propagate(False)
frame.configure(width=530,height=630)

captch_text=tk.Label(frame,text="Captcha Generator",bg="white",fg="blue",font=("times new roman",20,"bold")).place(x=165,y=10)
cap_ent=tk.Entry(frame,font=("bold",15),bd=2,highlightbackground="red",justify=tk.CENTER)
cap_ent.place(x=165,y=50)

enter=tk.Label(frame,text="Enter Correct Captcha",fg="blue",bg='white',font=("times new roman",20,"bold"))
enter.place(x=155,y=295)
ent=tk.Entry(frame,font=("bold",15),bd=2,highlightbackground="red",justify=tk.CENTER)
ent.place(x=155,y=350)

def sub():
    if rand_cap == ent.get():
        exp=tk.Label(frame,text="✔",bg="blue",fg="white",font=("times new roman",15,"bold"))
        exp.place(x=400,y=350)

    else:
        exp = tk.Label(frame, text="❌", bg="blue", fg="white", font=("times new roman", 15, "bold"))
        exp.place(x=400, y=350)


new=Image.open("C:\\Users\ELCOT\Desktop\py projects\Refresh-Transparent-Images.png")
resize=new.resize((30,30),Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resize)
ref=tk.PhotoImage(file="C:\\Users\ELCOT\Desktop\py projects\Refresh-Transparent-Images.png")
captcha_lab=tk.Label(frame)
captcha_lab.place(x=165,y=150)


generator=tk.Button(frame,text="Generate Captcha",command=generate_captcha,font=("times new roman",15,"bold"),bg="blue",fg="white",relief=FLAT)
generator.place(x=180,y=480)
generator_rep=tk.Button(frame,image=new_pic,command=auto)
generator_rep.place(x=250,y=100)
check=tk.Button(frame,text="Submit",fg="white",command=sub,bg="blue",font=("times new roman",15,"bold"))
check.place(x=235,y=420)

root.mainloop()