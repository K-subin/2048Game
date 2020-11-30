import sys
from menuWindow import MainWindow
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec_())
