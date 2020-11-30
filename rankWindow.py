import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QShortcut, QDialog
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPainter, QPalette, QColor, QKeySequence, QPen, QFont

from itemBtn import Button
from item import Item

class RankWindow(QDialog):
    def __init__(self, scoredb):
        super().__init__()
        self.scoredb = scoredb
        self.initUi()

    def initUi(self):
        # Window Backgrond
        palette = QPalette()
        palette.setColor( QPalette.Background , QColor(251, 248, 239))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setGeometry(700,200,540,670)
        self.setFixedSize(self.rect().size())
        self.setWindowTitle("2048 Game")

        # menu button
        menu = Item().itemGroup['menuBtn']
        menuBtn = Button(menu['img'], menu['size'])
        menuBtn.setFixedSize(50,50)
        menuBtn.clicked.connect(self.showMenuwindow)

        # rankLabel, scoreLabel
        font = QLabel().font()
        font.setFamily('맑은 고딕')
        font.setBold(True)
        font.setPointSize(font.pointSize() + 5)

        rankLayout = QGridLayout()

        ml = [(1,0),(1,1),(7,0),(7,1)]
        sl = [(0,0),(0,1),(6,0),(6,1)]
       
        for idx in range(4):
            scoreText = ''
            rankLabel, sizeLabel = QLabel(), QLabel()

            sizeScore = self.scoredb[idx]
            for rank, score in enumerate(sizeScore['score']):
                if score == 0: break
                scoreText += str(rank+1)+'위\t'+str(score)+'점\n'
            
            rankLabel.setText(scoreText)
            rankLabel.setStyleSheet('border-style:solid; border-width:4px; border-color:rgb(187, 173, 160); border-radius:10px; color:rgb(118, 109, 100);')
            rankLabel.setFont(font)
            rankLabel.setAlignment(Qt.AlignCenter)

            sizeText = str(sizeScore['size'])+' x '+str(sizeScore['size'])
            sizeLabel.setText(sizeText)
            sizeLabel.setStyleSheet('background-color:rgb(187, 173, 160); color:white')
            sizeLabel.setFont(font)
            sizeLabel.setAlignment(Qt.AlignCenter)
            
            rankLayout.addWidget(sizeLabel, sl[idx][0], sl[idx][1])
            rankLayout.addWidget(rankLabel, ml[idx][0], ml[idx][1], 5, 1)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(menuBtn)
        mainLayout.addLayout(rankLayout)

        self.setLayout(mainLayout)
        self.show()

    def showMenuwindow(self):
        self.close() # go back to main window