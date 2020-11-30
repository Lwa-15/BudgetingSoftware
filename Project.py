from tkinter import * #Imports tkinter modules for the user interface
from tkinter import ttk
from tkinter import messagebox
import pyodbc #Imports modules for connecting a Python file and a Microsoft Access Database 
from datetime import datetime #Imports modules to utilise dates and times
import random #Imports random modules
from random import randint #Imports randint module from random
import matplotlib.pyplot as plt #Imports modules for creating matplotlib graphs
DatebaseFilePath=r"C:\Users\Luke\Desktop\Uni Python Project" #File Path to the database
Connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DatebaseFilePath+'\Budgets.accdb;') #Establishes a connection to the database
Cursor = Connect.cursor() #Creates a cursor object for the database
Username = "" #Establishes an empty variable for the Username which can be accessed globally and is for easy writing to the different tables
UserID = 0 #Establishes an empty variable for the UserID which can be accessed globally and is for easy writing to the different tables
class Login: #Class for the Login screen
    def __init__(self, master): #Initialises all of the methods for the class as well as the interface for the page
        def OpenRegisterScreen(self): #Opens the Register screen
            self.Register = Toplevel(self.master) #Brings the Register class to Toplevel
            self.application = Register(self.Register) #Runs the Register class code
        def Reset(self): #Clears all of the textboxes on the page
            Username.set("")
            Password.set("")
            self.txtUsername.focus() #Focuses the cursor back on the Username textbox
            self.txtUsername.config(bg="white") #If any error was picekd up, the background of the textbox would go red, so pressing Reset would set it back to white
            self.txtPassword.config(bg="white")
            self.txtUsername.config(fg="black")
            self.txtPassword.config(fg="black") 
        def Exit(self): #Prompts the user asking them if they want to exit the program or not
            Exit=messagebox.askyesno("Exit Program","Confirm that you want to exit")
            if Exit > 0: #If the user selects "Yes" (1), then the program is closed
                root.destroy()
                Connect.close() #Closes the database connection
        def ValidateLogin(self, Username, Password): #Ran once the Login button is pressed
            if Username == "": #If the Username textbox is empty, then an error message is presented and the textbox is coloured red 
                messagebox.showinfo("Username Error","Please enter your Username into the Username textbox.", parent=self.master)
                self.txtUsername.config(bg="red")
            if Password == "": #If the Password textbox is empty, then an error message is presented and the textbox is coloured red 
                messagebox.showinfo("Password Error","Please enter your Password into the Password textbox.")
                self.txtPassword.config(bg="red")
            if Username != "" and Password != "": #If none of the textboxes are empty, then the software will run the user details checks before logging them in
                UserPassword = Cursor.execute("SELECT Password FROM Users WHERE Username = ?", Username).fetchone()[0] #The system fetches one password where the entered username = the username in the database
                if Password == UserPassword: #If they match, then the system will login to the software
                    global UserID
                    UserID = Cursor.execute("SELECT UserID from Users WHERE Username = ?", Username).fetchone()[0] #Fetches the UserID for use throughout the program
                    messagebox.showinfo("Login Success","Welcome to Budgeting Manager", parent=self.master) #Message prompted to the user
                    self.HomePage = Toplevel(self.master) #Displays the Home Page
                    self.application = HomePage(self.HomePage)
                else:
                    messagebox.showinfo("Login Error","The Username and Password do not match. Please try again", parent=self.master) #If the textboxes' contents do not match the user details in the database, then this will be prompted to the user and the textboxes will be coloured red
                    self.txtUsername.config(fg="red")
                    self.txtPassword.config(fg="red")
            
        Username = StringVar() #Declares the two textboxes as String variables
        Password = StringVar()
        self.master = master #OOP declaration of the master variable (the page)
        self.master.title("Budgeting Manager")
        self.master.geometry("1350x1350+0+0") #Sets the dimensions of the page
        self.master.configure(background="LightSteelBlue1")

        MainFrame = Frame(self.master) #Asigns a frame to a variable
        MainFrame.grid() #Sets the frame inside the page
        MainFrame.config(background="LightSteelBlue1")
        FrameTitle = Frame(MainFrame, bd=10, width=1350, height=1200, padx=20, relief=RIDGE) #Asigns a frame inside the MainFrame variable with a ridged border
        FrameTitle.pack(side=TOP) #Packs this frame into the MainFrame near to the top
        self.Title = Label(FrameTitle, font=("Courier New", 40), text="Budgeting Manager", padx=2) #Declares a Label in the FrameTitle with a x-padding of 2
        self.Title.grid()

        DataFrame = Frame(MainFrame, bd=10, width=800, height=1200, padx=20, relief=RIDGE)
        DataFrame.pack()
        DataFrame.config(background="gray78")
        self.lblLogin = Label(DataFrame, font=("Courier New", 40), text="Login", padx=2)
        self.lblLogin.grid(row=0, column=0, sticky=W) #Assigns the Label in the first row and first column, staying to the left
        self.lblLogin.config(background="gray78")

        self.Pad0 = Label(DataFrame, font=("Courier New", 20), text="", padx=2) #Padding throughout the interface ensures that all of the widgets are spaced out from each other
        self.Pad0.grid(row=1, column=0, sticky=W)
        self.Pad0.config(background="gray78")

        self.lblUsername = Label(DataFrame, font=("Courier New", 20), text="Username:", padx=2)
        self.lblUsername.grid(row=2, column=0, sticky=W)
        self.lblUsername.config(background="gray78")
        self.txtUsername = Entry(DataFrame, font=("Courier New", 20), textvariable=Username) #Declares an Entry textbox, assigning the contents of the textbox to the variable "Username"
        self.txtUsername.grid(row=2, column=1, sticky=W)

        self.lblPassword = Label(DataFrame, font=("Courier New", 20), text="Password:", padx=2)
        self.lblPassword.grid(row=3, column=0, sticky=W)
        self.lblPassword.config(background="gray78")
        self.txtPassword = Entry(DataFrame, font=("Courier New", 20), textvariable=Password)
        self.txtPassword.grid(row=3, column=1, sticky=W)

        self.Pad1 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad1.grid(row=4, column=0, sticky=W)
        self.Pad1.config(background="gray78")

        self.btnLogin = Button(DataFrame, text="Login", font=("Courier New", 20), command = lambda: ValidateLogin(self, Username.get(), Password.get()), width=24, bd=4) #When the button is pressed, the method "ValidateLogin" will run with the contents of the textboxes as parameters
        self.btnLogin.grid(row=5, column=0)
        self.btnRegister = Button(DataFrame, text="Register", font=("Courier New", 20), command = lambda: OpenRegisterScreen(self), width=24, bd=4)
        self.btnRegister.grid(row=5, column=1)
        self.btnExit = Button(DataFrame, text="Exit", font=("Courier New", 20), command = lambda: Exit(self), width=24, bd=4)
        self.btnExit.grid(row=6, column=0)
        self.btnReset = Button(DataFrame, text="Reset", font=("Courier New", 20), command = lambda: Reset(self), width=24, bd=4)
        self.btnReset.grid(row=6, column=1)

