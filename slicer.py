import tkinter as tk
window = tk.Tk()
window.geometry("480x440")
window.config(bg="#BE361A")
window.resizable(width=False,height=False)
window.title('Simple Email Slicer')

def result():
    try:
        email=entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index('@')]
        domain = inp_email[inp_email.index('@') + 1:]
        text_box.delete('1.0', tk.END)
        msg = 'Email entered was: {}\nYour email username is {}\nAnd your email domain server is {}'
        msg_formatted = msg.format(email,username,domain)
        text_box.insert(tk.END,msg_formatted)
        entry.delete(0, 'end')
    except:
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END,"ERROR!")

def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')

greeting = tk.Label(text="Welcome to A Simple Email Slicer!",font=(12),foreground="white",background="black")
Info = tk. Label(foreground= "white",background="#BE361A",font=(10),text="Enter your email id click the done button!\n The application will extract your username and domain name.")
entry_label = tk.Label(foreground= "white",font=(10),background="black",text="Enter Your Email Id: ")
result_label = tk.Label(font=(10),foreground= "white",background="black",text="The results are as follows:")
empty_label0=tk.Label(background="#BE361A")
empty_label1=tk.Label(background="#BE361A")
empty_label2=tk.Label(background="#BE361A")
empty_label3=tk.Label(background="#BE361A")
empty_label4=tk.Label(background="#BE361A")
empty_label5=tk.Label(background="#BE361A")

e1=tk.StringVar()
entry = tk.Entry(font=(11),width=50,justify='center',textvariable=e1)

button = tk.Button(text="Done!",command=result,font=(11))
reset=tk.Button(text="Reset!",command=reset_all,font=(11))

text_box = tk.Text(height=5,width=50)

empty_label0.pack()
greeting.pack()
Info.pack()
empty_label1.pack()
entry_label.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
button.pack()
empty_label5.pack()
reset.pack()
empty_label3.pack()
result_label.pack()
text_box.pack()

window.mainloop()