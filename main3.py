import sys
import time
from PyQt5 import  QtCore, QtWidgets, QtGui
from project3 import *

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.number = 0
        # индекс нашей строки
        self.table_index = 0
        # количество наших строк
        self.row_count = 1
        self.ui.pushButton.clicked.connect(self.add_item)
        self.ui.pushButton_2.clicked.connect(self.clear_all)
        self.ui.pushButton_3.clicked.connect(self.add_in_table)
        self.ui.pushButton_4.clicked.connect(self.clear_tbl)

    def add_item(self):
        radio_base = [
            self.ui.radioButton,
            self.ui.radioButton_2,
            self.ui.radioButton_3,
            self.ui.radioButton_4
        ]

        for radio in radio_base:
            if radio.isChecked():
                name = radio.text()

                icon = QtGui.QIcon(f"{name}.png")
                self.ui.listWidget.addItem(f"{name} - {self.number}")
                # поставить курсор на текущюю  строку
                self.ui.listWidget.setCurrentRow(self.number)
                # выбрать текущий элемент
                item = self.ui.listWidget.currentItem()
                # устоновить иконку
                item.setIcon(icon)
                self.number += 1

    def clear_all(self):
        self.number = 0
        self.ui.listWidget.clear()

    def add_in_table(self):
        ID = None
        Name = None
        Age = None

        if len(self.ui.lineEdit.text()) > 0:
            ID = self.ui.lineEdit.text()
        else:
            return
        if len(self.ui.lineEdit_2.text()) > 0:
            Name = self.ui.lineEdit_2.text()
        else:
            return
        if len(self.ui.lineEdit.text()) > 0:
            Age = self.ui.lineEdit_3.text()
        else:
            return

        # SetRowCount устанавливает длина таблички
        self.ui.tableWidget.setRowCount(self.row_count)
        # SetItem устанавливает значения
        self.ui.tableWidget.setItem(self.table_index, 0, QtWidgets.QTableWidgetItem(ID))
        self.ui.tableWidget.setItem(self.table_index, 1, QtWidgets.QTableWidgetItem(Name))
        self.ui.tableWidget.setItem(self.table_index, 2, QtWidgets.QTableWidgetItem(Age))
        self.row_count += 1
        self.table_index += 1

    def clear_tbl(self):
        self.table_index = 0
        # количество наших строк
        self.row_count = 1
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.ui.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("NAME"))
        self.ui.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("AGE"))
        self.ui.tableWidget.setRowCount(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #это обьект позволяющий вывести объект на экран
    myapp = MyWin()
    # показать окно
    myapp.show()
    # бесконечная прорисовка
    sys.exit(app.exec_())