class Register:
    def __init__(self, master):
        def Reset(self):
            Forename.set("")
            Surname.set("")
            Password.set("")
            ReEnterPassword.set("")
            self.txtForename.focus()
            self.txtForename.config(bg="white")
            self.txtSurname.config(bg="white")
            self.txtPassword.config(bg="white")
            self.txtReEnterPassword.config(bg="white")
        def Back(self):
            self.Login = Toplevel(self.master)
            self.application = Login(self.Login)
        def UserRegister(self, Forename, Surname, Password, ReEnterPassword):
            ValidationFail = False
            if Forename == "":
                ValidationFail = True
                messagebox.showinfo("Forename Error","Please enter a forename into the Forename textbox", parent=self.master)
                self.txtForename.config(bg="red")
            if Surname == "":
                ValidationFail = True
                messagebox.showinfo("Surname Error","Please enter a surname into the Surname textbox", parent=self.master)
                self.txtSurname.config(bg="red")
            if Password == "":
                ValidationFail = True
                messagebox.showinfo("Password Error","Please enter a password into the Password textbox", parent=self.master)
                self.txtPassword.config(bg="red")
            if ReEnterPassword == "":
                ValidationFail = True
                messagebox.showinfo("Re-Enter Password Error","Please enter your chosen password again into the Re-Enter Password textbox", parent=self.master)
                self.txtReEnterPassword.config(bg="red")
            if Password != ReEnterPassword:
                ValidationFail = True
                messagebox.showinfo("Password Matching Error","Please ensure your password is the same in both the Password and Re-Enter Password textboxes", parent=self.master)
                self.txtPassword.config(bg="red")
                self.txtReEnterPassword.config(bg="red")
            if ValidationFail == False:
                Username = Forename[0] + Surname[0] + str(random.randint(0,101)) #Takes the first letter of the forename and surname and a random number between 0 and 100 and this forms the Username
                Cursor.execute("INSERT INTO Users (Username, Forename, Surname, Password) VALUES (?, ?, ?, ?)", Username, Forename, Surname, Password) #Runs the SQL query and writes the user data to the database
                Connect.commit() #Commits the writing to the database officially
                messagebox.showinfo("Register Success",f"Registering successful {Forename} {Surname}. Your username is {Username}.", parent=self.master) #Presents the user with their username
                self.HomePage = Toplevel(self.master)
                self.application = HomePage(self.HomePage)

        Forename = StringVar()
        Surname = StringVar()
        Password = StringVar()
        ReEnterPassword = StringVar()
        self.master = master
        self.master.title("Budgeting Manager")
        self.master.geometry("1350x1350+0+0")
        self.master.configure(background="LightSteelBlue1")

        MainFrame = Frame(self.master)
        MainFrame.grid()
        MainFrame.config(background="LightSteelBlue1")
        FrameTitle = Frame(MainFrame, bd=10, width=1350, height=1200, padx=20, relief=RIDGE)
        FrameTitle.pack(side=TOP)
        self.Title = Label(FrameTitle, font=("Courier New", 40), text="Register User", padx=2)
        self.Title.grid()

        DataFrame = Frame(MainFrame, bd=10, width=800, height=1200, padx=20, relief=RIDGE)
        DataFrame.pack()
        DataFrame.config(background="gray78")
        self.Register = Label(DataFrame, font=("Courier New", 40), text="Register", padx=2)
        self.Register.grid(row=0, column=0, sticky=W)
        self.Register.config(background="gray78")

        self.Pad0 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad0.grid(row=1, column=0, sticky=W)
        self.Pad0.config(background="gray78")

        self.lblForename = Label(DataFrame, font=("Courier New", 20), text="Forename:", padx=2)
        self.lblForename.grid(row=2, column=0, sticky=W)
        self.lblForename.config(background="gray78")
        self.txtForename = Entry(DataFrame, font=("Courier New", 20), textvariable=Forename)
        self.txtForename.grid(row=2, column=1, sticky=W)

        self.lblSurname = Label(DataFrame, font=("Courier New", 20), text="Surname:", padx=2)
        self.lblSurname.grid(row=3, column=0, sticky=W)
        self.lblSurname.config(background="gray78")
        self.txtSurname = Entry(DataFrame, font=("Courier New", 20), textvariable=Surname)
        self.txtSurname.grid(row=3, column=1, sticky=W)

        self.lblPassword = Label(DataFrame, font=("Courier New", 20), text="Password:", padx=2)
        self.lblPassword.grid(row=4, column=0, sticky=W)
        self.lblPassword.config(background="gray78")
        self.txtPassword = Entry(DataFrame, font=("Courier New", 20), textvariable=Password)
        self.txtPassword.grid(row=4, column=1, sticky=W)

        self.lblReEnterPassword = Label(DataFrame, font=("Courier New", 20), text="Re-enter Password:", padx=2)
        self.lblReEnterPassword.grid(row=5, column=0, sticky=W)
        self.lblReEnterPassword.config(background="gray78")
        self.txtReEnterPassword = Entry(DataFrame, font=("Courier New", 20), textvariable=ReEnterPassword)
        self.txtReEnterPassword.grid(row=5, column=1, sticky=W)

        self.Pad1 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad1.grid(row=6, column=0, sticky=W)
        self.Pad1.config(background="gray78")

        self.btnRegister = Button(DataFrame, text="Register", font=("Courier New", 20), command = lambda: UserRegister(self, Forename.get(), Surname.get(), Password.get(), ReEnterPassword.get()), width=24, bd=4)
        self.btnRegister.grid(row=7, column=0)
        self.btnReset = Button(DataFrame, text="Reset", font=("Courier New", 20), command = lambda: Reset(self), width=24, bd=4)
        self.btnReset.grid(row=7, column=1)
        self.btnBack = Button(DataFrame, text="Back", font=("Courier New", 20), command = lambda: Back(self), width=24, bd=4)
        self.btnBack.grid(row=7, column=2)
        
