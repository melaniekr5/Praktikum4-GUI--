import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Latihan ComboBox')

        self.combo = QComboBox()
        self.combo.addItem('--Pilih Makanan--')
        self.combo.addItem('Mendoan')
        self.combo.addItem('Cireng')
        self.combo.addItem('Gethuk')
        self.combo.addItem('Tahu Bulat')
        self.combo.addItem('Ketan Susu')

        self.combo1 = QComboBox()
        self.combo1.addItem('--Pilih Minuman--')
        self.combo1.addItem('Es Cincau')
        self.combo1.addItem('Milshake')
        self.combo1.addItem('Chatime')
        self.combo1.addItem('Thaitea')
        self.combo1.addItem('Kopi Hitam')

        self.getTextButton = QPushButton('Pilihan Anda')

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.combo1)
        layout.addWidget(self.getTextButton)

        layout.addStretch()
        self.setLayout(layout)

        self.getTextButton.clicked.connect(self.getTextButtonClick)

    def getTextButtonClick(self):
        QMessageBox.information(self, 'Informasi','Anda memilih: ' + self.combo.currentText() + " & " + self.combo1.currentText())

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
