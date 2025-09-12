from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
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
        self.stopwatch = QLabel('09:00:09')
        
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
        
    
    def connects(self):
        self.btn_result.clicked.connect(self.next_win)
