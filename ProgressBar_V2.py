import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QApplication
from PyQt5.QtCore import *

class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Progress Bar")

        self.pbar = QProgressBar(self)
        self.pbar.setValue(10)
        self.pbar.setOrientation(Qt.Vertical)
        self.resize(300, 100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pb = ProgressBar()
    pb.show()
    sys.exit(app.exec_())