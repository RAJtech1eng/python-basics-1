import tkinter as tk
root=tk.Tk()
root.title('Raj Narayan Singh')
root.geometry('800x900')
def on_button_click():
    label.config(text='button clicked')
label=tk.Label(root,text='Welcome')
label.pack(pady=20)
button=tk.Button(root,text='Click me',command=on_button_click)
button.pack(pady=20)



root.mainloop()