from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from second_win import TestWin

class MainWin(QWidget):
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
        self.hello_text = QLabel('aplikasi kesehatan')
        self.instruction = QLabel('aplikasi ada 3 tahapan, detak jantung....')
        self.button = QPushButton('Start')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    
    def next_win(self):
        self.tw = TestWin()
        self.hide()
        
    
    def connects(self):
        self.button.clicked.connect(self.next_win)

app = QApplication([])
win = MainWin()
app.exec_()