class HomePage:
    def __init__(self, master):
        def OpenAddBudget(self):
            self.AddBudget = Toplevel(self.master)
            self.application = AddBudget(self.AddBudget)
        def OpenViewBudget(self):
            self.ViewBudget = Toplevel(self.master)
            self.application = ViewBudget(self.ViewBudget)
        def OpenAddExpenditure(self):
            self.AddExpenditure = Toplevel(self.master)
            self.application = AddExpenditure(self.AddExpenditure)
        def GetExpenditurePieChart(self):
            Labels = Cursor.execute("SELECT ExpenditureTopic FROM Expenditures WHERE UserID = ?", UserID).fetchall() #Extracts all of the Expenditure Topics for the logged-in user as tuples
            Topics = []
            for ReadInExpenditures in Labels:
                Topics.append(ReadInExpenditures[0]) #Takes the Labels data and writes them to another list where they are strings and not tuples
            Data = Cursor.execute("SELECT ExpenditureValue FROM Expenditures WHERE UserID = ?", UserID).fetchall() #Extracts all of the Expenditure Values for the logged-in user as tuples
            Values = []
            for Value in Data:
                Values.append(Value) #Takes the Values data and converts the list of tuples to a list of strings
            Explode = []
            for label in range(len(Labels)):
                Explode.append(0.1) #Applies an Explode value of 0.1 to every Label (all of the chunks of the pie chart seperate from each other)
            Figure, Axis = plt.subplots()
            Axis.pie(Values, explode=Explode, labels=Topics, autopct="%1.1f%%", shadow=False, startangle=90) #autopct is used to label the chunks of the chart with their numeric value
            Axis.axis("equal") #Sets the aspect ratio of the pie chart to "equal"
            plt.show() #Displays the pie chart
        def Logout(self):
            self.Login = Toplevel(self.master) #Returns the user to the Login screen
            self.application = Login(self.Login)
            Connect.close() #Closes the database connection
                
        self.master = master
        self.master.title("Budgeting Manager")
        self.master.geometry("1350x1350+0+0")
        self.master.configure(background="LightSteelBlue1")

        MainFrame = Frame(self.master)
        MainFrame.grid()
        MainFrame.config(background="LightSteelBlue1")
        FrameTitle = Frame(MainFrame, bd=10, width=1350, height=1200, padx=20, relief=RIDGE)
        FrameTitle.pack(side=TOP)
        self.Title = Label(FrameTitle, font=("Courier New", 40), text="Budgeting Manager", padx=2)
        self.Title.grid()

        DataFrame = Frame(MainFrame, bd=10, width=800, height=1200, padx=20, relief=RIDGE)
        DataFrame.pack()
        DataFrame.config(background="gray78")

        self.Pad0 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad0.grid(row=0, column=0, sticky=W)
        self.Pad0.config(background="gray78")
        
        self.btnAddBudget = Button(DataFrame, font=("Courier New", 20), text="Add Budget", command=lambda: OpenAddBudget(self))
        self.btnAddBudget.grid(row=1, column=0)
        
        self.Pad1 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad1.grid(row=2, column=0, sticky=W)
        self.Pad1.config(background="gray78")
        
        self.btnViewBudget = Button(DataFrame, font=("Courier New", 20), text="View Budget", command=lambda: OpenViewBudget(self))
        self.btnViewBudget.grid(row=3, column=0)
        
        self.Pad2 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad2.grid(row=4, column=0, sticky=W)
        self.Pad2.config(background="gray78")
        
        self.btnAddExpenditure = Button(DataFrame, font=("Courier New", 20), text="Add Expenditure", command=lambda: OpenAddExpenditure(self))
        self.btnAddExpenditure.grid(row=5, column=0)
        
        self.Pad3 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad3.grid(row=6, column=0, sticky=W)
        self.Pad3.config(background="gray78")
        
        self.btnViewExpenditure = Button(DataFrame, font=("Courier New", 20), text="View Expenditure", command=lambda: GetExpenditurePieChart(self))
        self.btnViewExpenditure.grid(row=7, column=0)
        
        self.Pad4 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad4.grid(row=8, column=0, sticky=W)
        self.Pad4.config(background="gray78")

        self.btnViewExpenditure = Button(DataFrame, font=("Courier New", 20), text="Logout", command=lambda: Logout(self))
        self.btnViewExpenditure.grid(row=9, column=0)

