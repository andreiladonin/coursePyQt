import sys
import time
from PyQt5 import  QtCore, QtWidgets, QtGui

from twoProject import *

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.getText)
        # self.ui.checkBox.clicked.connect(self.output)
        self.ui.radioButton_2.clicked.connect(self.output)
        self.i = 0

    def output(self):
        pass

    def getText(self):

        if self.ui.checkBox.isChecked():
            chekBox_1 = self.ui.checkBox.text()
        else: chekBox_1 = ""

        if self.ui.checkBox_2.isChecked():
            chekBox_2 = self.ui.checkBox_2.text()
        else: chekBox_2 = ""

        if self.ui.radioButton.isChecked():
            radio_1 = self.ui.radioButton.text()
        else: radio_1 = ""

        if self.ui.radioButton_2.isChecked():
            radio_2 = self.ui.radioButton_2.text()
        else: radio_2 = ""

        result = f"{chekBox_1}{chekBox_2}{radio_1}{radio_2}HELLO WORLD"

        self.ui.plainTextEdit.appendPlainText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #это обьект позволяющий вывести объект на экран
    myapp = MyWin()
    # показать окно
    myapp.show()
    # бесконечная прорисовка
    sys.exit(app.exec_())