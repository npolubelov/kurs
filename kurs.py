#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMainWindow, QLabel, QHBoxLayout, 
    QVBoxLayout, QLineEdit, QTextEdit, QLCDNumber, QSlider, 
    QInputDialog, QAction, QFileDialog, QCheckBox, QTextEdit)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtCore import (QCoreApplication, Qt)
import csv
import codecs

class energy:
 
    def __init__(self, name, price, energytype, objectof, mdiffrnce):
        self.name = name
        self.price = price  
        self.energytype = energytype  
        self.objectof = objectof
        self.mdiffrnce = mdiffrnce   

    def __repr__(self):
        return '\nНазвание энергосберегающего мероприятия = {} \nСтоимость проведения мероприятия = {} \nТип затрагиваемого энергетического ресурса = {} \nОбъект, на котором будет проводится мероприятие = {} \nЭкономия на ресурсе в месяц после приминения мероприятия = {}\n'.format(self.name, self.price, self.energytype, self.objectof, self.mdiffrnce)

    def display_info(self):
        print("\nНазвание энергосберегающего мероприятия - ",self.name)
        print("Стоимость проведения мероприятия - ",self.price)
        print("Тип затрагиваемого энергетического ресурса - ",self.energytype)
        print("Объект, на котором будет проводится мероприятие - ",self.objectof)
        print("Экономия на ресурсе в месяц после приминения мероприятия - ",self.mdiffrnce,"\n")
 
    def ocup(self):
        self.oc = self.price // self.mdiffrnce
        return "\nСрок окупаемости мероприятия с названием %s %s месяц(ев)" % (self.name, self.oc) 
    
    def percentof(self):
        self.prc = self.mdiffrnce / self.price * 100
        return "\nЭкономия на ресурс в месяц состовляет %s процента от стоимости мероприятия %s" % (self.prc, self.name)

class Example(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton('Подключить CSV', self)
        btn1.move(10, 10)
        btn1.resize(780,30)
        btn1.clicked.connect(self.buttonClicked1)

        self.textbox = QTextEdit(self)
        self.textbox.move(10, 50)
        self.textbox.resize(780,600)

        btn2 = QPushButton('Расчитать срок окупаемости мероприятия', self)
        btn2.move(10, 660)
        btn2.resize(390,30)
        btn2.clicked.connect(self.buttonClicked2)

        btn3 = QPushButton('Расчитать экономию на ресурс в месяц', self)
        btn3.move(400, 660)
        btn3.resize(390,30)
        btn3.clicked.connect(self.buttonClicked3)

        btn4 = QPushButton('Сохранить результат в CSV', self)
        btn4.move(10, 700)
        btn4.resize(780,30)

        self.setGeometry(0, 0, 800, 740)
        self.setWindowTitle('Формирование энергосберегающих мероприятий')
        self.show()
    
    def buttonClicked1(self):
        import sqlite3
        conn = sqlite3.connect('lab3.db')
        c = conn.cursor()
        c.execute("SELECT * FROM table1 WHERE s_price='545999'")
        row = c.fetchone() 
        exmpl1 = energy(row[0],row[1],row[2],row[3],row[4])
        self.textbox.setText('\nНазвание энергосберегающего мероприятия = {} \nСтоимость проведения мероприятия = {} \nТип затрагиваемого энергетического ресурса = {} \nОбъект, на котором будет проводится мероприятие = {} \nЭкономия на ресурсе в месяц после приминения мероприятия = {}\n'.format(exmpl1.name, exmpl1.price, exmpl1.energytype, exmpl1.objectof, exmpl1.mdiffrnce))
        onb=3
        return onb,exmpl1

    def buttonClicked2(self):
        if (onb<1):
            self.textbox.setText('Ошибка, не был подключен CSV файл')
        elif (onb>2):
            self.textbox.setText(exmpl1.ocup())

    def buttonClicked3(self):
        if (onb<1):
            self.textbox.setText('Ошибка, не был подключен CSV файл')
        elif (onb>2):
            self.textbox.setText(exmpl1.percentof())

if __name__ == '__main__':

    onb=0
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    