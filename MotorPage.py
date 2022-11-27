import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MotorPage(QWidget):
    def __init__(self):
        super().__init__()

        M1_THROTTLE_PERCENTAGE = 25
        M2_THROTTLE_PERCENTAGE = 50
        M3_THROTTLE_PERCENTAGE = 75
        M4_THROTTLE_PERCENTAGE = 100

        M1_MOTOR_OUTPUT = 10
        M2_MOTOR_OUTPUT = 20
        M3_MOTOR_OUTPUT = 30
        M4_MOTOR_OUTPUT = 40

        M1_CURRENT_DRAW = 10
        M2_CURRENT_DRAW = 20
        M3_CURRENT_DRAW = 30
        M4_CURRENT_DRAW = 40

        self.setWindowTitle("Motor Page") 
        
        # Throttle Percentage UI
        top_horizontal_layout = QHBoxLayout()
        throttle_layout = QVBoxLayout()
        percentage_layout = QHBoxLayout()

        m1_layout = QVBoxLayout()
        m2_layout = QVBoxLayout()
        m3_layout = QVBoxLayout()
        m4_layout = QVBoxLayout()

        throttle_label = QLabel("Throttle %")
        #throttle_label.alignment(Qt.AlignCenter)

        self.m1ProgressBar = QProgressBar(self)
        self.m1ProgressBar.setValue(M1_THROTTLE_PERCENTAGE)
        self.m1ProgressBar.setOrientation(Qt.Vertical)
        self.m1ThrottlePercentage = QLabel(f"{M1_THROTTLE_PERCENTAGE} %")
        self.m1Label = QLabel("Motor 1")

        self.m2ProgressBar = QProgressBar(self)
        self.m2ProgressBar.setValue(M2_THROTTLE_PERCENTAGE)
        self.m2ProgressBar.setOrientation(Qt.Vertical)
        self.m2ThrottlePercentage = QLabel(f"{M2_THROTTLE_PERCENTAGE} %")
        self.m2Label = QLabel("Motor 2")

        self.m3ProgressBar = QProgressBar(self)
        self.m3ProgressBar.setValue(M3_THROTTLE_PERCENTAGE)
        self.m3ProgressBar.setOrientation(Qt.Vertical)
        self.m3ThrottlePercentage = QLabel(f"{M3_THROTTLE_PERCENTAGE} %")
        self.m3Label = QLabel("Motor 3")

        self.m4ProgressBar = QProgressBar(self)
        self.m4ProgressBar.setValue(M4_THROTTLE_PERCENTAGE)
        self.m4ProgressBar.setOrientation(Qt.Vertical)
        self.m4ThrottlePercentage = QLabel(f"{M4_THROTTLE_PERCENTAGE} %")
        self.m4Label = QLabel("Motor 4")

        m1_layout.addWidget(self.m1Label)
        m1_layout.addWidget(self.m1ProgressBar)
        m1_layout.addWidget(self.m1ThrottlePercentage)

        m2_layout.addWidget(self.m2Label)
        m2_layout.addWidget(self.m2ProgressBar)
        m2_layout.addWidget(self.m2ThrottlePercentage)

        m3_layout.addWidget(self.m3Label)
        m3_layout.addWidget(self.m3ProgressBar)
        m3_layout.addWidget(self.m3ThrottlePercentage)

        m4_layout.addWidget(self.m4Label)
        m4_layout.addWidget(self.m4ProgressBar)
        m4_layout.addWidget(self.m4ThrottlePercentage)

        percentage_layout.addLayout(m1_layout)
        percentage_layout.addLayout(m2_layout)
        percentage_layout.addLayout(m3_layout)
        percentage_layout.addLayout(m4_layout)

        throttle_layout.addWidget(throttle_label)
        throttle_layout.addLayout(percentage_layout)

        # Setpoint and Current Draw Layout
        setpoint_layout = QVBoxLayout()

        # Motor 1 Display
        m1_setpoint_layout = QVBoxLayout()
        m1_set_output_layout = QHBoxLayout()

        self.m1_setpoint_label = QLabel(f"Motor 1 Output")
        self.m1_setpoint_line_edit = QLineEdit()
        self.m1_setpoint_button = QPushButton("Apply")

        m1_set_output_layout.addWidget(QLabel("Motor 1 Desired Output: "))
        m1_set_output_layout.addWidget(self.m1_setpoint_line_edit)
        m1_set_output_layout.addWidget(self.m1_setpoint_button)

        m1_setpoint_layout.addWidget(self.m1_setpoint_label)
        m1_setpoint_layout.addWidget(QLabel(f"Current Draw: {M1_CURRENT_DRAW}"))
        m1_setpoint_layout.addWidget(QLabel(f"Current Motor Output: {M1_MOTOR_OUTPUT}"))
        m1_setpoint_layout.addLayout(m1_set_output_layout)

        # Motor 2 Display
        m2_setpoint_layout = QVBoxLayout()
        m2_set_output_layout = QHBoxLayout()

        self.m2_setpoint_label = QLabel(f"Motor 2 Output")
        self.m2_setpoint_line_edit = QLineEdit()
        self.m2_setpoint_button = QPushButton("Apply")

        m2_set_output_layout.addWidget(QLabel("Motor 2 Desired Output: "))
        m2_set_output_layout.addWidget(self.m2_setpoint_line_edit)
        m2_set_output_layout.addWidget(self.m2_setpoint_button)

        m2_setpoint_layout.addWidget(self.m2_setpoint_label)
        m2_setpoint_layout.addWidget(QLabel(f"Current Draw: {M2_CURRENT_DRAW}"))
        m2_setpoint_layout.addWidget(QLabel(f"Current Motor Output: {M2_MOTOR_OUTPUT}"))
        m2_setpoint_layout.addLayout(m2_set_output_layout)

        # Motor 3 Display
        m3_setpoint_layout = QVBoxLayout()
        m3_set_output_layout = QHBoxLayout()

        self.m3_setpoint_label = QLabel(f"Motor 3 Output")
        self.m3_setpoint_line_edit = QLineEdit()
        self.m3_setpoint_button = QPushButton("Apply")

        m3_set_output_layout.addWidget(QLabel("Motor 3 Desired Output: "))
        m3_set_output_layout.addWidget(self.m3_setpoint_line_edit)
        m3_set_output_layout.addWidget(self.m3_setpoint_button)

        m3_setpoint_layout.addWidget(self.m3_setpoint_label)
        m3_setpoint_layout.addWidget(QLabel(f"Current Draw: {M3_CURRENT_DRAW}"))
        m3_setpoint_layout.addWidget(QLabel(f"Current Motor Output: {M3_MOTOR_OUTPUT}"))
        m3_setpoint_layout.addLayout(m3_set_output_layout)

        # Motor 4 Display
        m4_setpoint_layout = QVBoxLayout()
        m4_set_output_layout = QHBoxLayout()

        self.m4_setpoint_label = QLabel(f"Motor 4 Output")
        self.m4_setpoint_line_edit = QLineEdit()
        self.m4_setpoint_button = QPushButton("Apply")

        m4_set_output_layout.addWidget(QLabel("Motor 4 Desired Output: "))
        m4_set_output_layout.addWidget(self.m4_setpoint_line_edit)
        m4_set_output_layout.addWidget(self.m4_setpoint_button)

        m4_setpoint_layout.addWidget(self.m4_setpoint_label)
        m4_setpoint_layout.addWidget(QLabel(f"Current Draw: {M4_CURRENT_DRAW}"))
        m4_setpoint_layout.addWidget(QLabel(f"Current Motor Output: {M4_MOTOR_OUTPUT}"))
        m4_setpoint_layout.addLayout(m4_set_output_layout)

        setpoint_layout.addSpacing(30)
        setpoint_layout.addLayout(m1_setpoint_layout)
        setpoint_layout.addSpacing(10)
        setpoint_layout.addLayout(m2_setpoint_layout)
        setpoint_layout.addSpacing(10)
        setpoint_layout.addLayout(m3_setpoint_layout)
        setpoint_layout.addSpacing(10)
        setpoint_layout.addLayout(m4_setpoint_layout)

        top_horizontal_layout.addLayout(throttle_layout)
        top_horizontal_layout.addSpacing(50)
        top_horizontal_layout.addLayout(setpoint_layout)

        bot_horizontal_layout = QHBoxLayout()
        l_stick_deflection_layout = QHBoxLayout()
        l_pbar_layout = QVBoxLayout()

        # X, Y, Z Axis Layout
        lx_axis_layout = QHBoxLayout()
        ly_axis_layout = QHBoxLayout()
        lz_axis_layout = QHBoxLayout()

        self.lx_rot_pbar = QProgressBar(self)
        self.lx_rot_pbar.setValue(10)

        self.ly_rot_pbar = QProgressBar(self)
        self.ly_rot_pbar.setValue(20)

        self.lz_axis_pbar = QProgressBar(self)
        self.lz_axis_pbar.setValue(30)

        lx_axis_layout.addWidget(QLabel("X Rotation"))
        lx_axis_layout.addWidget(self.lx_rot_pbar)

        ly_axis_layout.addWidget(QLabel("Y Rotation"))
        ly_axis_layout.addWidget(self.ly_rot_pbar)

        lz_axis_layout.addWidget(QLabel("Z Axis      "))
        lz_axis_layout.addWidget(self.lz_axis_pbar)

        l_pbar_layout.addLayout(lx_axis_layout)
        l_pbar_layout.addLayout(ly_axis_layout)
        l_pbar_layout.addLayout(lz_axis_layout)

        painter = QPainter()
        # Thrust/Yaw X and Y Box

        bot_horizontal_layout.addLayout(l_pbar_layout)

        body_layout = QVBoxLayout()
        body_layout.addLayout(top_horizontal_layout)
        body_layout.addLayout(bot_horizontal_layout)

        self.setLayout(body_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pb = MotorPage()
    pb.show()
    sys.exit(app.exec_())