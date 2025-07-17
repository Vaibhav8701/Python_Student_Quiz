from tkinter import *
from tkinter import messagebox, ttk
from functools import partial
import re
import json


registrated_mail="Admin"
registrated_password="Abcd@1234"

#----------------- Login Window--------------------------

def login_screen():
    # Create the main window
    login_window = Tk()
    login_window.title("Email Login")
    login_window.geometry("400x300")
    login_window.config(bg="light green")
    login_window.resizable(0,0)

    # Function to validate the password

    def valid_password():
        password=password_var.get()
        mail=mail_var.get()
      
        if password==registrated_password and mail==registrated_mail :
            login_window.destroy()
            registration()
            
          
        else:
          messagebox.showwarning("warning ","please login valid email and password")
          
          
        
    # Function to  visible of the password

    def show_password():
        if h1.get():
            ent1.config(show="")
        else:
            ent1.config(show="*")

    #Email Id
    mail_var=StringVar()
    lbl1=Label(login_window,text=" Enter Your Email  ID  :",bg="light green",font="bold 12")
    lbl1.place(x=30,y=58)
    ent1=Entry(login_window,textvariable=mail_var,width=25,bg="pink",font="bold 10")
    ent1.place(x=200,y=60)

    #Password
    password_var=StringVar()
    lbl2=Label(login_window,text="Enter Your Password :",bg="light green",font="bold 12")
    lbl2.place(x=30,y=100)
    ent1=Entry(login_window,width=25,textvariable=password_var,bg="pink",font="bold 10",show="*")
    ent1.place(x=200,y=100)

    #Show Password Check Button
    h1=BooleanVar()
    chkbtn=Checkbutton(login_window,text="Show Password",variable=h1,bg="light green",font="bold 12",activebackground="light green",command=show_password)
    chkbtn.place(x=200,y=123)


    btn=Button(login_window,text="Registor",bg="pink",activebackground="yellow",font="bold 12",command=valid_password)
    btn.place(x=170,y=200)

    login_window.mainloop()


