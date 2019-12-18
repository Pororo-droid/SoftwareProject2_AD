import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import getImage

class CWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.Images,self.Answers = getImage.getImages()
        self.Answer = self.Answers[0]
        self.Image = self.Images[0]
        #print(Images)
        #print(Answers)

        self.formbox = QHBoxLayout()
        self.setLayout(self.formbox)

        left = QVBoxLayout()
        self.right = QVBoxLayout()

        #그룹박스1 사용자의 정답
        gb = QGroupBox('사용자 정답:')
        left.addWidget(gb)

        vbox = QVBoxLayout()
        gb.setLayout(vbox)

        self.userAnswer = QLineEdit()

        vbox.addWidget(self.userAnswer)
        #left.addStretch(0)

        guessBtn = QPushButton("Submit")
        passBtn = QPushButton("Pass")

        vbox.addWidget(guessBtn)
        vbox.addWidget(passBtn)

        guessBtn.clicked.connect(self.submitClicked)
        passBtn.clicked.connect(self.passClicked)

        #그룹박스2 사용자의 점수
        self.score = 0

        gb = QGroupBox('사용자의 점수')
        self.userScore = QLineEdit()

        left.addWidget(gb)

        hbox = QHBoxLayout()
        hbox.addWidget(self.userScore)
        gb.setLayout(hbox)

        self.userScore.setText(str(self.score))

        #PROGRESS BAR
        gb = QGroupBox('진행률')
        self.progress = 0
        self.progressBar = QProgressBar()

        left.addWidget(gb)

        hbox = QHBoxLayout()
        hbox.addWidget(self.progressBar)
        gb.setLayout(hbox)

        #오른쪽 레이아웃 박스에 그래픽 뷰 추가
        self.pixmap = QPixmap(self.Image)
        self.pixmap = self.pixmap.scaledToHeight(450)
        self.view = QLabel()
        self.view.setPixmap(self.pixmap)
        self.right.addWidget(self.view)

        self.formbox.addLayout(left)
        self.formbox.addLayout(self.right)

        self.formbox.setStretchFactor(left, 0)

        self.formbox.setStretchFactor(self.right, 1)

        self.setGeometry(300, 300, 800, 500)
        self.show()

    def submitClicked(self):
        if self.userAnswer.text() == self.Answer:
            self.progress += 20
            self.progressBar.setValue(self.progress)
            if self.progress == 100:
                self.userScore.setText('당신의 최종 스코어 :'+str(self.score+1))
                return
            #print(self.Images)
            del self.Answers[0]
            del self.Images[0]
            self.Answer =self.Answers[0]
            self.Image = self.Images[0]
            #print(self.Image)
            self.pixmap = QPixmap(self.Image)
            self.pixmap = self.pixmap.scaledToHeight(450)
            self.view.setPixmap(self.pixmap)

            self.score+=1
            self.userScore.setText(str(self.score))


    def passClicked(self):
        del self.Answers[0]
        del self.Images[0]
        self.Answer = self.Answers[0]
        self.Image = self.Images[0]
        # print(self.Image)
        self.pixmap = QPixmap(self.Image)
        self.pixmap = self.pixmap.scaledToHeight(450)
        self.view.setPixmap(self.pixmap)

        self.progress += 20
        self.progressBar.setValue(self.progress)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())