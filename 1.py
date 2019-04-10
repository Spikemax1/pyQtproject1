#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QToolTip, QApplication, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 15))
        self.setWindowIcon(QIcon('web.png'))
        self.setToolTip("You everybody <b>die</b> here")

        qbnt = QPushButton('Quit', self)
        qbnt.setToolTip('This button to <i>Quit</i>')
        qbnt.clicked.connect(QCoreApplication.instance().quit)
        qbnt.resize(qbnt.sizeHint())
        qbnt.move(50, 50)

        qbnt = QPushButton('NoQuit', self)
        qbnt.setToolTip('This button nothing doing')
        qbnt.resize(qbnt.sizeHint())
        qbnt.move(150, 50)

        self.setWindowTitle('App Quit')
        self.setGeometry(300, 300, 250 , 150)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure?', \
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            event.ignore()
        else:
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())