class AddBudget:
    def __init__(self, master):
        BudgetValue = StringVar()
        BudgetTopic = StringVar()
        BudgetDeadline = StringVar()

        def Reset(self):
            BudgetValue.set("")
            BudgetTopic.set("")
            BudgetDeadline.set("")
            self.txtBudgetValue.focus()
            self.txtBudgetValue.config(bg="white")
            self.txtBudgetTopic.config(bg="white")
            self.txtBudgetDeadline.config(bg="white")
        def Back(self):
            self.HomePage = Toplevel(self.master)
            self.application = HomePage(self.HomePage)
        def ValidateData(self, UserID, BudgetValue, BudgetTopic, BudgetDeadline):
            ValidateFailure = False #Will be True if any data is not validated (Presence Checks and Pattern Check validation algorithms) 
            if BudgetValue == "":
                messagebox.showinfo("Budget Value Error","Please enter your Budget Value into the Budget Value textbox.", parent=self.master)
                self.txtBudgetValue.config(bg="red")
                ValidateFailure = True
            if BudgetTopic == "":
                messagebox.showinfo("Budget Topic Error","Please enter your Budget Topic into the Budget Topic textbox.", parent=self.master)
                self.txtBudgetTopic.config(bg="red")
                ValidateFailure = True
            if BudgetDeadline == "":
                messagebox.showinfo("Budget Deadline Error","Please enter your Budget Deadline into the Budget Deaadline textbox.", parent=self.master)
                self.txtBudgetDeadline.config(bg="red")
                ValidateFailure = True
            try:
                datetime.strptime(BudgetDeadline, "%d/%m/%Y") #Checks that the contents of the Budget Deadline textbox conforms to the Pattern for validation
            except ValueError: #Error will arise if the date does not conform to the pattern
                messagebox.showinfo("Budget Deadline Pattern Error","Please ensure your Budget Deadline in the Budget Deaadline textbox is in the pattern XX/XX/XXXX.", parent=self.master)
                ValidateFailure = True
            if ValidateFailure == False:
                AddBudgetToDatabase(self, UserID, BudgetValue, BudgetTopic, BudgetDeadline)
        def AddBudgetToDatabase(self, UserID, BudgetValue, BudgetTopic, BudgetDeadline): #Checks that the budget doesn't already exist in the database and adds the budget data to the database if it doesn't already exist
            Budgets = Cursor.execute("SELECT BudgetTopic FROM Budgets WHERE UserID = ? AND BudgetTopic = ?", UserID, BudgetTopic).fetchall()
            if BudgetTopic not in Budgets:
                Cursor.execute("INSERT INTO Budgets (BudgetTopic, BudgetValue, BudgetDeadline, UserID) VALUES (?, ?, ?, ?)", BudgetTopic, BudgetValue, BudgetDeadline, UserID)
                Connect.commit()
                messagebox.showinfo("Add Budget Success","Budget Successfully added", parent=self.master)
            else:    
                messagebox.showinfo("Add Budget Error","This budget already exists and was not added to the database", parent=self.master)
   
        self.master = master
        self.master.title("Budgeting Manager")
        self.master.geometry("1350x1350+0+0")
        self.master.configure(background="LightSteelBlue1")

        MainFrame = Frame(self.master)
        MainFrame.grid()
        MainFrame.config(background="LightSteelBlue1")
        FrameTitle = Frame(MainFrame, bd=10, width=1350, height=1200, padx=20, relief=RIDGE)
        FrameTitle.pack(side=TOP)
        self.Title = Label(FrameTitle, font=("Courier New", 40), text="Add Budget", padx=2)
        self.Title.grid()

        DataFrame = Frame(MainFrame, bd=10, width=800, height=1200, padx=20, relief=RIDGE)
        DataFrame.pack()
        DataFrame.config(background="gray78")

        self.Pad0 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad0.grid(row=0, column=0, sticky=W)
        self.Pad0.config(background="gray78")

        self.lblBudgetValue = Label(DataFrame, font=("Courier New", 20), text="Budget Value:", padx=2)
        self.lblBudgetValue.grid(row=1, column=0, sticky=W)
        self.lblBudgetValue.config(background="gray78")
        
        self.txtBudgetValue = Entry(DataFrame, font=("Courier New", 20), textvariable=BudgetValue)
        self.txtBudgetValue.grid(row=1, column=1)

        self.lblBudgetTopic = Label(DataFrame, font=("Courier New", 20), text="Budget Topic:", padx=2)
        self.lblBudgetTopic.grid(row=2, column=0, sticky=W)
        self.lblBudgetTopic.config(background="gray78")
        
        self.txtBudgetTopic = Entry(DataFrame, font=("Courier New", 20), textvariable=BudgetTopic)
        self.txtBudgetTopic.grid(row=2, column=1)

        self.lblBudgetDeadline = Label(DataFrame, font=("Courier New", 20), text="Budget Deadline:", padx=2)
        self.lblBudgetDeadline.grid(row=3, column=0, sticky=W)
        self.lblBudgetDeadline.config(background="gray78")
        
        self.txtBudgetDeadline = Entry(DataFrame, font=("Courier New", 20), textvariable=BudgetDeadline)
        self.txtBudgetDeadline.grid(row=3, column=1)

        self.Pad1 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad1.grid(row=4, column=0, sticky=W)
        self.Pad1.config(background="gray78")

        self.btnAdd = Button(DataFrame, text="Add", font=("Courier New", 20), command = lambda: ValidateData(self, UserID, BudgetValue.get(), BudgetTopic.get(), BudgetDeadline.get()), width=24, bd=4)
        self.btnAdd.grid(row=5, column=0)
        self.btnReset = Button(DataFrame, text="Reset", font=("Courier New", 20), command = lambda: Reset(self), width=24, bd=4)
        self.btnReset.grid(row=5, column=1)
        self.btnBack = Button(DataFrame, text="Back", font=("Courier New", 20), command = lambda: Back(self), width=24, bd=4)
        self.btnBack.grid(row=5, column=2)

