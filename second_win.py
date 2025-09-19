from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle('test ruffier')
        self.resize(1000, 600)
        
    def initUI(self):
        self.lbl_name = QLabel('Enter your full name')
        self.lbl_age = QLabel('Full years')
        self.lbl_first = QLabel('tahap pertama')
        self.lbl_second = QLabel('tahap kedua')
        self.lbl_three = QLabel('tahap ketiga')
        self.stopwatch = QLabel('00:00:00')
        self.stopwatch.setFont(QFont('Times', 36, QFont.Bold))

        self.btn_first = QPushButton('start the first test')
        self.btn_second = QPushButton('start the doing squats')
        self.btn_three = QPushButton('start the final test')
        self.btn_result = QPushButton('send the result')
        
        self.name = QLineEdit('Full Name')
        self.age = QLineEdit('0')
        self.line_first = QLineEdit('0')
        self.line_second = QLineEdit('0')
        self.line_three = QLineEdit('0')
        
        self.r_line = QVBoxLayout()
        self.r_line.addWidget(self.stopwatch)
        
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.lbl_name)
        self.l_line.addWidget(self.name)
        self.l_line.addWidget(self.lbl_age)
        self.l_line.addWidget(self.age)
        self.l_line.addWidget(self.lbl_first)
        self.l_line.addWidget(self.btn_first)
        self.l_line.addWidget(self.line_first)
        self.l_line.addWidget(self.lbl_second)
        self.l_line.addWidget(self.btn_second)
        self.l_line.addWidget(self.line_second)
        self.l_line.addWidget(self.lbl_three)
        self.l_line.addWidget(self.btn_three)
        self.l_line.addWidget(self.line_three)
        
        self.h_line = QHBoxLayout()
        self.h_line.addLayout(self.l_line)
        self.h_line.addWidget(self.btn_result)
        self.h_line.addLayout(self.r_line)
        
        self.setLayout(self.h_line)
    
    def next_win(self):
        self.fw = FinalWin()
        self.hide()

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.stopwatch.setText(time.toString("hh:mm:ss"))
        self.stopwatch.setFont(QFont("Times", 36, QFont.Bold))
        self.stopwatch.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.stopwatch.setText(time.toString("hh:mm:ss")[6:8])
        self.stopwatch.setStyleSheet("color: rgb(0,0,0)")
        self.stopwatch.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.stopwatch.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.stopwatch.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.stopwatch.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.stopwatch.setStyleSheet("color: rgb(0,0,0)")
        self.stopwatch.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def connects(self):
        self.btn_result.clicked.connect(self.next_win)
        self.btn_first.clicked.connect(self.timer_test)
        self.btn_second.clicked.connect(self.timer_sits)
        self.btn_three.clicked.connect(self.timer_final)
        
        
