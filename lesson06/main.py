import sys
import time
from PyQt5 import  QtCore, QtWidgets, QtGui
from dis_main import *
from dis_modal import Ui_Form

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.modal)

    def modal(self):
        window = Modal_Win(self)
        window.show()

class Modal_Win(QtWidgets.QWidget):
    def __init__(self, parent=MyWin):
        # QtCore.Qt.Window - чтобы модальное оконо не показалось в родительском окне
        super().__init__(parent, QtCore.Qt.Window)
        self.modal = Ui_Form()
        self.modal.setupUi(self)
        # setWindowModality - чтоб другие окна зблокировалось
        self.setWindowModality(2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #это обьект позволяющий вывести объект на экран
    myapp = MyWin()
    # показать окно
    myapp.show()
    # бесконечная прорисовка
    sys.exit(app.exec_())