class AddExpenditure:
    def __init__(self, master):
        ExpenditureValue = StringVar()
        ExpenditureTopic = StringVar()
        ExpenditureDate = StringVar()

        def Reset(self):
            ExpenditureValue.set("")
            ExpenditureTopic.set("")
            ExpenditureDate.set("")
            self.txtExpenditureValue.focus()
            self.txtExpenditureValue.config(bg="white")
            self.txtExpenditureTopic.config(bg="white")
            self.txtExpenditureDate.config(bg="white")
        def Back(self):
            self.HomePage = Toplevel(self.master)
            self.application = HomePage(self.HomePage)
        def ValidateData(self, UserID, ExpenditureValue, ExpenditureTopic, ExpenditureDate):
            ValidateFailure = False
            if ExpenditureValue == "":
                messagebox.showinfo("Expenditure Value Error","Please enter your Expenditure Value into the Expenditure Value textbox.", parent=self.master)
                self.txtExpenditureValue.config(bg="red")
                ValidateFailure = True
            if ExpenditureTopic == "":
                messagebox.showinfo("Expenditure Topic Error","Please enter your Expenditure Topic into the Expenditure Topic textbox.", parent=self.master)
                self.txtExpenditureTopic.config(bg="red")
                ValidateFailure = True
            if ExpenditureDate == "":
                messagebox.showinfo("Expenditure Date Error","Please enter your Expenditure Date into the Expenditure Date textbox.", parent=self.master)
                self.txtExpenditureDate.config(bg="red")
                ValidateFailure = True
            try:
                datetime.strptime(ExpenditureDate, "%d/%m/%Y")
            except ValueError:
                messagebox.showinfo("Expenditure Date Pattern Error","Please ensure your Expenditure Date in the Expenditure Date textbox is in the pattern XX/XX/XXXX.", parent=self.master)
                ValidateFailure = True
            if ValidateFailure == False:
                BudgetID = Cursor.execute("SELECT BudgetID FROM Budgets WHERE UserID = ? AND BudgetTopic = ?", UserID, ExpenditureTopic).fetchone()[0]
                if BudgetID == None:
                    messagebox.showinfo("Add Expenditure Error","This expenditure topic is invalid, as a budget topic needs to exist.", parent=self.master)
                else:
                    Cursor.execute("INSERT INTO Expenditures (UserID, ExpenditureTopic, ExpenditureValue, BudgetID, ExpenditureDate) VALUES (?, ?, ?, ?, ?)", UserID, ExpenditureTopic, float(ExpenditureValue), BudgetID, ExpenditureDate)
                    Connect.commit()
                    messagebox.showinfo("Add Expenditure Success","Expenditure Successfully added", parent=self.master)

        self.master = master
        self.master.title("Budgeting Manager")
        self.master.geometry("1350x1350+0+0")
        self.master.configure(background="LightSteelBlue1")

        MainFrame = Frame(self.master)
        MainFrame.grid()
        MainFrame.config(background="LightSteelBlue1")
        FrameTitle = Frame(MainFrame, bd=10, width=1350, height=1200, padx=20, relief=RIDGE)
        FrameTitle.pack(side=TOP)
        self.Title = Label(FrameTitle, font=("Courier New", 40), text="Add Expenditure", padx=2)
        self.Title.grid()

        DataFrame = Frame(MainFrame, bd=10, width=800, height=1200, padx=20, relief=RIDGE)
        DataFrame.pack()
        DataFrame.config(background="gray78")

        self.Pad0 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad0.grid(row=0, column=0, sticky=W)
        self.Pad0.config(background="gray78")

        self.lblExpenditureValue = Label(DataFrame, font=("Courier New", 20), text="Expenditure Value:", padx=2)
        self.lblExpenditureValue.grid(row=1, column=0, sticky=W)
        self.lblExpenditureValue.config(background="gray78")
        
        self.txtExpenditureValue = Entry(DataFrame, font=("Courier New", 20), textvariable=ExpenditureValue)
        self.txtExpenditureValue.grid(row=1, column=1)

        self.lblExpenditureTopic = Label(DataFrame, font=("Courier New", 20), text="Expenditure Topic:", padx=2)
        self.lblExpenditureTopic.grid(row=2, column=0, sticky=W)
        self.lblExpenditureTopic.config(background="gray78")
        
        self.txtExpenditureTopic = Entry(DataFrame, font=("Courier New", 20), textvariable=ExpenditureTopic)
        self.txtExpenditureTopic.grid(row=2, column=1)

        self.lblExpenditureDate = Label(DataFrame, font=("Courier New", 20), text="Expenditure Date:", padx=2)
        self.lblExpenditureDate.grid(row=3, column=0, sticky=W)
        self.lblExpenditureDate.config(background="gray78")
        
        self.txtExpenditureDate = Entry(DataFrame, font=("Courier New", 20), textvariable=ExpenditureDate)
        self.txtExpenditureDate.grid(row=3, column=1)

        self.Pad1 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad1.grid(row=4, column=0, sticky=W)
        self.Pad1.config(background="gray78")

        self.btnAdd = Button(DataFrame, text="Add", font=("Courier New", 20), command = lambda: ValidateData(self, UserID, ExpenditureValue.get(), ExpenditureTopic.get(), ExpenditureDate.get()), width=24, bd=4)
        self.btnAdd.grid(row=5, column=0)
        self.btnReset = Button(DataFrame, text="Reset", font=("Courier New", 20), command = lambda: Reset(self), width=24, bd=4)
        self.btnReset.grid(row=5, column=1)
        self.btnBack = Button(DataFrame, text="Back", font=("Courier New", 20), command = lambda: Back(self), width=24, bd=4)
        self.btnBack.grid(row=5, column=2)

