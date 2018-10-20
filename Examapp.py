from tkinter import *
from time import time    
from tkinter import messagebox
q = [
        "1> In order to store values in terms of key and value we use what core datatype.",
        "2> What is the output of this expression, 3*1**3?",
        "3> What is the output of the following?\nd = {0: 'a', 1: 'b', 2: 'c'}\nfor i in d:\nprint(i)",
        "4> What is the output when following statement is executed ?\n>>>'abcd'[2:]",
        "5> Which of the following is not a class method?",
        "6> Which Of The Following Is Required To Create A New Instance Of The Class?",
        "7> Opening a file in ‘a’ mode:",
        "8> Which of the following is correct?",
        "9> Which of the following statements is wrong about inheritance?",
        "10> Suppose B is a subclass of A, to invoke the __init__ method in A from B, what is the line of code you should write?",



]

options = [    
    ["a) list","b) tuple","c) class","d) dictionary"],
    ["a) 27","b) 9","c) 3","d) 1"],
    ["a) 0 1 2","b) a b c","c) 0 a 1 b 2 c","d) none of the mentioned"],
    ["a) a","b) ab","c) cd","d) dc"],
    ["a) Non-static","b)	Static","c)	Bounded","d)	Unbounded"],
    ["a) A constructor","b) A class","c) A value-returning method","d) A None method"],
    ["a) opens a file for reading","b) opens a file for writing","c) opens a file for appending at the end of the file","d)opens a file for exclusive creation"],
    ["a) An exception is an error that occurs at the runtime.","b)A syntax error is also an exception.","c)An exception is used to exclude a block of code in Python.","d)All of the above."],
    ["a) Protected members of a class can be inherited","b)	The inheriting class is called a subclass","c)	Private members of a class can be inherited and accessed","d)	Inheritance is one of the features of OOP"],
    ["a) A.__init__(self)","b)	B.__init__(self)","c)	A.__init__(B)","d)	B.__init__(A)"],
]
a = [4,3,2,3,1,1,3,1,3,1]
class Welcome:
    
    def __init__(self,master):
        self.master=master
        self.master.geometry('800x400+100+200')
        self.master.title('WELCOME')
        self.label1=Label(self.master,text="Welcome to the python quiz.Lets test your knowledge in python.\nYou will be given 10 questions.Each question carries 1 mark each.\nWhen we click the start button the test get started, you will have to answer 10 questions within 2 minutes, the timer runs.\nIf you do not wish to answer a particular question you can move on to next question by pressing next button\n or if you wish to move to the previous question that you had skipped you can make this move by previous button.\nOnce the test is finished, result window will appear.\n The result window will show the marks obtained out of 10.\n\n\n\n",fg="green").grid(row=0,column=1)
        self.button1=Button(self.master,text="START",fg="blue",width=8, height=4,command=self.newwindow).grid(row=5,column=0)
        self.button1=Button(self.master,text="QUIT",fg="red",width=8, height=4,command=self.finish).grid(row=5,column=2)
        self.label2=Label(master, text="First Name :").grid(row=2)
        self.label3=Label(master, text="Last Name  :").grid(row=3)
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e1.grid(row=2, column=1)
        self.e2.grid(row=3, column=1)
        
    def newwindow(self):       
        if self.e1.get() and self.e2.get():
            print("next")
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            root2=Toplevel(self.master)
            myGUI=Quiz(root2)
            
        else:
            messagebox.showinfo("ERROR","Data Missing!!")
            self.e1.focus_set()
            self.e2.focus_set()

        
        
        
    def finish(self):
        self.master.destroy()

        
class Quiz():
    def __init__(self, master):
        self.master=master
        self.master.geometry('800x400+100+200')
        self.master.title('QUIZ')
        self.master.label=Label(master, text="Press the SUBMIT button to show the result.",fg="red")
        self.master.label.pack()
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Next",fg="blue",width=8, height=4, command=self.next_btn)
        self.button.pack(side=LEFT)
        self.button = Button(master, text="Back",fg="purple", width=8, height=4, command=self.back_btn)
        self.button.pack(side=LEFT)
        self.button = Button(master, text="Quit",fg="red", width=8, height=4, command=self.finish)
        self.button.pack(side=RIGHT)
  
        self.state = True
        self.minutes = 2
        self.seconds = 0
        self.mins = 2
        self.secs = 0
        self.pause_button = Button(master, bg="yellow", activebackground="Dark BLUE", text="SUBMIT", width=8, height=4, command=self.show)
        self.pause_button.pack(side=BOTTOM)

    
        self.display = Label(master, height=10, width=10, textvariable="")
        self.display.config(text="00:00")
        self.display.pack(side=BOTTOM)
        self.countdown()

    def countdown(self):
        """Displays a clock starting at min:sec to 00:00, ex: 01:00 -> 00:00"""

        if self.state == True:
            if self.secs < 10:
                if self.mins < 10:
                    self.display.config(text="0%d : 0%d" % (self.mins, self.secs))
                else:
                    self.display.config(text="%d : 0%d" % (self.mins, self.secs))
            else:
                if self.mins < 10:
                    self.display.config(text="0%d : %d" % (self.mins, self.secs))
                else:
                    self.display.config(text="%d : %d" % (self.mins, self.secs))

            if (self.mins == 0) and (self.secs == 0):
                self.display.config(text="TIMES UP!")
            else:
                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1

                self.master.after(1000, self.countdown)
        else:
            self.master.after(100, self.countdown)
    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

        
    def back_btn(self):
        self.qn = self.qn - 1
        self.display_q(self.qn)

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)
    def print_results(self):
        print("Score: ", self.correct, "/", len(q))
          
    def  finish(self):
          self.master.destroy()  
    def show(self):
        self.ans=self.correct
        messagebox.showinfo("YOUR SCORE IS:",self.ans)

    def end(self):
             self.master.destroy()               
def main():
    master=Tk()
    myGUIWelcome=Welcome(master)
    master.mainloop()
if __name__ == '__main__':
    main()    

