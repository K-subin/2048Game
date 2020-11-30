import unittest
from gameMap import CMap

class TestGameMap(unittest.TestCase):

    def setUp(self):
        self.N = 4
        self.g1 = CMap(self)        

    def tearDown(self):
        pass
    
    def testGameInit(self):
        # 초기화 테스트
        self.g1.gameInit()
        
        # 2블록이 2개, 0블록이 self.N*self.N-2개 있어야 한다.
        cntTwo,cntZero=0,0
        for row in self.g1.map:
            cntTwo += row.count(2)
            cntZero += row.count(0)
        self.assertEqual(cntTwo, 2)
        self.assertEqual(cntZero, self.N*self.N - 2)

    def testGenerateBlock(self):
        currentMap = [[16, 4, 0, 0], [32, 64, 16, 4], [4, 0, 32, 8], [2, 0, 4, 2]]
        self.g1.map = [[16, 4, 0, 0], [32, 64, 16, 4], [4, 0, 32, 8], [2, 0, 4, 2]]
        self.g1.generateBlock()
        nextMap = self.g1.map

        # 현재 맵의 0 부분이 2 또는 4로 1개 바뀌어야 한다.
        notEqualMap = [ (c, n) for cList, nList in zip(currentMap, nextMap) for c, n in zip(cList, nList) if c != n] 
        self.assertEqual(len(notEqualMap), 1)
        self.assertEqual(notEqualMap[0][0], 0)
        self.assertIn(notEqualMap[0][1], [2, 4])

    def testGameover(self):
        # 0이 있을 경우
        self.g1.map = [[16, 4, 2, 8], [32, 64, 16, 4], [4, 16, 32, 8], [2, 0, 4, 2]]
        self.assertFalse(self.g1.gameover())
        
        # 0이 없고 움직일 수 있는 경우
        self.g1.map = [[16, 4, 2, 8], [32, 64, 16, 4], [4, 16, 32, 8], [2, 16, 4, 2]]
        self.assertFalse(self.g1.gameover())

        # 0이 없고 움직이지 못할 경우
        self.g1.map = [[2, 16, 4, 8], [32, 4, 16, 4], [4, 64, 32, 8], [2, 32, 4, 2]]
        self.assertTrue(self.g1.gameover())

    def testSuccess(self):
        # 2048이 없을 경우
        self.g1.map = [[16, 4, 0, 0], [32, 64, 16, 4], [4, 0, 32, 8], [2, 0, 4, 2]]
        self.assertFalse(self.g1.success())
        
        # 2048이 있을 경우
        self.g1.map = [[16, 4, 0, 0], [32, 2048, 16, 4], [32, 4, 32, 0], [2, 0, 4, 2]]
        self.assertTrue(self.g1.success())


if __name__ == '__main__':
    unittest.main()