#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5 import QtWidgets

class Example(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):   
        btn1 = QtWidgets.QPushButton("Button 1", self)   
        btn2 = QtWidgets.QPushButton("Button 2", self) 
        btn1.move(30, 50)  
        btn2.move(150, 50)  

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()
        columns_name = ['Имя', 'Отдел', 'Подразделение', 'телефон', 'сотовый']
        arr = [
                    {'name': 'Maxim', 'otdel': 'It', 'podr': 'It', 'tel': '555', 'sot':'87773434'},
                    {'name': 'Petya', 'otdel': 'GGt', 'podr': 'Asyt', 'tel': '555', 'sot':'87773434'},
                    {'name': 'Kolya', 'otdel': 'Neo', 'podr': 'It', 'tel': '555', 'sot':'87773434'},
                    {'name': 'Vasya', 'otdel': 'Buh', 'podr': 'RR', 'tel': '555', 'sot':'87773434'}
                ]
        self.myTable = QtWidgets.QTableWidget(len(arr), len(columns_name), self)
        self.myTable.setGeometry(0, 100, 400,400)
        self.myTable.setSortingEnabled(True)
        

        self.myTable.setHorizontalHeaderLabels(columns_name)

        
        num = len(arr)-1
        for i in arr:
            print(i['name'])
            print(i['otdel'])
            print(i['podr'])
            print(i['tel'])
            print(i['sot'])
        
        self.one = QtWidgets.QTableWidgetItem('sdlfjsdf')
        for i in range(len(arr)):
            elem = QtWidgets.QTableWidgetItem(arr[i]['name'])
            self.myTable.setItem(i, 0, elem)
            elem = QtWidgets.QTableWidgetItem(arr[i]['otdel'])
            self.myTable.setItem(i, 1, elem)
            elem = QtWidgets.QTableWidgetItem(arr[i]['podr'])
            self.myTable.setItem(i, 2, elem)
            elem = QtWidgets.QTableWidgetItem(arr[i]['tel'])
            self.myTable.setItem(i, 3, elem)
            elem = QtWidgets.QTableWidgetItem(arr[i]['sot'])
            self.myTable.setItem(i, 4, elem)
            num -= 1
        
        
        
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Qtable")
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed ')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
