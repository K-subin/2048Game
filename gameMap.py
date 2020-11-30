
from PyQt5.QtWidgets import QMessageBox

from moveBlock import MoveBlock
import random

class CMap:

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.N = self.parent.N
        self.score = 0

        self.MoveBlock = MoveBlock()     

    def __del__(self):        
        pass
    
    # 게임 초기화 함수
    def gameInit(self):
        self.map = [[0 for j in range(self.N)] for i in range(self.N)] # 맵 초기화
        self.score = 0 # 점수 초기화

        # 2블록 랜덤한 위치에 두개 생성
        row = random.sample(range(self.N), 2)
        col = random.sample(range(self.N), 2)
        self.map[row[0]][col[0]] = 2
        self.map[row[1]][col[1]] = 2
  
    # 게임 초기화 draw
    def displayGameinit(self):
        self.parent.writeScoreDB()
        self.gameInit()
        self.parent.scoreText.setText('SCORE\n'+str(self.score))
        self.parent.blockUpdate(self.map)

    # 블록 생성 함수
    def generateBlock(self):
        # 맵이 0인 위치(row, col) 선택
        zeroIndex = [[row, col] for row in range(self.N) for col in range(self.N) if self.map[row][col] == 0]

        num = random.randrange(len(zeroIndex))
        row, col = zeroIndex[num][0], zeroIndex[num][1]
        
        # 90% 확률로 2카드 생성, 10% 확률로 4카드 생성
        if random.randrange(100)<90:
            self.map[row][col] = 2
        else:
            self.map[row][col] = 4
    
    # Map 바꾸기
    def changeMap(self, sKey):
        
        nextMap, nextScore = self.MoveBlock.nextMove(sKey, self.map)

        self.score += nextScore
        self.parent.scoreText.setText('SCORE\n'+str(self.score))
        
        if self.score > self.parent.sizeScoredb[0]:
            self.parent.bestScore.setText('BEST\n'+str(self.score))
        
        # key 누르기 전과 후가 다르면 새 카드 생성
        if not nextMap == self.map:
            self.map = nextMap
            self.generateBlock()
            self.parent.blockUpdate(self.map)

        if self.success():
            self.message(f'승리!\nscore : {self.score}점\n다시 시작하시겠습니까?')
        elif self.gameover():
            self.message(f'승리!\nscore : {self.score}점\n다시 시작하시겠습니까?')
    
    def message(self, text):
        result = QMessageBox.information(self.parent, 'finish', text, QMessageBox.Yes | QMessageBox.No)
        
        if result == QMessageBox.Yes:
            self.displayGameinit()
        else:
            self.parent.writeScoreDB()
            self.parent.close()

    def success(self):
        for r in range(self.N):
            for c in range(self.N):
                if self.map[r][c] == 2048:
                    return True
        return False
        
    def gameover(self):
        
        for r in range(self.N):
            for c in range(self.N):
                if self.map[r][c] == 0:
                    return False

        # 더 움직일 수 없으면 True
        for sKey in ['L','R','U','D']:
            nextMap = self.MoveBlock.nextMove(sKey, self.map)[0]
            if not nextMap == self.map:
                return False
        return True

  