#------------------------------REGISTRATION FORM-------------------------------------------
def registration():
    top=Tk()
    top.geometry("600x600")
    top.resizable(0,0)
    top.title("REGISTRATION FORM")              
    top.config(bg="light green")
    

    def exam():
       if not registration_completed:
            messagebox.showwarning("Warning", "Please submit the registration form first!")
       else:
            top.destroy()
            QuizWindow()

    def add(self,n1,n2,n3,n4,radio1,radio2,h1,h2,h3,h4):
        name=n1.get()+n2.get()#get n1 and n2 values in this function
        fname=n3.get()
        mname=n4.get()
        if name=="":
           messagebox.showwarning("warning ","please fill your name")
        elif fname=="":
           messagebox.showwarning("warning ","please fill your father's name")
        elif mname=="":
           messagebox.showwarning("warning ","please fill your mother's name")

        else:
           gender=radio1.get()

           if gender == 1:
              rd = "Male"
           elif gender == 2:
              rd = "Female"
           elif gender == 3:
              rd = "Other"
           else:
              rd = "Not Selected"
    
           qualification=radio2.get()

           if qualification == 1:
              qf = "10th"
           elif qualification == 2:
              qf = "12th"
           elif qualification == 3:
              qf = "Graduation"
           else:
              qf = "Not Selected"
    
           h1=h1.get()    
           h2=h2.get()
           h3=h3.get()
           h4=h4.get()

           if  h1==1 and h2==0 and h3==0 and h4==0:
             hb="Python"
           if h1==0 and h2==1 and h3==0 and h4==0:
             hb="C++"
           if h1==0 and h2==0 and h3==1 and h4==0:
             hb="Java"
           if h1==0 and h2==0 and h3==0 and h4==1:
             hb="SQL"
           if h1==0 and h2==0 and h3==0 and h4==0:
             hb=""
           if h1==0 and h2==0 and h3==1 and h4==1:
             hb="Java & SQL"
           if h1==0 and h2==1 and h3==0 and h4==1:
             hb="C++ & SQL"
           if h1==0 and h2==1 and h3==1 and h4==0:
             hb="C++ & Java"
           if h1==0 and h2==1 and h3==1 and h4==1:
             hb="C++ & Java & SQL"
           if h1==1 and h2==1 and h3==0 and h4==1:
             hb="Pyhton & C++ & SQL"
           if h1==1 and h2==0 and h3==0 and h4==1:
             hb="Python & SQL"
           if h1==1 and h2==0 and h3==1 and h4==0:
             hb="Python & Java"
           if h1==1 and h2==0 and h3==1 and h4==1:
             hb="Python & Java & SQL"
           if h1==1 and h2==1 and h3==0 and h4==0:
             hb="Python & c++"
           if h1==1 and h2==1 and h3==1 and h4==0:
             hb="Python & c++ & Java"
           if h1==1 and h2==1 and h3==1 and h4==1:
             hb="Python & C++ & Java & SQL"
        

           if gender==0:  
              messagebox.showwarning("warning ","please fill your gender ")
           elif qualification==0:
             messagebox.showwarning("warning ","please fill your qualification ")
           else:
        
              result=(
                     "Name = "+name +
                     "\n Father's Name = "+fname+
                     "\n Mother's Name = "+mname+
                     "\n Gender = "+rd+
                     "\n Qualification = "+qf+
                     "\n Skills  = "+hb+
                     "\n State  = "+state+
                     "\n City   = "+city
                     )
           f=open("demo.txt","a")
           f.write(result)

           self.config(text=result)

           global registration_completed
           registration_completed = True
           messagebox.showinfo("Success", "Registration successful! You can now start the quiz.")

  


    state=""
    city=""
    def update_city(self):
       global state
       global city
       state=combo_state.get()
    
       if state=="Rajasthan":
            print(state)
            combo_city=ttk.Combobox(top,values=["Sikar","Jaipur","Udaipur"])
            combo_city.place(x=230,y=310)
            combo_city.bind("<<ComboboxSelected>>",update_city1)
            city=combo_city.get()
            print(city)


       elif state=="Gujarat":
            combo_city=ttk.Combobox(top,values=["Ahmedabad", "Surat", "Rajkot"])
            combo_city.place(x=230,y=310)
            city=combo_city.get()


       elif state=="Bihar":
            combo_city=ttk.Combobox(top,values=["Patna", "Gaya", "Bhagalpur"])
            combo_city.place(x=230,y=310)
            city=combo_city.get()


       elif state=="Goa":
            combo_city=ttk.Combobox(top,values=["Panaji", "Vasco", "Mapusa"])
            combo_city.place(x=230,y=310)
            city=combo_city.get()
    def update_city1(self):
        
        global state
        global city
        city=combo_state.get()
        print(city)
    

  
   
   # First Name

    n1=StringVar()
    lbl1=Label(top,text="Enter your first name : ",bg="light green",font="bold 12")
    lbl1.place(x=40,y=58)
    ent1=Entry(top,textvariable=n1)
    ent1.place(x=230,y=60)

