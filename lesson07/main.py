import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from dis import Ui_MainWindow

class MY_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_File)
        self.ui.pushButton_3.clicked.connect(self.open_Files)
        self.ui.pushButton_2.clicked.connect(self.save_file)
        self.ui.pushButton_5.clicked.connect(self.open_folder)
        self.ui.pushButton_4.clicked.connect(self.color)

    def open_File(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Python File *.py\nВсе файлы (*)")
        print("hi")
        # fil = open(file[0], "r")
        # with fil as f:
        #     print(f.readlines())

    def open_Files(self):
        file = QtWidgets.QFileDialog.getOpenFileNames(self, "Open Files", "", "Python File *.py\nВсе файлы (*)")
        print(file)

    def save_file(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Txt File *.txt\nВсе файлы (*)")
        print(file)
        with open(file[0], "w") as f:
            f.write("STEPA LOH")

    def open_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self)
        print(folder)
    def color(self):

        color = QtWidgets.QColorDialog(self).getColor()
        print(color.getRgb())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = MY_Window()
    my_app.show()
    sys.exit(app.exec_())