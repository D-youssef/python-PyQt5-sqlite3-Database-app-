import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import sqlite3

# class of login window
class WelcomeScreen(QDialog) : 
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("login_window.ui",self)   
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.b_login.clicked.connect(self.loginfunction)

    # login button
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
    
    