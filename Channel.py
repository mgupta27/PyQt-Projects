import sys
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QPixmap(400, 25)
        canvas.fill(QColor('white'))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.label.pixmap())
        
        pen_1 = QPen()
        pen_1.setColor( QColor("red") )

        painter.setPen(pen_1)
        painter.setBrush( QBrush(Qt.red, Qt.SolidPattern) )
        painter.drawRect(200, 0, 50, 25)

        pen_2 = QPen()
        pen_2.setColor( QColor("black") )
        pen_2.setWidth(4)
        
        painter.setPen(pen_2)
        painter.drawLine(200, 0, 200, 100)
        
        # painter = QPainter(self.label.pixmap())
        # pen = QPen()
        # pen.setColor(QColor('red'))
        # painter.setPen(pen)
        # painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        # # The third parameter should be used to control length
        # painter.drawRect(200, 0, 50, 25)
        # painter.end()
        


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()