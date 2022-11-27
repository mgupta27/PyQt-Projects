import sys
from PyQt5.QtWidgets import * 
                    
   
#Main Window
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTableWidget'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
   
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
   
        self.createTable()
   
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
   
        #Show window
        self.show()
   
    #Create table
    def createTable(self):
        HEADER = ['Name', 'Latitude', 'Longitude', 'Add', 'Remove']

        self.tableWidget = QTableWidget()

        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setHorizontalHeaderLabels(HEADER)

        #self.tableWidget.setItem(0, 0, QTableWidget("Alpha"))
        # self.tableWidget.setItem(0, 1, QTableWidget(f'{-71.6375025}'))
        # self.tableWidget.setItem(0, 2, QTableWidget(f'{48.5166707}'))
        #self.tableWidget.setItem(0, 3, QP)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())