# Last Name

    n2=StringVar()
    lbl2=Label(top,text="Enter your last name : ",bg="light green",font="bold 12")
    lbl2.place(x=40,y=88)
    ent2=Entry(top,textvariable=n2)
    ent2.place(x=230,y=90)

   # Father's Name

    n3=StringVar()
    lbl3=Label(top,text="Enter your father's name : ",bg="light green",font="bold 12")
    lbl3.place(x=40,y=118)
    ent3=Entry(top,textvariable=n3)
    ent3.place(x=230,y=120)

   # Mother's Name

    n4=StringVar()
    lbl4=Label(top,text="Enter your Mother's name : ",bg="light green",font="bold 12")
    lbl4.place(x=40,y=148)
    ent4=Entry(top,textvariable=n4)
    ent4.place(x=230,y=150)

   # Gender Radio Buttons

    radio1=IntVar()
    lbl5=Label(top,text="Select your Gender : ",bg="light green",font="bold 12")
    lbl5.place(x=40,y=180)
    rbtn1=Radiobutton(top,text="Male",variable=radio1,value=1,bg="light green",font="bold 12",activebackground="light green")
    rbtn1.place(x=230,y=180)
    rbtn2=Radiobutton(top,text="Female",variable=radio1,value=2,bg="light green",font="bold 12",activebackground="light green")
    rbtn2.place(x=290,y=180)
    rbtn3=Radiobutton(top,text="Other",variable=radio1,value=3,bg="light green",font="bold 12",activebackground="light green")
    rbtn3.place(x=370,y=180)

   # Qualification Radio Buttons

    radio2=IntVar()
    lbl6=Label(top,text="Select your Qualification : ",bg="light green",font="bold 12")
    lbl6.place(x=40,y=210)
    rbtn4=Radiobutton(top,text="10th",variable=radio2,value=1,bg="light green",font="bold 12",activebackground="light green")
    rbtn4.place(x=230,y=210)
    rbtn5=Radiobutton(top,text="12th",variable=radio2,value=2,bg="light green",font="bold 12",activebackground="light green")
    rbtn5.place(x=290,y=210)
    rbtn6=Radiobutton(top,text="Graduation",variable=radio2,value=3,bg="light green",font="bold 12",activebackground="light green")
    rbtn6.place(x=370,y=210)

   # Skills Check Buttons

    h1=IntVar()
    h2=IntVar()
    h3=IntVar()
    h4=IntVar()
    lbl7=Label(top,text="Select your Skills : ",bg="light green",font="bold 12")
    lbl7.place(x=40,y=240)
    chkbtn1=Checkbutton(top,text="Python",variable=h1,bg="light green",font="bold 12",activebackground="light green")
    chkbtn1.place(x=230,y=240)
    chkbtn2=Checkbutton(top,text="Java",variable=h2,bg="light green",font="bold 12",activebackground="light green")
    chkbtn2.place(x=310,y=240)
    chkbtn3=Checkbutton(top,text="C++",variable=h3,bg="light green",font="bold 12",activebackground="light green")
    chkbtn3.place(x=380,y=240)
    chkbtn4=Checkbutton(top,text="SQL",variable=h4,bg="light green",font="bold 12",activebackground="light green")
    chkbtn4.place(x=440,y=240)

   # State Combobox

    lbl8=Label(top,text="Select your State : ",bg="light green",font="bold 12")
    lbl8.place(x=40,y=278)
    combo_state=ttk.Combobox(top,value=["Rajasthan","Gujarat","Bihar","Goa"])
    combo_state.place(x=230,y=280)
    combo_state.set("Select State")  # Optional: Default placeholder
    combo_state.bind("<<ComboboxSelected>>",update_city)
    # State Combobox

    lbl9=Label(top,text="Select your City : ",bg="light green",font="bold 12")
    lbl9.place(x=40,y=308)
    combo_city=ttk.Combobox(top)
    combo_city.place(x=230,y=310)
    combo_city.set("Select City")
  


   # Output Label

    lbl=Label(top,bg="light green",fg="black",font="bold 12")
    lbl.place(x=200,y=400)

    add=partial(add,lbl,n1,n2,n3,n4,radio1,radio2,h1,h2,h3,h4)

    # Submit Button

    btn=Button(top,text="SUBMIT",bg="blue",fg="white",font="bold 10",command=add)
    btn.place(x=270,y=550)
    
    btn=Button(top,text="START EXAM",bg="blue",fg="white",font="bold 10",command=exam)
    btn.place(x=370,y=550)

    top.mainloop()

