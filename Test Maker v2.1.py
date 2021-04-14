
import tkinter as tk
import tkinter.filedialog as filereader
from test import create_test, check_test
import os
import sys
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

def create_sentence(number, mistake):
    sentence = str(number) + ") Gujarati : " + mistake[0] + "  \nEnglish(Correct) : " + mistake[1] + "  \nEnglish(Test) :  " + mistake[2]
    return sentence
def get_result():
    temp = check_test()
    frame.forget()
    mistakes = temp[3]
    if mistakes != []:
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        mylist = tk.Listbox(root, yscrollcommand = scrollbar.set, width=100 )
        mylist.insert(tk.END, "Score: "+str(temp[0])+"/"+str(temp[1])+ "Correct Words\nAccuracy: " + str(temp[2])[:5]+ "%")
        if mistakes != []:
            mylist.insert(tk.END, "Mistakes:")
            for line in range(len(mistakes)):
                mylist.insert(tk.END, create_sentence(line + 1, mistakes[line]))
        mylist.pack( side = tk.LEFT, fill = tk.BOTH )
        scrollbar.config( command = mylist.yview )

def create_test_temp(sourcefile, testfile, lim):
    if testfile == "":
        testfile = None
    elif ".docx" not in testfile:
        testfile += ".docx"
    if lim == "":
        lim = None
    else:
        lim = int(lim)
    create_test(sourcefile, testfile, lim)
    button2 = tk.Button(frame, text="Submit", fg="white", bg="green",command=get_result)
    button2.grid(row=7, column=2)
root = tk.Tk()
root.iconbitmap(bitmap=r"gui_icon_temp.ico")
root.title("Test Maker v2.1")
source_filename = filereader.askopenfilename(initialdir = "/",title = "Select source file",filetypes=[("word files", "*.docx")])
frame = tk.Frame(root, height=1200, width=800)
lim = tk.Entry(frame)
test_file_name = tk.Entry(frame)
button1 = tk.Button(frame, text="Go", fg="white", bg="green",command=lambda : create_test_temp(source_filename, test_file_name.get(), lim.get()))
file_label = tk.Label(frame, text='File name: '+source_filename)
test_file_name_label = tk.Label(frame, text="Test file name(optional): ")
lim_label = tk.Label(frame, text="lim: ")
file_label.grid(row=1, column=1, sticky=tk.N)
test_file_name_label.grid(row=3, column=1, sticky=tk.E)
test_file_name.grid(row=3, column=2, sticky=tk.W)
lim_label.grid(row=4, column=1, sticky=tk.E)
lim.grid(row=4, column=2, sticky=tk.W)
button1.grid(row=6, column=2, sticky=tk.N)
frame.pack(fill=None, expand=False)
root.mainloop()