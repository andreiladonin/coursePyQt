import sys
import time
from PyQt5 import  QtCore, QtWidgets, QtGui
from fir_project import *

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.handler)

    def handler(self):
        self.ui.pushButton.setDisabled(1)

        self.ui.plainTextEdit.appendPlainText("test")
        self.ui.label.setText("text")
#ЭТО ЧТОБ НЕ ЭКСПОРТИРОВАЛИ КАК БИБЛИОТЕКУ
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #это обьект позволяющий вывести объект на экран
    myapp = MyWin()
    # показать окно
    myapp.show()
    # бесконечная прорисовка
    sys.exit(app.exec_())