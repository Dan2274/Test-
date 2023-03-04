from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from txt import *
from second_win import *

class FinalWin(QWidget):
    def __init__(self, exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        self.exp = exp

        # создаём и настраиваем графические элелементы:
        self.initUI(self.exp)

        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def result(self):
        if self.exp.a == 13:
            a2 = 1
        else:
            a2 = 0
        if self.exp.b == 23:
            b2 = 1
        else:
            b2 = 0
        if self.exp.c == 32:
            c2 = 1
        else:
            c2 = 0
        if self.exp.d == 42:
            d2 = 1
        else:
            d2 = 0
        if self.exp.e == 51:
            e2 = 1
        else:
            e2 = 0
        if self.exp.g == 62:
            g2 = 1
        else:
            g2 = 0
        if self.exp.h == 71:
            h2 = 1
        else:
            h2 = 0
        if self.exp.y == 83:
            y2 = 1
        else:
            y2 = 0
        
        total = a2 + b2 + c2 + d2 + e2 + g2 + h2 + y2
        if total == 8:
            return final_txt1
        elif total >= 6 and total < 8:
            return final_txt2
        elif total >= 4 and total < 6:
            return final_txt3
        elif total >= 1 and total < 4:
            return final_txt4
        else:
            return fail

    def initUI(self, exp):
        self.workh_text = QLabel(txt_workheart)
        #self.ball = QLabel(self.total)
        #self.index_text = QLabel(txt_index)
        self.result = QLabel(self.result())
        self.layout_line = QVBoxLayout()

        #self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        #self.layout_line.addWidget(self.ball, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)  
        self.layout_line.addWidget(self.result, alignment = Qt.AlignCenter)       
        self.setLayout(self.layout_line)

#app = QApplication([])
#mw = FinalWin()
#app.exec_()
