from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
from random import randint
from PyQt6 import uic
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('UI.ui', self)
        self.ui.button.clicked.connect(self.draw_circles)
        self.circles = []

    def draw_circles(self):
        self.circles.append((randint(50, 200), randint(50, 200), randint(20, 100)))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.yellow, Qt.BrushStyle.SolidPattern))
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