#--------------------QUIZ WINDOW-------------------------------
def QuizWindow():
    class Quiz:
        def __init__(self):
            self.q_no = 0
            self.correct = 0
            self.opt_selected = IntVar()

            self.hour = StringVar()
            self.minute = StringVar()
            self.second = StringVar()
            self.hour.set(0)
            self.minute.set(1)
            self.second.set(5)
            

            time_label=Label(top,text="(HH:MM:SS)",bg="light green",font="ariel 15 bold")
            time_label.place(x=10,y=60)
            hourEntry = Entry(top,width=3,textvariable=self.hour,font="ariel 15")
            hourEntry.place(x=150,y=60)
            hourEntry = Entry(top,width=3,textvariable=self.minute,font="ariel 15")
            hourEntry.place(x=190,y=60)
            hourEntry = Entry(top,width=3,textvariable=self.second,font="ariel 15")
            hourEntry.place(x=230,y=60)

            self.display_title()
            self.display_question()
            self.opts = self.radio_buttons() # This calls the function radio_buttons() and return it to variable self.opts
            self.display_options()
            self.buttons()

            self.submit()

            self.data_size = len(questions)
        def display_title(self):
            title = Label(top,text="MULTIPE CHOICE QUESTIONS :",width=50,bg="light green",font="ariel 20 bold")
            title.place(x=0,y=10)


        def display_question(self):
            #self.q_no takes the question from json file line wise
            q_label = Label(top,text=questions[self.q_no],bg="skyblue",font="ariel 20 bold",anchor="w")#anchore tag is used for west side
            q_label.place(x=70,y=120)
        
        def radio_buttons(self):
            q_list = []
            y_pos = 170
            while len(q_list) < 4:
                radio_btn = Radiobutton(top, text="", variable=self.opt_selected,
                                        value=len(q_list) + 1, font="ariel 14", bg="skyblue")
                radio_btn.place(x=100, y=y_pos)
                q_list.append(radio_btn)#its appends the all 4 options 
                y_pos += 40
            return q_list
        

        def display_options(self):
            self.opt_selected.set(0)
            val = 0
            for option in options[self.q_no]:
                self.opts[val]['text'] = option
                val += 1
        
        def buttons(self):
            next_btn = Button(top,text="Next",command=self.next_btn,bg="light green",font="ariel 16 bold")
            next_btn.place(x=350,y=380)

            quit_btn = Button(top,text="Exit",command=top.destroy,bg="light green",font="ariel 16 bold")
            quit_btn.place(x=700,y=60)

        def next_btn(self):
            if self.check_ans(self.q_no):
                self.correct += 1
            self.q_no += 1

            if self.q_no == self.data_size:
                self.display_result()
                top.destroy()
            else:
                self.display_question()
                self.display_options()


        def check_ans(self,q_no):
            if self.opt_selected.get() == answer[q_no]:
                return True
            
        def display_result(self):
            wrong_count = self.data_size - self.correct
            correct = f"Correct: {self.correct}"
            wrong = f"Wrong: {wrong_count}"
            score = int(self.correct / self.data_size * 100)
            result = f"Score: {score}%"
            
            messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        

        def submit(self):
            try:
                temp = int(self.hour.get())  * 3600 + int(self.minute.get()) * 60 + int(self.second.get())
            
            except:
                messagebox.showerror("Invalid input","please enter valid time values")
                return
            

            def countdown():
                nonlocal temp
                if temp >= 0:
                    mins,secs = divmod(temp, 60)
                    hours, mins = divmod(mins, 60)

                    self.hour.set(f"{hours:02}")
                    self.minute.set(f"{mins:02}")
                    self.second.set(f"{secs:02}")
                
                    top.after(1000, countdown)
                    temp -= 1
            
                else:
                    messagebox.showerror("Time's up!", "Time's up!")
                    self.display_result()
                    top.quit()

            countdown()



    top=Tk()
    top.geometry("800x500")
    top.title("QUIZ")
    top.config(bg="skyblue")


    #load JSON data  
    with open('Mdata.json') as f:
        Mdata=json.load(f)

    questions=Mdata['question']
    options=Mdata['options']
    answer=Mdata['answer']

    quiz = Quiz()
    top.mainloop()

#------------------------RUN APP--------------------------------
login_screen()

   

