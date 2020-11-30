from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QPainter, QPixmap

class Button(QToolButton):

    def __init__(self, img, size):
        super().__init__()
        self.img = img
        self.size = size
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    def setImg(self, img):
        self.img = img
        self.update()

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(self.size)
        size.setWidth(max(size.width(), size.height()))
        return size
    
    def paintEvent(self, event):
        QToolButton.paintEvent(self, event)
        qp = QPainter(self)
        qp.drawPixmap(self.rect(), self.img)

