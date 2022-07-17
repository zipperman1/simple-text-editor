import tkinter as tk
from tkinter import filedialog, messagebox

# test command
def test():
    print(openedFile)

# File commands
def on_open():
    global openedFile # might want to change this up somehow later
    textPath = filedialog.askopenfilename(filetypes=(('Text files','*.txt'), ('All files','*.*')))
    with open(textPath, 'r') as textFile:
        if textFile is not None:
            textWindow.delete('1.0', tk.END)
            textWindow.insert('1.0', textFile.read())
            openedFile = textPath

def on_save():
    if openedFile is not None:
        with open(openedFile, 'w') as textFile:
            textFile.write(textWindow.get('1.0', tk.END))

def on_save_as():
    textPath = filedialog.asksaveasfilename(filetypes=(('Text files','*.txt'), ('All files','*.*')))
    with open(textPath, 'w+') as textFile:
        textFile.write(textWindow.get('1.0', tk.END))

def on_exit(): # needs reworking (i think)
    if openedFile is not None:
        quitPrompt = messagebox.askyesnocancel(title='Exit', message='Save before quitting?')
        if quitPrompt:
            on_save()
            win.quit()
        if quitPrompt is None:
            return None
        if not quitPrompt:
            win.quit()
    else:
        win.quit()

win = tk.Tk()
openedFile = None

# initialising the window
win.resizable(True, True)

# top bar
win.title('© Bauman Ballistics')
menuBar = tk.Menu(win)

fileMenu = tk.Menu(menuBar, tearoff=0) # File button
fileMenu.add_command(label='Open', command=on_open)
fileMenu.add_command(label='Save', command=on_save)
fileMenu.add_command(label='Save as', command=on_save_as)
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