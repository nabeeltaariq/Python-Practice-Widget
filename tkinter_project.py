import os
import tkinter as tk
from tkinter import ttk
from typing import Dict
import csv


win = tk.Tk()
win.title('GUI')

name_label= ttk.Label(win,text="Enter your  name:")
name_label.grid(row=0,column=0,sticky=tk.W)

email_label=ttk.Label(win,text="Enter your  email:")
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="Enter your  age:")
age_label.grid(row=2,column=0,sticky=tk.W)


#entry box

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16, textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()


email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16, textvariable=email_var)
email_entrybox.grid(row=1,column=1)


age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16, textvariable=age_var)
age_entrybox.grid(row=2,column=1)

#combo box

gender_label=ttk.Label(win,text="Select your gender")
gender_label.grid(row=3,column=0)
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=13,textvariable=gender_var, state='readonly' )
gender_combobox['values']=('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)



#radioButton
user_type_radio_btn_var=tk.StringVar()
user_type_radio_btn1=ttk.Radiobutton(win,text='Student',value='Student', variable=user_type_radio_btn_var)
user_type_radio_btn1.grid(row=4,column=0)
user_type_radio_btn2=ttk.Radiobutton(win,text='Teacher',value='Teacher', variable=user_type_radio_btn_var)
user_type_radio_btn2.grid(row=4,column=1)


#check Button


check_btn_var=tk.IntVar()
check_btn=ttk.Checkbutton(win,text="check if your want to check this and get news from us",variable=check_btn_var)
check_btn.grid(row=5,columnspan=3)


#button


# def action ():
#     username=name_var.get()
#     email=email_var.get()
#     age=age_var.get()
#     gender_combobox_value=gender_var.get
#     user_type_val=user_type_radio_btn_var.get();
#     check_btn_val=check_btn_var.get();
#     if check_btn_val==0:
#         subscribed='NO'
#     else:
#         subscribed='YES'

#     with open('file.txt','a') as f:
#         f.write(f'{username},{email},{age},{gender_combobox},{user_type_val},{subscribed}\n')
    
#     name_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     name_label.configure(foreground='Blue')


def action ():
    username=name_var.get()
    email=email_var.get()
    age=age_var.get()
    gender_combobox_value=gender_var.get
    user_type_val=user_type_radio_btn_var.get();
    check_btn_val=check_btn_var.get();
    if check_btn_val==0:
        subscribed='NO'
    else:
        subscribed='YES'

    with open('file.csv','a', newline='') as f:
        dict_writer = csv.DictWriter(f,fieldnames=['Username','email','age','type','gender','subcribed'])
        if os.stat("file.csv").st_size==0:
            dict_writer.writeheader()
       
        dict_writer.writerow(
            {
                'Username':username,
                'email': email,
                'age': age,
                'type': user_type_val,
                'gender':gender_combobox_value ,
                'subcribed': subscribed

            }
        )
        

    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    name_label.configure(foreground='Blue') 


     

submit_button = ttk.Button(win,text="submit", command=action)

submit_button.grid(row=6,column=0)





win.mainloop()