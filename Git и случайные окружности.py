from PyQt6 import QtWidgets, QtGui, QtCore
from random import randint
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Random Circles')
        self.button = QtWidgets.QPushButton('Draw Circle', self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.draw_circle)
        self.show()

    def draw_circle(self):
        x = randint(50, 700)
        y = randint(50, 550)
        diameter = randint(20, 100)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        for x, y, diameter, color in self.circles:
            painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 2, QtGui.QPen.Style.SolidLine))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), QtGui.QBrush.Style.SolidPattern))
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
