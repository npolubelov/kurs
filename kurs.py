#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMainWindow, QLabel, QHBoxLayout, 
    QVBoxLayout, QLineEdit, QTextEdit, QLCDNumber, QSlider, 
    QInputDialog, QAction, QFileDialog, QCheckBox)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtCore import (QCoreApplication, Qt)

class Example(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton('Подключить CSV', self)
        btn1.move(10, 10)
        btn1.resize(780,30)

        self.textbox = QLineEdit(self)
        self.textbox.move(10, 50)
        self.textbox.resize(780,600)

        btn2 = QPushButton('Расчитать срок окупаемости мероприятия', self)
        btn2.move(10, 660)
        btn2.resize(390,30)

        btn3 = QPushButton('Расчитать экономию на ресурс в месяц', self)
        btn3.move(400, 660)
        btn3.resize(390,30)

        btn4 = QPushButton('Сохранить результат в CSV', self)
        btn4.move(10, 700)
        btn4.resize(780,30)

        self.setGeometry(0, 0, 800, 740)
        self.setWindowTitle('Формирование энергосберегающих мероприятий')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())