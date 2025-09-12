from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
# from second_win import TestWin

class FinalWin(QWidget):
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
        self.index = QLabel('Rufier index')
        self.result = QLabel('Cardio performance: there is no data for this age')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.result, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    
    def next_win(self):
        pass
        
    
    def connects(self):
        pass
