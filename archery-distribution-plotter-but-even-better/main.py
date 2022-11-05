from PyQt5 import QtCore, QtGui, QtWidgets

# Creates a window containing button and label widgets
# Created with Qt Designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plotter_button = QtWidgets.QPushButton(self.centralwidget)
        self.plotter_button.setGeometry(QtCore.QRect(120, 180, 241, 191))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(12)
        self.plotter_button.setFont(font)
        self.plotter_button.setObjectName("plotter_button")
        self.classification_button = QtWidgets.QPushButton(self.centralwidget)
        self.classification_button.setGeometry(QtCore.QRect(420, 180, 241, 191))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(12)
        self.classification_button.setFont(font)
        self.classification_button.setObjectName("classification_button")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 120, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 510, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.plotter_button.clicked.connect(self.plotter_clicked)
        self.classification_button.clicked.connect(self.classifications_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Archery App", "Archery App"))
        self.plotter_button.setText(_translate("MainWindow", "Open Plotter"))
        self.classification_button.setText(_translate("MainWindow", "Open Classifications"))
        self.label.setText(_translate("MainWindow", "Archery Distribution Plotter and Classification Viewer"))
        self.label_2.setText(_translate("MainWindow", "github.com/corey-richardson"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    def plotter_clicked(self):
        import plotter
        plotter
        
    def classifications_clicked(self):
        import round_classifications
        round_classifications

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
