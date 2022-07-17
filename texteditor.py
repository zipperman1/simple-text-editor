import tkinter as tk
from tkinter import filedialog

# test command
def test():
    print('command executed')

# File commands
def on_open():
    textFile = filedialog.askopenfile(mode='w', filetypes=(('Text files','*.txt'), ('All files','*.*')))

def on_save():
    print('no')

def on_exit():
    win.quit()

win = tk.Tk()

# initialising the window
win.title('© Bauman Ballistics')
win.resizable(True, True)

# top bar
menuBar = tk.Menu(win)

fileMenu = tk.Menu(menuBar, tearoff=0) # File button
fileMenu.add_command(label='Open', command=on_open)
fileMenu.add_command(label='Save', command=on_save)
fileMenu.add_command(label='Exit', command=on_exit)

editMenu = tk.Menu(menuBar, tearoff=0) # Edit button

debugMenu = tk.Menu(menuBar) # Debug menu
debugMenu.add_command(label='Test', command=test)

menuBar.add_cascade(label='File', menu=fileMenu)
menuBar.add_cascade(label='Edit', menu=editMenu)
menuBar.add_cascade(label='Debug', menu=debugMenu)

win.config(menu=menuBar)

# text window + scrollbar
textScrollBar = tk.Scrollbar(win, orient='vertical')
textScrollBar.pack(side=tk.RIGHT, fill='y')

textWindow = tk.Text(win, yscrollcommand=textScrollBar.set)
textScrollBar.config(command=textWindow.yview)
textWindow.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

win.mainloop()