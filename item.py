from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

class Item:
    def __init__(self):
        super().__init__()
        self.itemGroup = {
            'background':{'size':500, 'img':QPixmap("Image/background.png")},
            'block':{'size':150, 'img':[QPixmap("Image/0.png")]+[QPixmap("Image/"+str(2**i)+".png") for i in range(1,12)]},
            'menuBtn':{'size':50, 'img':QPixmap("Image/home.png")},
            'restartBtn':{'size':50, 'img':QPixmap("Image/restart.png")},
            'arrow':{'size':15, 'img':[QPixmap("Image/Left.png"), QPixmap("Image/Right.png")]},
            'mapPhoto':{'size':300, 'img':[QPixmap("Image/"+str(i)+"x"+str(i)+"map.png") for i in range(3,7)]},
            'startBtn':{'size':75, 'img':QPixmap("Image/startBtn.png")},
            'rankBtn':{'size':75, 'img':QPixmap("Image/rankBtn.png")}
        }
