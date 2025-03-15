from tkinter import *

class Calculator:
    def __init__(self, root):

        self.root = root
        self.root.title("Calculator")
        self.root.geometry("590x680+300+100")  
        self.root.config(bg="powder blue")

        self.Mainframe = Frame(self.root, bd=20, width=600, height=700, relief=RIDGE, bg="#808080")
        self.Mainframe.grid()
        self.widgetframe = Frame(self.Mainframe, bd=20, width=600, height=700, relief=RIDGE, bg="#c0c0c0")
        self.widgetframe.grid()

        self.lbldisplay = Label(self.widgetframe, width=28, height=2, bg='white', font=('arial', 20, 'bold'), anchor='e')
        self.lbldisplay.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

        self.input_button = ""

        self.create_button("←", 1, 0)
        self.create_button("CE", 1, 1)
        self.create_button("C", 1, 2)
        self.create_button("±", 1, 3)

        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("+", 2, 3)

        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("*", 4, 3)

        self.create_button("0", 5, 0)
        self.create_button(".", 5, 1)
        self.create_button("=", 5, 2)
        self.create_button("/", 5, 3)

        self.root.bind("<Key>", self.key_press)

    def create_button(self, text, row, column):
        btnWidget = Button(self.widgetframe, text=text, width=6, height=2, bd=4, bg='#d3d3d3',
                           font=('arial', 20, 'bold'), command=lambda: self.button_click(text))
        btnWidget.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):

        if text == "←":  
            self.input_button = self.input_button[:-1]

        elif text == "CE":  
            self.input_button = self.input_button[:-1]

        elif text == "C":  
            self.input_button = ""

        elif text == "=":  
            try:
                if self.input_button and self.input_button[-1] not in "+-*/":
                    self.input_button = str(eval(self.input_button))
                else:
                    self.input_button = "Error"
            except:
                self.input_button = "Error"

        elif text == "±": 
            if self.input_button:
                if self.input_button[0] == "-":
                    self.input_button = self.input_button[1:]  
                else:
                    self.input_button = "-" + self.input_button  

        else: 
            self.input_button += text

        self.lbldisplay.config(text=self.input_button)
    def key_press(self, event):
        key = event.char

        if key in "0123456789+-*/.=C":
            self.button_click(key) 
        elif key == "\r":  
            self.button_click("=")
        elif key == "\x08":  
            self.button_click("←")



root = Tk()
aap = Calculator(root)
root.mainloop()
