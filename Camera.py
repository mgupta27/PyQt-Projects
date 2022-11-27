import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2 

class HomePage(QWidget):
    
    def __init__(self):
        super(HomePage, self).__init__()
        # Create the Home page UI here
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Home Page"))
        self.FeedLabel = QLabel()
        layout.addWidget(self.FeedLabel)
        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        layout.addWidget(self.CancelBTN) #basic page layout
        self.cvstream = cameraThread()
        self.cvstream.start()
        self.cvstream.ImageUpdate.connect(self.ImageUpdateSlot) 
        self.setLayout(layout)
        
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.cvstream.stop()



class cameraThread(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0) #defines video capture
        while self.ThreadActive: #while it can read
            ret, frame = Capture.read()
            if ret: #if it can read
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert to color pic but pyqt cannot read still
                FlippedImage = cv2.flip(Image, 1) #flip on vertical axis
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit() 

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = HomePage() 
    Root.show()
    sys.exit(App.exec())