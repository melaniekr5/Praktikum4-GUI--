import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle(' ')

        self.showTittle = QCheckBox()
        self.showTittle.setText('Show Title')
        self.showTittle.stateChanged.connect(self.cek)

        layout = QVBoxLayout()
        layout.addWidget(self.showTittle)

        self.setLayout(layout)

    def cek(self):
        if self.showTittle.isChecked():
            self.setWindowTitle('Contoh QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
