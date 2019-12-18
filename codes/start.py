import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
import draw_main
import guess_main

class Mainwindow(QWidget):
    def __init__(self):
        width = 640
        height = 480

        QWidget.__init__(self)
        self.setGeometry(300,300,width,height)

        oImage = QImage("./images/background_1.jpg")
        sImage = oImage.scaled(QSize(width, height))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.drawGoBtn = QPushButton("그림그리기",self)
        self.drawGoBtn.setGeometry(50,50,200,50)
        self.guessGoBtn = QPushButton("그림 맞추기", self)
        self.guessGoBtn.setGeometry(400, 50, 200, 50)


        self.drawGoBtn.clicked.connect(self.drawGo)
        self.guessGoBtn.clicked.connect(self.guessGo)

        self.show()

    def drawGo(self):
        self.newWindow = draw_main.CWidget()
    def guessGo(self):
        self.newWindow = guess_main.CWidget()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = Mainwindow()

    sys.exit(app.exec_())