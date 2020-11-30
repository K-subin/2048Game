import sys

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

from itemBtn import Button
from item import Item
from gameWindow import GameWindow
from rankWindow import RankWindow

import pickle

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.dbfilename = 'scoreDB.dat'
        self.scoredb = []
        self.readScoreDB()
        
        self.initUI()
    
    def initUI(self):
        # Window Backgrond
        palette = QPalette()
        palette.setColor( QPalette.Background , QColor(251, 248, 239))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.setGeometry(700,200,540,670)
        self.setFixedSize(self.rect().size())
        self.setWindowTitle("2048 Game")

        self.N = 3
        self.mapsizeText = [str(i)+"x"+str(i) for i in range(3,7)]
        self.mapsizeLabel = QLabel(self.mapsizeText[0])

        font = self.mapsizeLabel.font()
        font.setFamily('맑은 고딕')
        font.setBold(True)
        font.setPointSize(font.pointSize() + 10)
        self.mapsizeLabel.setStyleSheet('color: rgb(118,109,100);')
        self.mapsizeLabel.setFont(font)
        
        self.itemGroup = Item().itemGroup
        self.mapPhoto = self.itemGroup['mapPhoto']
        arrow = self.itemGroup['arrow']
        start = self.itemGroup['startBtn']
        rank = self.itemGroup['rankBtn']

        # mapPhoto button
        self.mapPhotoBtn = Button(self.mapPhoto['img'][0], self.mapPhoto['size'])
        self.mapPhotoBtn.setStyleSheet('background:transparent')

        # arrow button
        arrowBtn = []
        arrowText = ['Left','Right']
        for i in range(2):
            arrowButton = Button(arrow['img'][i], arrow['size'])
            arrowButton.setStyleSheet('background:transparent')
            arrowButton.setObjectName(arrowText[i])
            arrowButton.clicked.connect(self.sizeFunc)
            arrowBtn.append(arrowButton)

        # start button
        startBtn = Button(start['img'], start['size'])
        startBtn.clicked.connect(self.showGamewindow)
        startBtn.setStyleSheet('background:transparent')

        # rank button
        rankBtn = Button(rank['img'], rank['size'])
        rankBtn.clicked.connect(self.showRankwindow)
        rankBtn.setStyleSheet('background:transparent')

        # Layout
        hSizebox = QHBoxLayout()
        hSizebox.addWidget(arrowBtn[0])
        hSizebox.addStretch(1)
        hSizebox.addWidget(self.mapsizeLabel)
        hSizebox.addStretch(1)
        hSizebox.addWidget(arrowBtn[1])

        # mainLayout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.mapPhotoBtn)
        mainLayout.addStretch(1)
        mainLayout.addLayout(hSizebox)
        mainLayout.addStretch(1)
        mainLayout.addWidget(startBtn)
        mainLayout.addWidget(rankBtn)

        self.setLayout(mainLayout)

        self.setContentsMargins(100,30,100,30)
        self.show()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            self.scoredb = []
            return
  
        fH.close()

    def sizeFunc(self):
        
        if self.sender().objectName() == 'Left':
            if self.N == 3:
                self.N = 6
            else:
                self.N -= 1
        elif self.sender().objectName() == 'Right':
            if self.N == 6:
                self.N = 3
            else:
                self.N += 1
            
        self.mapPhotoBtn.setImg(self.mapPhoto['img'][self.N-3])
        self.mapsizeLabel.setText(self.mapsizeText[self.N-3]) 

    def showGamewindow(self):
        self.hide() # hide main window
        self.gameWindow = GameWindow(self.N, self.scoredb)
        self.gameWindow.exec()
        self.show()

    def showRankwindow(self):
        self.hide() # hide main window
        self.rankWindow = RankWindow(self.scoredb)
        self.rankWindow.exec()
        self.show()
