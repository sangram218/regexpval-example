from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys, validator

ui,_=loadUiType('regex_onpa.bin')

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.sctit = "Validation completed with SUCCESS"
        self.scmsg = "Congratulations for all the valid information you gave here! Now we will sell this information to third party websites at huge prices!"
        self.pwstr = "Password strength : "
        self.ertit = "Validation completed with FAILURE"
        self.ermsg = "We could not store your information due to the following issues. \nCorrect them and try again!"
        self.fnerr = "The first name consists of illegal characters. Only alphabets and symbols like - are allowed in this field."
        self.lnerr = "The last name consists of illegal characters. Only alphabets and symbols like - are allowed in this field."
        self.pnerr = "The phone number consists of illegal characters. Only numbers and symbols like + and - are allowed in this field."
        self.emerr = "The email address consists of illegal characters. Only alphanumeric characters and valid email symbols are allowed in this field."
        self.pwerr = "The password consists of illegal characters. Only alphanumeric characters and valid password symbols are allowed in this field."
        self.sperr = "The PIN field consists of illegal characters Only numbers are allowed in this field."
        self.fnemp = "The first name cannot be empty."
        self.lnemp = "The last name cannot be empty."
        self.pnemp = "The phone number cannot be empty."
        self.ememp = "The email address cannot be empty."
        self.pwemp = "The password cannot be empty."
        self.spemp = "The PIN cannot be empty."
        self.errar = [self.fnerr, self.lnerr, self.pnerr, self.emerr, self.pwerr, self.sperr]
        self.empar = [self.fnemp, self.lnemp, self.pnemp, self.ememp, self.pwemp, self.spemp]
        self.acmsg = ""
        self.title = "Regular Expression Validator Example v0.01 by t0xic0der"
        self.setupUi(self)
        self.handle_elements()

    def handle_elements(self):
        self.setWindowTitle(self.title)
        self.btn_valid.clicked.connect(self.validnow)

    def activity(self,fname,lname,phnum,email,paswd,sepin):
        valid,error=[-1,-1,-1,-1,-1,-1],""
        valid[0]=validator.vld_fname(fname)
        valid[1]=validator.vld_lname(lname)
        valid[2]=validator.vld_phnum(phnum)
        valid[3]=validator.vld_email(email)
        valid[4]=validator.vld_paswd(paswd)
        valid[5]=validator.vld_sepin(sepin)
        return valid

    def validnow(self):
        attrs=["","","","","",""]
        attrs[0]=self.box_fname.text()
        attrs[1]=self.box_lname.text()
        attrs[2]=self.box_phnum.text()
        attrs[3]=self.box_email.text()
        attrs[4]=self.box_paswd.text()
        attrs[5]=self.box_sepin.text()
        emche=[-1,-1,-1,-1,-1,-1]
        for i in range(6):
            if not attrs[i].strip():
                emche[i]=1
        if 1 in emche:
            self.acmsg=self.ermsg+"\n"
            for i in range(6):
                if emche[i]==1:
                    self.acmsg=self.acmsg+" * "+self.empar[i]+"\n"
            warn = QMessageBox.information(self, self.ertit, self.acmsg, QMessageBox.Ok)
        else:
            array = self.activity(attrs[0],attrs[1],attrs[2],attrs[3],attrs[4],attrs[5])
            if 0 in array:
                self.acmsg=self.ermsg+"\n"
                for i in range(6):
                    if array[i]==0:
                        self.acmsg=self.acmsg+" * "+self.errar[i]+"\n"
                warn = QMessageBox.information(self, self.ertit, self.acmsg, QMessageBox.Ok)
            else:
                warn = QMessageBox.information(self, self.sctit, self.scmsg, QMessageBox.Ok)
        print(emche)

def main():
    app=QApplication(sys.argv)
    QFontDatabase.addApplicationFont("fsrg.ttf")
    QFontDatabase.addApplicationFont("dpcb.ttf")
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()