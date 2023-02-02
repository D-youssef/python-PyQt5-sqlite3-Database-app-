import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget ,QLineEdit
import sqlite3   

# main window
class WelcomeScreen(QDialog) : 
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("window1.ui",self)   
        self.login.clicked.connect(self.gotologin)  # button login
        self.create.clicked.connect(self.gotocreate)  # button create

    # function of login page
    def gotologin(self):
        to_login = LoginScreen()
        widget.addWidget(to_login)  
        widget.setCurrentIndex(widget.currentIndex() + 1) # to stay in same page

    # function of create page
    def gotocreate(self):
        to_create = CreateScreen()
        widget.addWidget(to_create)
        widget.setCurrentIndex(widget.currentIndex() + 1)  # to stay in same page

# class of login window
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("login_window.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.b_login.clicked.connect(self.loginfunction)

    # login function
    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        # validate inupt fields if empty
        if len(user) == 0 or len(password) == 0 :
            self.error.setText("Please input all fields !")

        # to get data from Database
        else:
            conn = sqlite3.connect("login_data.db")
            cur = conn.cursor()
            query = "SELECT username,password FROM login_info WHERE username LIKE '"+user+"' AND password LIKE '"+password+"'"
            cur.execute(query)
            result = cur.fetchone()

            if result == None :
                self.error.setText("Incorrect username or password")
            else :
                self.error.setText("You are logged in")

# class of create window
class CreateScreen(QDialog) : 
    def __init__(self):
        super(CreateScreen,self).__init__()
        loadUi("create_window.ui",self)   
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.b_login.clicked.connect(self.loginfunction)

    # login function
    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpassword.text()

        # validate inupt fields if empty
        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0 :
            self.error.setText("Please input all fields !")

        # validate if passwords match or not
        elif password != confirmpassword :
            self.error.setText("Passwords do not match !")

        # insert data to Databse
        else:
            conn = sqlite3.connect("login_data.db")
            cur = conn.cursor()

            user_info = [user,password]
            cur.execute("INSERT INTO login_info VALUES(?,?)",user_info)
           
            conn.commit()
            conn.close()
            print("Data Added To Table...")

# main window
app = QApplication(sys.argv) 
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()   
widget.addWidget(welcome)
widget.setFixedWidth(800)
widget.setFixedHeight(500)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
    
    