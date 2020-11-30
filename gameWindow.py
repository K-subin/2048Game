import sys

from PyQt5.QtWidgets import QWidget, QLabel, QShortcut, QDialog
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPainter, QPalette, QColor, QKeySequence
from PyQt5.QtCore import Qt, QRect

from item import Item
from itemBtn import Button
from gameMap import CMap

from copy import copy
import pickle

class GameWindow(QDialog):
    def __init__(self, N, scoredb):
        super().__init__()
        self.N = N
        self.dbfilename = 'scoreDB.dat'
        self.scoredb = scoredb
        for sizeScore in self.scoredb:
            if sizeScore['size'] == self.N:
                self.sizeScoredb = sizeScore['score']
        
        self.initUi()    
        
    def initUi(self):
        
        # Game Window Backgrond
        palette = QPalette()
        palette.setColor( QPalette.Background , QColor(251, 248, 239))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        
        # Game Window Setting
        self.setGeometry(700,200,540,670)
        self.setWindowTitle("2048 Game")
        self.setFixedSize(self.rect().size())
        self.setContentsMargins(10,0,10,0)

        # widget
        title = QLabel("2048")
        self.scoreText = QLabel('SCORE\n0')
        self.scoreText.setAlignment(Qt.AlignCenter)
        self.scoreText.setContentsMargins(10,0,10,0)
        self.scoreText.setStyleSheet('background-color:rgb(187, 173, 160); color:white')
        
        self.bestScore = QLabel('BEST\n'+str(self.sizeScoredb[0]))
        self.bestScore.setAlignment(Qt.AlignCenter)
        self.bestScore.setContentsMargins(10,0,10,0)
        self.bestScore.setStyleSheet('background-color:rgb(187, 173, 160); color:white')

        font = title.font()
        font.setFamily('Times New Roman')
        font.setBold(True)
        font.setPointSize(font.pointSize() + 25)
        title.setStyleSheet('color: rgb(118,109,100);')
        title.setFont(font)
        
        font.setPointSize(font.pointSize() - 20)
        self.scoreText.setFont(font)
        self.bestScore.setFont(font)

        # item button
        self.itemGroup = Item().itemGroup
      
        restart = self.itemGroup['restartBtn']
        restartBtn = Button(restart['img'], restart['size'])
        menu = self.itemGroup['menuBtn']
        menuBtn = Button(menu['img'], menu['size'])

        # layout
        hTitlebox = QHBoxLayout()
        hTitlebox.addWidget(title)
        hTitlebox.addStretch(1)
        hTitlebox.addWidget(self.scoreText)
        hTitlebox.addWidget(self.bestScore)
        
        hButtonbox = QHBoxLayout()
        hButtonbox.addWidget(menuBtn)
        hButtonbox.addStretch(1)
        hButtonbox.addWidget(restartBtn)
        
        # map background
        self.background = self.itemGroup['background']
        self.backgroundRect = QRect(20, 150, self.background['size'], self.background['size'])
        
        # mapLayout
        mapLayout = QGridLayout()

        self.block = self.itemGroup['block']
        self.button = []
        for r in range(self.N):
            btnR = []
            for c in range(self.N):
                button = Button(self.block['img'][0], self.block['size'])
                button.setEnabled(False)
                mapLayout.addWidget(button, r, c)
                btnR.append(button)
            self.button.append(btnR)

        mapLayout.setContentsMargins(10,20,10,20)
        mapLayout.setSpacing(10)

        # mainLayout
        mainLayout = QVBoxLayout()
        
        mainLayout.addLayout(hTitlebox)
        mainLayout.addLayout(hButtonbox)
        mainLayout.addLayout(mapLayout)
        
        self.setLayout(mainLayout)

        # create map
        self.CMap = CMap(self)
        self.CMap.displayGameinit()

        menuBtn.clicked.connect(self.showMenuwindow)
        restartBtn.clicked.connect(self.CMap.displayGameinit)

        self.keyPress()

    def writeScoreDB(self):
        
        if self.CMap.score not in self.sizeScoredb:
            
            self.sizeScoredb.append(self.CMap.score)
            self.sizeScoredb.sort(reverse=True)
            for idx in range(len(self.sizeScoredb)-1,-1,-1):
                if idx > 4: del self.sizeScoredb[idx]
           
            fH = open(self.dbfilename, 'wb')
            pickle.dump(self.scoredb, fH)
            fH.close()

    def showMenuwindow(self):
        self.writeScoreDB()
        self.close() # go back to main window

    def keyPress(self):
        QShortcut(QKeySequence(Qt.Key_Left), self, activated=(lambda : self.CMap.changeMap('L')))
        QShortcut(QKeySequence(Qt.Key_Up), self, activated=(lambda : self.CMap.changeMap('U')))
        QShortcut(QKeySequence(Qt.Key_Right), self, activated=(lambda : self.CMap.changeMap('R')))
        QShortcut(QKeySequence(Qt.Key_Down), self, activated=(lambda : self.CMap.changeMap('D')))
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawPixmap(self.backgroundRect, self.background['img'])
        qp.end()
    
    # block Button 업데이트 하기
    def blockUpdate(self, map):   
        for r in range(self.N):
            for c in range(self.N):
                for i in range(12):
                    if map[r][c] == 0: 
                        self.button[r][c].setImg(self.block['img'][0])
                    elif map[r][c] == 2**i:
                        self.button[r][c].setImg(self.block['img'][i])