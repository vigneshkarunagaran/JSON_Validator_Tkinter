import json
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('Json Validator')
panedwindow=ttk.Panedwindow(window, orient=VERTICAL)  
panedwindow.grid()  
frame1=ttk.Frame(panedwindow,width=500,height=200, relief=SUNKEN)  
frame2=ttk.Frame(panedwindow,width=500,height=800, relief=SUNKEN)  
panedwindow.add(frame1, weight=1)  
panedwindow.add(frame2, weight=4)

def validate():
    try:
        inpu = txt.get("1.0",END)
        parsed = json.loads(inpu)
        out = json.dumps(parsed, indent=4, sort_keys=True)
        txt.delete('1.0', END)
        txt.insert(INSERT, out)
        messagebox.showinfo("Info","Valid JSON")
    except:
        messagebox.showerror("Error", "Invalid JSON")
    
B1 = Button(frame1,width=60, text ='Vlidate', command = validate)
B1.grid(column=0, row=0)
txt = scrolledtext.ScrolledText(frame2,height=50,width=50)
txt.grid(column=0, row=0)

window.mainloop()
    
