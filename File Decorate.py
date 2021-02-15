""" Import """
from PyQt5 import QtCore, QtGui, QtWidgets
from Image import Image as Image_rc
import os, shutil, sys


""" Object """
class File_Decorate():
    def __init__(self, MainWindow):
        ### Main Window
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(628, 360)
        self.MainWindow.setMaximumSize(QtCore.QSize(630, 360))
        self.MainWindow.setWindowTitle("Decorator")
        self.MainWindow.setStyleSheet("background-image: url(:/Image/Background.jpg);")
		### Central Widget
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow.setCentralWidget(self.centralwidget)
        ### Title
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(199, 50, 233, 36))
        self.Title.setObjectName("Title")
        self.Title.setStyleSheet("background-image: url(:/Image/Title.png);\n"
                                 "border: none;")
        ### Connect
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        ### Call
        self.GUILocation()
        ### Show
        self.FrmLocation.show()
        self.BNext.show()


    ### GUI For Location
    def GUILocation(self):
        ### Frame For Location
        self.FrmLocation = QtWidgets.QFrame(self.centralwidget)
        self.FrmLocation.setGeometry(QtCore.QRect(15, 130, 600, 100))
        self.FrmLocation.setObjectName("FrmLocation")
        self.FrmLocation.setStyleSheet("background-color: #FFFFFF;\n"
                                       "border-radius: 20px;")
        ### Location
        self.Location = QtWidgets.QLineEdit(self.FrmLocation)
        self.Location.setGeometry(QtCore.QRect(20, 50, 500, 30))
        self.Location.setObjectName("Location")
        self.Location.setStyleSheet("background-color: #FFFFFF;\n"
                                    "border-radius: 14.99px;\n"
                                    "font-size: 15px;")
        ### Text
        self.Text = QtWidgets.QLabel(self.FrmLocation)
        self.Text.setGeometry(QtCore.QRect(20, 20, 74, 20))
        self.Text.setObjectName("Text")
        self.Text.setText("Location")
        self.Text.setStyleSheet("background: none;\n"
                                "borde: none;\n"
                                "font-size: 20px;")
		### Browse
        self.BBrowse = QtWidgets.QPushButton(self.FrmLocation)
        self.BBrowse.setGeometry(QtCore.QRect(500, 50, 80, 30))
        self.BBrowse.setObjectName("BBrowse")
        self.BBrowse.clicked.connect(self.DBrowse)
        self.BBrowse.setStyleSheet("QPushButton#BBrowse{\n"
                                  "    background-image: url(:/Image/BBrowse.png);\n"
                                  "    border-radius: 14.99px;\n""}\n"
                                  "QPushButton#BBrowse:focus:pressed{n"
                                  "    background-image: url(:/Image/BBrowseC.png);\n"
                                  "    border-radius: 14.99px;\n""}\n"
                                  "QPushButton#BBrowse:hover{\n"
                                  "    background-image: url(:/Image/BBrowseH.png);\n"
                                  "    border-radius: 14.99px;\n""}")
        ### Warn Nedd
        self.WarnNeed = QtWidgets.QLabel(self.FrmLocation)
        self.WarnNeed.setGeometry(QtCore.QRect(30, 80, 215, 12))
        self.WarnNeed.setObjectName("WarnNeed")
        self.WarnNeed.setText("We must need a location for file decorating")
        self.WarnNeed.hide()
        self.WarnNeed.setStyleSheet("background: none;\n"
                                "borde: none;\n"
                                "font-size: 10px;\n"
                                "color: #FF0000;")
        ### Warn Invalid
        self.WarnInvalid = QtWidgets.QLabel(self.FrmLocation)
        self.WarnInvalid.setGeometry(QtCore.QRect(30, 80, 215, 12))
        self.WarnInvalid.setObjectName("WarnInvalid")
        self.WarnInvalid.setText("We must need a valid location for file decorating")
        self.WarnInvalid.hide()
        self.WarnInvalid.setStyleSheet("background: none;\n"
                                "borde: none;\n"
                                "font-size: 10px;\n"
                                "color: #FF0000;")
		### Next
        self.BNext = QtWidgets.QPushButton(self.centralwidget)
        self.BNext.setGeometry(QtCore.QRect(215, 248, 200, 30))
        self.BNext.setObjectName("BNext")
        self.BNext.setShortcut("Return")
        self.BNext.clicked.connect(self.DNext)
        self.BNext.setStyleSheet("QPushButton#BNext{\n"
                                 "    background-image: url(:/Image/BNext.png);\n"
                                 "    border-radius: 14.99px;\n""}\n"
                                 "QPushButton#BNext:focus:pressed{\n"
                                 "    background-image: url(:/Image/BNextC.png);\n"
                                 "    border-radius: 14.99px;\n""}\n"
                                 "QPushButton#BNext:hover{\n"
                                 "    background-image: url(:/Image/BNextH.png);\n"
                                 "    border-radius: 14.99px;\n""}")
		### Connect
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


    ### GUI For Decorate
    def GUIDecorate(self):
        ### Decorate My File
        self.BDecorateMyFile = QtWidgets.QPushButton(self.centralwidget)
        self.BDecorateMyFile.setGeometry(QtCore.QRect(215, 250, 200, 30))
        self.BDecorateMyFile.setObjectName("BDecorateMyFile")
        self.BDecorateMyFile.setShortcut("Return")
        self.BDecorateMyFile.clicked.connect(self.DDecorateMyFile)
        self.BDecorateMyFile.setStyleSheet("QPushButton#BDecorateMyFile{\n"
                                           "    background-image: url(:/Image/BDecorateMyFile.png);\n"
                                           "    border-radius: 14.99px;\n""}\n"
                                           "QPushButton#BDecorateMyFile:focus:pressed{\n"
                                           "    background-image: url(:/Image/BDecorateMyFileC.png);\n"
                                           "    border-radius: 14.99px;\n""}\n"
                                           "QPushButton#BDecorateMyFile:hover{\n"
                                           "    background-image: url(:/Image/BDecorateMyFileH.png);\n"
                                           "    border-radius: 14.99px;\n""}")
        ##########     Frame For Found     ##########
        self.FrmFound = QtWidgets.QFrame(self.centralwidget)
        self.FrmFound.setGeometry(QtCore.QRect(5, 121, 620, 118))
        self.FrmFound.setObjectName("FrmFound")
        self.FrmFound.setStyleSheet("background-color: #FFFFFF;\n"
                                    "border-radius: 10px;")
        ### Frame For Document
        self.F2Document = QtWidgets.QFrame(self.FrmFound)
        self.F2Document.setObjectName("F2Document")
        self.F2Document.setGeometry(QtCore.QRect(10, 9, 100, 100))
        self.F2Document.setStyleSheet("background: none;")
        # Document Holder
        self.HolderD = QtWidgets.QLabel(self.F2Document)
        self.HolderD.setGeometry(QtCore.QRect(10, 4, 80, 80))
        self.HolderD.setObjectName("HolderD")
        self.HolderD.setStyleSheet("background-image: url(:/Image/Holder.png);\n"
                                   "border-radius:27.6px;")
        # Document Text
        self.TextD = QtWidgets.QLabel(self.F2Document)
        self.TextD.setGeometry(QtCore.QRect(25, 85, 50, 10))
        self.TextD.setObjectName("TextD")
        self.TextD.setText("0")
        self.TextD.setAlignment(QtCore.Qt.AlignCenter)
        self.TextD.setStyleSheet("background: none;\n"
                                 "border: none;")
        # Document Icon        
        self.IconD = QtWidgets.QLabel(self.F2Document)
        self.IconD.setGeometry(QtCore.QRect(23, 17, 55, 55))
        self.IconD.setObjectName("IconD")
        self.IconD.setStyleSheet("background-image: url(:/Image/Document.png);\n"
                                 "border-radius: 0px;")
        ### Frame For Image
        self.F2Image = QtWidgets.QFrame(self.FrmFound)
        self.F2Image.setGeometry(QtCore.QRect(110, 9, 100, 100))
        self.F2Image.setStyleSheet("background: none;")
        self.F2Image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F2Image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F2Image.setObjectName("F2Image")
        # Image Holder
        self.HolderI = QtWidgets.QLabel(self.F2Image)
        self.HolderI.setGeometry(QtCore.QRect(10, 4, 80, 80))
        self.HolderI.setObjectName("HolderI")
        self.HolderI.setStyleSheet("background-image: url(:/Image/Holder.png);\n"
                                   "border-radius:27.6px;")
        # Image Text
        self.TextI = QtWidgets.QLabel(self.F2Image)
        self.TextI.setGeometry(QtCore.QRect(25, 85, 50, 10))
        self.TextI.setObjectName("TextI")
        self.TextI.setText("0")
        self.TextI.setAlignment(QtCore.Qt.AlignCenter)
        self.TextI.setStyleSheet("background: none;\n"
                                 "border: none;")
        # Image Icon
        self.IconI = QtWidgets.QLabel(self.F2Image)
        self.IconI.setGeometry(QtCore.QRect(23, 17, 55, 55))
        self.IconI.setObjectName("IconI")
        self.IconI.setStyleSheet("background-image: url(:/Image/Image.png);\n"
                                 "border-radius: 0px;")
        ### Frame For Video
        self.F2Video = QtWidgets.QFrame(self.FrmFound)
        self.F2Video.setGeometry(QtCore.QRect(210, 9, 100, 100))
        self.F2Video.setStyleSheet("background: none;")
        self.F2Video.setObjectName("F2Video")
        # Video Holder
        self.HolderV = QtWidgets.QLabel(self.F2Video)
        self.HolderV.setGeometry(QtCore.QRect(10, 4, 80, 80))
        self.HolderV.setObjectName("HolderV")
        self.HolderV.setStyleSheet("background-image: url(:/Image/Holder.png);\n"
                                   "border-radius:27.6px;")
        # Video Text
        self.TextV = QtWidgets.QLabel(self.F2Video)
        self.TextV.setGeometry(QtCore.QRect(25, 85, 50, 10))
        self.TextV.setObjectName("TextV")
        self.TextV.setText("0")
        self.TextV.setAlignment(QtCore.Qt.AlignCenter)
        self.TextV.setStyleSheet("background: none;\n"
                                 "border: none;")
        # Video Icon
        self.IconV = QtWidgets.QLabel(self.F2Video)
        self.IconV.setGeometry(QtCore.QRect(23, 17, 55, 55))
        self.IconV.setObjectName("IconV")
        self.IconV.setStyleSheet("background-image: url(:/Image/Video.png);\n"
                                 "border-radius: 0px;")
        ### Frame For Audio
        self.F2Audio = QtWidgets.QFrame(self.FrmFound)
        self.F2Audio.setGeometry(QtCore.QRect(310, 9, 100, 100))
        self.F2Audio.setStyleSheet("background: none;")
        self.F2Audio.setObjectName("F2Audio")
		# Audio Holder
        self.HolderA = QtWidgets.QLabel(self.F2Audio)
        self.HolderA.setGeometry(QtCore.QRect(10, 4, 80, 80))
        self.HolderA.setObjectName("HolderA")
        self.HolderA.setStyleSheet("background-image: url(:/Image/Holder.png);\n"
                                   "border-radius:27.6px;")
		# Audio Text
        self.TextA = QtWidgets.QLabel(self.F2Audio)
        self.TextA.setGeometry(QtCore.QRect(25, 85, 50, 10))
        self.TextA.setObjectName("TextA")
        self.TextA.setText("0")
        self.TextA.setAlignment(QtCore.Qt.AlignCenter)
        self.TextA.setStyleSheet("background: none;\n"
                                 "border: none;")
        # Audio Icon
        self.IconA = QtWidgets.QLabel(self.F2Audio)
        self.IconA.setGeometry(QtCore.QRect(23, 17, 55, 55))
        self.IconA.setObjectName("IconA")
        self.IconA.setStyleSheet("background-image: url(:/Image/Audio.png);\n"
                                 "border-radius: 0px;")
        ### Frame For Software
        self.F2Software = QtWidgets.QFrame(self.FrmFound)
        self.F2Software.setGeometry(QtCore.QRect(410, 9, 100, 100))
        self.F2Software.setStyleSheet("background: none;")
        self.F2Software.setObjectName("F2Software")
		# Software Holder
        self.HolderS = QtWidgets.QLabel(self.F2Software)
        self.HolderS.setGeometry(QtCore.QRect(10, 4, 80, 80))
        self.HolderS.setObjectName("HolderS")
        self.HolderS.setStyleSheet("background-image: url(:/Image/Holder.png);\n"
                                   "border-radius:27.6px;")
        # Software Text
        self.TextS = QtWidgets.QLabel(self.F2Software)
        self.TextS.setGeometry(QtCore.QRect(25, 85, 50, 10))
        self.TextS.setObjectName("TextS")
        self.TextS.setText("0")
        self.TextS.setAlignment(QtCore.Qt.AlignCenter)
        self.TextS.setStyleSheet("background: none;\n"
                                 "border: none;")
        # Software Icon
        self.IconS = QtWidgets.QLabel(self.F2Software)
        self.IconS.setGeometry(QtCore.QRect(23, 17, 55, 55))
        self.IconS.setObjectName("IconS")
        self.IconS.setStyleSheet("background-image: url(:/Image/Software.png);\n"
                                 "border-radius: 0px;")
        ### Frame For Others
        self.F2Others = QtWidgets.QFrame(self.FrmFound)
        self.F2Others.setGeometry(QtCore.QRect(508, 9, 100, 100))
        self.F2Others.setObjectName("F2Others")
        self.F2Others.setStyleSheet("background: none;")
        # Others Holder
        self.HolderO = QtWidgets.QLabel(self.F2Others)
        self.HolderO.setGeometry(QtCore.QRect(10, 4, 80, 80))
        self.HolderO.setObjectName("HolderO")
        self.HolderO.setStyleSheet("background-image: url(:/Image/Holder.png);\n"
                                   "border-radius:27.6px;")
        # Others Text
        self.TextO = QtWidgets.QLabel(self.F2Others)
        self.TextO.setGeometry(QtCore.QRect(25, 85, 50, 10))
        self.TextO.setObjectName("TextS1")
        self.TextO.setText("0")
        self.TextO.setAlignment(QtCore.Qt.AlignCenter)
        self.TextO.setStyleSheet("background: none;\n"
                                  "border: none;")
        # Others Icon
        self.IconO = QtWidgets.QLabel(self.F2Others)
        self.IconO.setGeometry(QtCore.QRect(23, 17, 55, 55))
        self.IconO.setObjectName("IconO")
        self.IconO.setStyleSheet("background-image: url(:/Image/Others.png);\n"
                                 "border-radius: 0px;")
        ### Found
        self.Found = QtWidgets.QLabel(self.centralwidget)
        self.Found.setGeometry(QtCore.QRect(10, 90, 91, 20))
        self.Found.setObjectName("Found")
        self.Found.setText("We Found")
        self.Found.setStyleSheet("background: none;\n"
                                 "borde: none;\n"
                                 "font-size: 20px;")
        ### Connect
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
    

    ### GUI For Completed
    def GUICompleted(self):
        self.BCompleted = QtWidgets.QPushButton(self.centralwidget)
        self.BCompleted.setGeometry(QtCore.QRect(210, 150, 210, 50))
        self.BCompleted.setObjectName("BCompleted")
        self.BCompleted.setText("Completed!")
        self.BCompleted.setShortcut("Return")
        self.BCompleted.clicked.connect(self.DCompleted)
        self.BCompleted.setStyleSheet("background: none;\n"
                                    "borde: none;\n"
                                    "font-size: 40px;")
        ### Connect
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


    ### BBrowse
    def DBrowse(self):
        _ = QtWidgets.QFileDialog.getExistingDirectory(caption="Location")
        self.Location.setText(_)
        ### Checking Location Isn't Empty or Invalid
        if self.Location.text() == '':
            self.WarnNeed.show()
        elif os.path.isdir(self.Location.text()) == False:
            self.WarnInvalid.show()


    ### BNext
    def DNext(self):
        ### Checking Location Isn't Empty or Invalid
        if self.Location.text() == '':
            self.WarnNeed.show()
        elif os.path.isdir(self.Location.text()) == False:
            self.WarnInvalid.show()
        else:
            ### Hide
            self.FrmLocation.hide()
            self.BNext.hide()
            ########################################
            ### File Types
            LDocument_Type = ["docx", "pptx", "pdf", "ai", "txt"]
            LImage_Type = ["jpg", "JPG" "png", "PNG", "gif", "ico"]
            LVideo_Type = ["mp4", "mpg", "dat", "3gp"]
            LAudio_Type = ["mp3", "wav"]
            LSoftware_Type = ["exe", "msi", "bat", "app"]
            ### Folder Names
            self.Document = []
            self.Image = []
            self.Video = []
            self.Audio = []
            self.Software = []
            self.Others = []
            ### Collect FileNames
            LFileNames = os.listdir(self.Location.text())
            ### What Folder Need
            for i in range(len(LFileNames)):
                try:
                    if LFileNames[i][LFileNames[i].index('.')+1:] in LDocument_Type:
                        self.Document.append(LFileNames[i])
                    elif LFileNames[i][LFileNames[i].index('.')+1:] in LImage_Type:
                        self.Image.append(LFileNames[i])
                    elif LFileNames[i][LFileNames[i].index('.')+1:] in LVideo_Type:
                        self.Video.append(LFileNames[i])
                    elif LFileNames[i][LFileNames[i].index('.')+1:] in LAudio_Type:
                        self.Audio.append(LFileNames[i])
                    elif LFileNames[i][LFileNames[i].index('.')+1:] in LSoftware_Type:
                        self.Software.append(LFileNames[i])
                    else:
                        self.Others.append(LFileNames[i])
                except:
                    self.Others.append(LFileNames[i])
            ### Next
            self.GUIDecorate()
            ### Show
            self.FrmFound.show()
            self.Found.show()
            self.BDecorateMyFile.show()
            ### Found
            self.TextD.setText(str(len(self.Document)))
            self.TextI.setText(str(len(self.Image)))
            self.TextV.setText(str(len(self.Video)))
            self.TextA.setText(str(len(self.Audio)))
            self.TextS.setText(str(len(self.Software)))
            self.TextO.setText(str(len(self.Others)))


    ### BDecorateMyFile
    def DDecorateMyFile(self):
        ### Hide
        self.FrmFound.hide()
        self.Found.hide()
        self.BDecorateMyFile.hide()
        ### Make Dir
        self.__Make_Dir("Document")
        self.__Make_Dir("Image")
        self.__Make_Dir("Video")
        self.__Make_Dir("Audio")
        self.__Make_Dir("Software")
        self.__Make_Dir("Others")
        ### Decorate
        for i in range(len(self.Document)):
            self.__Decorate(self.Document[i], "Document")
        for i in range(len(self.Image)):
            self.__Decorate(self.Image[i], "Image")
        for i in range(len(self.Video)):
            self.__Decorate(self.Video[i], "Video")
        for i in range(len(self.Audio)):
            self.__Decorate(self.Audio[i], "Audio")
        for i in range(len(self.Software)):
            self.__Decorate(self.Software[i], "Software")
        for i in range(len(self.Others)):
            self.__Decorate(self.Others[i], "Others")
        ### Decorate My File
        self.GUICompleted()
        self.BCompleted.show()


    ### BCompleted
    def DCompleted(self):
        sys.exit(App.exec_())


    ### Make Dir
    def __Make_Dir(self, Name):
        try:
            os.mkdir(self.Location.text()+'/'+Name)
        except:
            pass


    ### Decorate
    def __Decorate(self, File, Folder):
        try:
            shutil.move(self.Location.text()+'/'+File, self.Location.text()+'/'+Folder)
        except:
            pass


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Ui = File_Decorate(MainWindow)
    MainWindow.show()
    sys.exit(App.exec_())