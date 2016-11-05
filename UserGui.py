from tkinter import Tk, Label, Button, Entry, StringVar, END, W, E
from TextAnalysisMain import mainwork

class UserGui:

    def __init__(self, master):
        self.master = master
        master.title("Text Analyzer")

        self.output_file = None
        self.entered_file = None

        self.total_label_text = StringVar()
        self.total_label_text.set(self.output_file)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Text File:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.Enter_button = Button(master, text="Enter", command=lambda: self.update("Enter"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.Enter_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_file = None
            return True

        try:
            self.entered_file = str(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "Enter":
            self.output_file = self.entered_file
            mainwork(self.output_file)
        else: # reset
            self.output_file = None

        self.total_label_text.set(self.output_file)
        self.entry.delete(0, END)
