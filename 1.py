import sys

from ui_file import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF
import random

class MyWidget(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        r = random.randint(20, 100)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(QPointF(250, 250), r, r)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())