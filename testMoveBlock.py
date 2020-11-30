import unittest
from moveBlock import MoveBlock
class TestMoveBlock(unittest.TestCase):

    def setUp(self):
        self.MoveBlock = MoveBlock()
        self.testMap = [[0, 0, 0, 4], [0, 2, 0, 2], [2, 2, 2, 2], [0, 0, 0, 2]]     

    def tearDown(self):
        pass
    
    def testNextMove(self):
        
        # 키에 따른 nextMap 테스트
        # left
        nextMap, nextScore = self.MoveBlock.nextMove('L', self.testMap)
        self.assertEqual(nextMap, [[4, 0, 0, 0], [4, 0, 0, 0], [4, 4, 0, 0], [2, 0, 0, 0]])
        self.assertEqual(nextScore, 12)
        # Right
        nextMap, nextScore = self.MoveBlock.nextMove('R', self.testMap)
        self.assertEqual(nextMap, [[0, 0, 0, 4], [0, 0, 0, 4], [0, 0, 4, 4], [0, 0, 0, 2]])
        self.assertEqual(nextScore, 12)
        # Up
        nextMap, nextScore = self.MoveBlock.nextMove('U', self.testMap)
        self.assertEqual(nextMap, [[2, 4, 2, 4], [0, 0, 0, 4], [0, 0, 0, 2], [0, 0, 0, 0]])
        self.assertEqual(nextScore, 8)
        # Down
        nextMap, nextScore = self.MoveBlock.nextMove('D', self.testMap)
        self.assertEqual(nextMap, [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 2], [2, 4, 2, 4]])
        self.assertEqual(nextScore, 8)
        
        # 움직일 수 없을 경우 변화 없음
        self.testMap = [[2, 8, 2, 0], [4, 2, 0, 0], [2, 0, 0, 0], [2, 4, 0, 0]]
        nextMap, nextScore = self.MoveBlock.nextMove('L', self.testMap)
        self.assertEqual(nextMap, [[2, 8, 2, 0], [4, 2, 0, 0], [2, 0, 0, 0], [2, 4, 0, 0]])

if __name__ == '__main__':
    unittest.main()