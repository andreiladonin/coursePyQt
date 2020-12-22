import sys
import time
from PyQt5 import  QtCore, QtWidgets, QtGui
from less5 import *

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.step = 0

        self.ui.pushButton.clicked.connect(self.add_comboBox)
        self.ui.pushButton_2.clicked.connect(self.dellItemCombox)

    def add_comboBox(self):
        text = self.ui.lineEdit.text()

        if len(text) == 0:
            self.ui.plainTextEdit.appendPlainText("Введите значение")
        else:
            if self.ui.progressBar.value() == 100:
                self.ui.plainTextEdit.appendPlainText("список заполнен")
                return
            if self.checkItemComboBox(text):
                self.ui.plainTextEdit.appendPlainText("Значение уже есть!!")
                return
            if self.ui.progressBar.value() < 100:
                self.ui.comboBox.addItem(text)
                self.ui.plainTextEdit.appendPlainText("Добавлено значение")
                self.step += 25
                self.ui.progressBar.setValue(self.step)


    def checkItemComboBox(self, text):
        flag = False
        for count in range(self.ui.comboBox.count()):
            if self.ui.comboBox.itemText(count) == text:
                flag = True
        return flag

    def dellItemCombox(self):
        text = self.ui.comboBox.currentIndex()
        self.ui.comboBox.removeItem(text)
        self.step -= 25
        self.ui.progressBar.setValue(self.step)
        self.ui.plainTextEdit.appendPlainText("Удалено значение")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #это обьект позволяющий вывести объект на экран
    myapp = MyWin()
    # показать окно
    myapp.show()
    # бесконечная прорисовка
    sys.exit(app.exec_())