class ViewBudget:
    def __init__(self, master):
        Budgets = StringVar()
        def ValidateDropdown(self, BudgetTopic):
            if BudgetTopic == "":
                messagebox.showinfo("Budget Topic Error","Please select a Topic from the dropdown menu.", parent=self.master)
            else:
                GetBudgetData(self, BudgetTopic)
        def Back(self):
            self.HomePage = Toplevel(self.master)
            self.application = HomePage(self.HomePage)
        def GetBudgetData(self, BudgetTopic):
            ValueAxis = Cursor.execute("SELECT ExpenditureValue FROM Expenditures WHERE UserID = ? AND ExpenditureTopic = ?", UserID, BudgetTopic).fetchall()
            DateAxis = Cursor.execute("SELECT ExpenditureDate FROM Expenditures WHERE UserID = ? AND ExpenditureTopic = ?", UserID, BudgetTopic).fetchall()
            BudgetTotal = float(Cursor.execute("SELECT BudgetValue FROM Budgets WHERE UserID = ? AND BudgetTopic = ?", UserID, BudgetTopic).fetchone()[0]) #Fetches the Budget Value of the selected budget and converts the value from a tuple to a float (decimal)
            BudgetValues = []
            BudgetValues.append(BudgetTotal) #Applies the Budget Value as the starting value for the Y axis 
            for value in ValueAxis: #This For loop minuses the Expenditure Value for each entered data with the selected Budget from the Budget Value and appends it to a list (Y axis values)
                BudgetTotal = BudgetTotal - int(value[0])
                BudgetValues.append(BudgetTotal)
            if len(BudgetValues) < len(DateAxis): #This If statement appends the last item in the BudgetValues list repeatedly until the length of the list matches the length of the DateAxis list (X and Y axis lists need to be the same length for a line graph)
                LastItem = BudgetValues[len(BudgetValues)-1]
                while True:
                    BudgetValues.append(LastItem)
                    if len(BudgetValues) == len(DateAxis):
                        break
            elif len(DateAxis) < len(BudgetValues): #This If statement appends the last item in the DateAxis list repeatedly until the length of the list matches the length of the BudgetValues list (X and Y axis lists need to be the same length for a line graph)
                LastItem = DateAxis[len(DateAxis)-1]
                while True:
                    DateAxis.append(LastItem)
                    if len(DateAxis) == len(BudgetValues):
                        break
                
            plt.plot(DateAxis, BudgetValues, label="Remains of budget") 
            plt.xticks(rotation=45) #Rotates the X axis' labels 45 degrees
            plt.ylabel("Value of budget (£)")
            plt.title(f"Budget Graph for {self.cmbBudgets.get()}") 
            LastValue = BudgetValues[len(BudgetValues)-1] #Finds the current value of the budget after all of the subtractions
            LastValueDiff = 0 - LastValue
            if LastValue < 0: #This If statement checks if the user is over budget or not
                messagebox.showinfo("Budget Warning!",f"You are £{LastValueDiff} over budget! Please spend less in this area.", parent=self.master)
            elif LastValue > 0:
                LastValueDiff = abs(LastValueDiff)
                messagebox.showinfo("Budget Information!",f"You are £{LastValueDiff} under budget! Keep it up.", parent=self.master)
            else:
                messagebox.showinfo("Budget Warning!","You are on budget. Keep it up but proceed with caution.", parent=self.master)
            plt.show()
            
        self.master = master
        self.master.title("Budgeting Manager")
        self.master.geometry("1350x1350+0+0")
        self.master.configure(background="LightSteelBlue1")

        MainFrame = Frame(self.master)
        MainFrame.grid()
        MainFrame.config(background="LightSteelBlue1")
        FrameTitle = Frame(MainFrame, bd=10, width=1350, height=1200, padx=20, relief=RIDGE)
        FrameTitle.pack(side=TOP)
        self.Title = Label(FrameTitle, font=("Courier New", 40), text="View Budget", padx=2)
        self.Title.grid()

        DataFrame = Frame(MainFrame, bd=10, width=800, height=1200, padx=20, relief=RIDGE)
        DataFrame.pack()
        DataFrame.config(background="gray78")

        self.Pad0 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad0.grid(row=0, column=0, sticky=W)
        self.Pad0.config(background="gray78")

        BudgetList = Cursor.execute("SELECT BudgetTopic FROM Budgets WHERE UserID = ?", UserID).fetchall() #Fetches all of the logged in user's budgets in order to populate the dropdown menu
        Budgets = [] 
        for BudgetIndex in BudgetList:
            Budgets.append(BudgetIndex[0]) #Appends the string (from a tuple) to the Budgets list to remove the quote marks, commas and brackets 
        
        self.lblBudgets = Label(DataFrame, font=("Courier New", 20), text="Budget Topic:", padx=2) 
        self.lblBudgets.grid(row=1, column=0, sticky=W)
        self.lblBudgets.config(background="gray78")
        self.cmbBudgets = ttk.Combobox(DataFrame, font=("Courier New", 20),values=Budgets, state="readonly")
        self.cmbBudgets.grid(row=1, column=1, sticky=W)

        self.btnView = Button(DataFrame, text="View", font=("Courier New", 20), command = lambda: ValidateDropdown(self, self.cmbBudgets.get()), width=24, bd=4)
        self.btnView.grid(row=1, column=2)
        self.btnBack = Button(DataFrame, text="Back", font=("Courier New", 20), command = lambda: Back(self), width=24, bd=4)
        self.btnBack.grid(row=2, column=2)

        self.Pad1 = Label(DataFrame, font=("Courier New", 20), text="", padx=2)
        self.Pad1.grid(row=2, column=0, sticky=W)
        self.Pad1.config(background="gray78")
        
if __name__ == "__main__":
    root = Tk()
    application = Login(root) #Makes the Login page the first page which loads
    root.mainloop() #Begins the interface code
