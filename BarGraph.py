import sys, random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QHBoxLayout)
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries 
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.parent_layout = QHBoxLayout()

        self.resize(800, 600)

        set0 = QBarSet("Throttle Percentage")
        # set1 = QBarSet("X1")
        # set2 = QBarSet("X2")
        # set3 = QBarSet("X3")

        set0.append([ random.randint(0, 100) for i in range(4) ])
        # set1.append([ random.randint(0, 10) for i in range(4) ])
        # set2.append([ random.randint(0, 10) for i in range(4) ])
        # set3.append([ random.randint(0, 10) for i in range(4) ])

        series = QBarSeries()
        series.append(set0)
        # series.append(set1)
        # series.append(set2)
        # series.append(set3)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Bar Chart')
        
        motors = ('Motor 1', 'Motor 2', 'Motor 3', 'Motor 4')

        xAxis = QBarCategoryAxis()
        xAxis.append(motors)

        yAxis = QValueAxis()
        yAxis.setRange(0, 100)

        chart.addAxis(xAxis, Qt.AlignBottom)
        chart.addAxis(yAxis, Qt.AlignLeft)

        chart.legend().setAlignment(Qt.AlignBottom)
        chart_view = QChartView(chart)

        self.parent_layout.addWidget(chart_view)

        self.setLayout(self.parent_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

