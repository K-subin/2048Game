import numpy as np
from copy import deepcopy

class MoveBlock:
    def __init__(self):
        super().__init__()
    
    def nextMove(self, sKey, currentMap):
        nextMap = deepcopy(currentMap)
        self.N, self.sKey = len(nextMap), sKey

        nextMap = self.arrT(nextMap)
        nextMap = self.moveZero(nextMap)

        if sKey == 'L' or sKey == 'U':
            rg, num = range(self.N), -1
        else:
            rg, num = range(self.N-1,-1,-1), 1
        
        nextScore=0
        for r in rg:
            for c in rg:
                nextC = c + num
                if 0 <= nextC < self.N and nextMap[r][nextC] == nextMap[r][c]:
                    nextMap[r][nextC] *= 2
                    nextMap[r][c] = 0
                    nextScore += nextMap[r][nextC]
                    c += num
        
        nextMap = self.moveZero(nextMap)
        nextMap = self.arrT(nextMap)

        return nextMap, nextScore
    
    # 배열 transpose 하기
    def arrT(self, arr):
        if self.sKey == 'L' or self.sKey == 'R':
            return arr

        transArr = np.array(arr).T
        arr = transArr.tolist()
        return arr
        
    # 0을 맨 앞 또는 맨 뒤로 움직이기
    def moveZero(self, arr):
        res = []
        for row in arr:
            while(0 in row):
                row.remove(0)
            if self.sKey == 'L' or self.sKey == 'U':
                res.append(row + [0]*(self.N-len(row)))
            else:
                res.append([0]*(self.N-len(row)) + row)
        
        return res
