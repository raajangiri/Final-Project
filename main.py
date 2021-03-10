import webbrowser

from PyQt5 import QtGui
from PyQt5.QtCore import QRect


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton, QWidget, QPlainTextEdit, QLabel, QFileDialog
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "CybeX ML Powered Antivirus"
        self.top = 1000
        self.left = 1000
        self.width = 1500
        self.height = 1100
        # self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(0,0,1900,1100)
        self.setFixedSize(1900, 1100)



        self.setStyleSheet('background-color:white')

        frameBlack = QFrame(self)
        frameBlack.setFrameShape(QFrame.StyledPanel)
        frameBlack.setStyleSheet("background-color:black")
        frameBlack.setGeometry(0,0,400,1100)
        # frameBlack.groupBox=QGroupBox()
        labelImage = QLabel(frameBlack)
        labelImage.setGeometry(0, 630, 400, 400)
        pixmap = QPixmap("Image/VirusLogo.png")
        labelImage.setPixmap(pixmap)

        self.DashBoard()
        self.Frames()

        # WORK OF BUTTON
        btnDashBoard = QPushButton(self)
        btnDashBoard.setText("DashBoard")
        btnDashBoard.setGeometry(0,100 , 400, 100)
        btnDashBoard.setStyleSheet("QPushButton"
                             "{"
                             "background-color : black;color: white;border: 1px solid white"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : pink;"
                             "}")
        btnDashBoard.clicked.connect(self.DashBoard)
        btnDashBoard.setIcon(QtGui.QIcon("Image/dashboard.png"))
        btnScan = QPushButton(self)
        btnScan.setText("Scan")
        btnScan.setGeometry(0,200 , 400, 100)
        btnScan.setStyleSheet("QPushButton"
                             "{"
                             "background-color : black;color: white;border: 1px solid white"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : pink;"
                            "}")

        btnScan.clicked.connect(self.Scan)

        btnAbout = QPushButton(self)
        btnAbout.setText("About")
        # btnAbout.setStyleSheet("tect-color:white")
        btnAbout.setGeometry(0,300 , 400, 100)
        btnAbout.setStyleSheet("QPushButton"
                             "{"
                             "background-color : black;color: white;border: 1px solid white"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : pink;"
                             "}")
        btnAbout.setIcon(QtGui.QIcon("Image/about.png"))
        btnAbout.clicked.connect(self.About)
        btnSetting = QPushButton(self)
        btnSetting.setText("Setting")
        btnSetting.setGeometry(0,400 , 400, 100)
        btnSetting.setIcon(QtGui.QIcon("Image/setting.png"))
        btnSetting.setStyleSheet("QPushButton"
                             "{"
                             "background-color : black;color: white;border: 1px solid white"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color :pink;"
                             "}")
        btnSetting.setIcon(QtGui.QIcon("Image/setting.png"))
        btnSetting.clicked.connect(self.Setting)

        btnHelp = QPushButton(self)
        btnHelp.setText("Help")
        btnHelp.setGeometry(0,500 , 400, 100)

        btnHelp.setStyleSheet("QPushButton"
                             "{"
                             "background-color : black;color: white;border: 1px solid white"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color :pink;"
                             "}")
        btnHelp.setIcon(QtGui.QIcon("Image/help.png"))
        btnHelp.clicked.connect(self.Help)

        self.show()
    def DashBoard(self):
        DbFrame = QFrame(self)
        DbFrame.setFrameShape(QFrame.StyledPanel)
        DbFrame.setStyleSheet("background-color:#353007")
        DbFrame.setGeometry(400,100, 1500, 1000)

        label = QLabel(DbFrame)
        label.setGeometry(600,0,500,90)
        label.setText("<h1>   Welcome To</h1>")
        label.setStyleSheet("color:blue")

        label1 = QLabel(DbFrame)
        label1.setGeometry(360,70, 900, 90)
        label1.setText("<h1>CybeX ML Powered Antivirus</h1>")
        label1.setStyleSheet("color:blue")

        label2 = QLabel(DbFrame)
        label2.setGeometry(0,850, 200, 40)
        label2.setText("<h3>Raajan Giri</h3>")
        label2.setStyleSheet("color:red")

        label3 = QLabel(DbFrame)
        label3.setGeometry(0, 900, 222, 40)
        label3.setText("<h3>Mohit Bhatta</h3>")
        label3.setStyleSheet("color:yellow")

        label3 = QLabel(DbFrame)
        label3.setGeometry(0,950, 290, 40)
        label3.setText("<h3>Pranav Pudasaini</h3>")
        label3.setStyleSheet("color:green")

        labelImage = QLabel(DbFrame)
        labelImage.setGeometry(300,150, 1000, 900)
        pixmap = QPixmap("Image/BigLogo.png")
        # labelImage.setStyleSheet("background-color : black;color:green")
        labelImage.setPixmap(pixmap)
        DbFrame.show()

    def Scan(self):
        SFrame = QFrame(self)
        SFrame.setFrameShape(QFrame.StyledPanel)
        SFrame.setStyleSheet("background-color:pink")
        SFrame.setGeometry(400, 100, 1500, 1000)

        labelImage = QLabel(SFrame)
        # labelImage.setGeometry(0,400, 1000, 900)
        labelImage.move(0,650)
        pixmap = QPixmap("Image/icon.jpg")
        labelImage.setStyleSheet("background-color : black;color:green")
        labelImage.setPixmap(pixmap)

        labelImage1 = QLabel(SFrame)
        # labelImage.setGeometry(0,400, 1000, 900)
        labelImage1.move(750,650)
        pixmap1 = QPixmap("Image/icon1.jpg")
        labelImage1.setStyleSheet("background-color : black;color:green")
        labelImage1.setPixmap(pixmap1)

        btnSelect = QPushButton(SFrame)
        btnSelect.setText("Select")
        btnSelect.setGeometry(0, 500, 400, 100)

        btnSelect.setStyleSheet("QPushButton"
                              "{"
                              "background-color :Blue;color: white;border: 1px solid white"
                              "}"
                              "QPushButton::pressed"
                              "{"
                              "background-color :pink;"
                              "}")
        btnSelect.clicked.connect(self.Select)

        btn = QPushButton(SFrame)
        btn.setText("Scan")
        btn.setGeometry(1000, 500, 400, 100)

        btn.setStyleSheet("QPushButton"
                                "{"
                                "background-color :Blue;color: white;border: 1px solid white"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color :pink;"
                                "}")
        btn.clicked.connect(lambda: webbrowser.open('http://www.google.com'))



        SFrame.show()

    def Help(self):
        HFrame = QFrame(self)
        HFrame.setFrameShape(QFrame.StyledPanel)
        # HFrame.setStyleSheet("background-color:pink;background-image : url(Image/BigLogo.png);background-repeat: no-repeat; background-position: center")
        HFrame.setGeometry(400, 100, 1500, 1000)

        label = QLabel("<body>If you need any  help regarding technical issue you are kindely requested "
                       "to send us mail and please give us feedback as it will help us to imorove our product and focus"
                       " on most important issue for you , and fix most usability problems.<br><br>"
                       "<h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                       "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                       "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mail Us at:</h1></body>",HFrame)
        label.setWordWrap(True)
        label.setGeometry(0, 0, 1500,1000)
        label.setStyleSheet(
            "background-color:pink;background-image : url(Image/BigLogo.png);background-repeat: no-repeat; background-position: center;color:rgb(0,0,0)")

        label2=QLabel(HFrame)
        label2.setText("pranavpudasaini01@gmail.com<br>raajan.giri496@gmail.com<br>mohitbhatta9@gmail.com")
        label2.setStyleSheet("font-style: italic;color:blue;background-color: rgba(255, 255, 255, 10)")
        label2.setGeometry(440,750,600,100)
        l=QLabel(HFrame)
        l.setText("<h2>Are you experiencing any technical difficulties or do<br> you want to give us feedback?</h2>")
        l.setStyleSheet("background-color:rgba(255, 255, 255, 10);color:red")
        l.setGeometry(0,0,1400,100)

        HFrame.show()

    def About(self):

        AbFrame = QFrame(self)
        AbFrame.setStyleSheet("background-color:pink;background-image : url(Image/BigLogo.png);background-repeat: no-repeat; background-position: center")
        AbFrame.setFrameShape(QFrame.StyledPanel)
        # AbFrame.setStyleSheet("background-color:rgb(200,200,200)")
        AbFrame.setGeometry(400, 100, 1500, 1000)

        label=QLabel("<body><h3>"
                             "Cybex is a set of software programs designed to identify and prevent "
                             "users from viruses and malwares,spams, exploits, as well as phishing, by "
                             "using state-fo-the art Machine Learning models and techniques. <br><br><br>"
                             ""
                             ""
                             "The objective of this project is to make a security tool "
                             "that protect the users from malware like trojans, spywares, RATs, "
                             "crypto-miners, password stealers, exploit kits, ransomwares as well as "
                             "phishing prevention, intrusion detection, and spam classification using "
                             "modern Machine-Learning approaches. The ultimate product is the suite of tools"
                             " that can reliably detect various categories of malwares.</h3></body>",AbFrame)
        label.setWordWrap(True)
        label.setGeometry(0,0,1500,1000)
        AbFrame.show()

    def Setting(self):
        SeFrame = QFrame(self)
        SeFrame.setFrameShape(QFrame.StyledPanel)
        SeFrame.setStyleSheet("background-color:white")
        SeFrame.setGeometry(400, 100, 1500, 1000)
        SeFrame.show()

    def Select(self):
        QFileDialog.getOpenFileName()
        # QFileDialog.setFilter()

    def Frames(self):
        framePurple = QFrame(self)
        framePurple.setFrameShape(QFrame.StyledPanel)
        framePurple.setStyleSheet("background-color:purple")
        framePurple.setGeometry(400,0, 1500, 100)
        label=QLabel(framePurple)
        label.setText("<h1>CybeX</h1>")
        label.setStyleSheet("color:White")
        label.setGeometry(0,10,200,65)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())