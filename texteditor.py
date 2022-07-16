import tkinter as tk
from tkinter import filedialog
# test command
def test():
    print('command executed')

# File commands
def on_open():
    textFile = filedialog.askopenfile(mode='w', filetypes=(('Text files','*.txt'),
                                                           ('All files','*.*')))

win = tk.Tk()

# initialising the window
win.title('© Bauman Ballistics')
win.geometry('350x200')
win.resizable(True, True)

# top bar
menubar = tk.Menu(win)

filemenu = tk.Menu(menubar, tearoff=0) # File button
filemenu.add_command(label='Open', command=on_open)
filemenu.add_command(label='Save')
filemenu.add_command(label='Test', command=test)
filemenu.add_command(label='Exit')

editmenu = tk.Menu(menubar, tearoff=0) # Edit button

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)
win.config(menu=menubar)

win.mainloop()