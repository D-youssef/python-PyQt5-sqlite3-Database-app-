import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import sqlite3

# class of create window
class CreateScreen(QDialog) : 
    def __init__(self):
        super(CreateScreen,self).__init__()
        loadUi("create_window.ui",self)   
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.b_login.clicked.connect(self.loginfunction)

    # login button 
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
welcome = CreateScreen()
widget = QtWidgets.QStackedWidget()     
widget.addWidget(welcome)
widget.setFixedWidth(800)
widget.setFixedHeight(500)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
    
    