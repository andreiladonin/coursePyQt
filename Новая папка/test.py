import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar, QVBoxLayout, QApplication
import requests

class Thread(QThread):
    _signal = pyqtSignal(int)

    def __init__(self, url):
        super(Thread, self).__init__()
        self.url = url
    def __del__(self):
        self.wait()

    def run(self):
        url = self.url
        r = requests.get(url)
        i = 0
        while i < 100:
            
            with open("tutorial1.apk", "wb") as code:
                code.write(r.content)
            i+=1
            self._signal.emit(i)
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.setWindowTitle('QProgressBar')
        self.btn = QPushButton('Click me')
        self.btn.clicked.connect(self.btnFunc)
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.resize(300, 100)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.pbar)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)
        self.show()

    def btnFunc(self):
        url = "http://tegra3.icu/files/1151/hill-climb-racing_v1.48.0_tegra3.net.apk"
        self.thread = Thread(url=url)
        
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        self.btn.setEnabled(False)

    def signal_accept(self, msg):
        self.pbar.setValue(int(msg))
        if self.pbar.value() == 99:
            self.pbar.setValue(0)
            self.btn.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())