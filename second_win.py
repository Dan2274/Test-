from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from txt import *
from third_win import *

#class Experiment():
#    def __init__(self, age, test1, test2, test3):
#        self.age = age
#        self.t1 = test1
#        self.t2 = test2
#        self.t3 = test3
#
class second_win(QWidget):
    def __init__(self):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        # создаём и настраиваем графические эелементы:
        self.initUI()

        #устанавливает связи между элементами
        self.connects()

        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()


    
    def next_click(self):
        self.hide()
#        self.exp = Experiment(int(self.line_age.text()), self.line_test1.text(), self.line_test2.text(), self.line_test3.text())
        self.fw = FinalWin()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        ''' создает графические элементы '''
        #self.questionnary = AllQuestions()
        self.btn_next = QPushButton(txt_sendresults, self)
#        self.btn_test1 = QPushButton(txt_starttest1, self)
#        self.btn_test2 = QPushButton(txt_starttest2, self)
#        self.btn_test3 = QPushButton(txt_starttest3, self)
#
#
#        self.text_name = QLabel(txt_name)
#        self.text_age = QLabel(txt_age)
#        self.text_test1 = QLabel(txt_test1)
#        self.text_test2 = QLabel(txt_test2)
#        self.text_test3 = QLabel(txt_test3)
#
#        self.line_name = QLineEdit(txt_hintname)
#
#        self.line_age = QLineEdit(txt_hintage)
#
#        self.line_test1 = QLineEdit(txt_hinttest1)
#
#        self.line_test2 = QLineEdit(txt_hinttest2)
#
#        self.line_test3 = QLineEdit(txt_hinttest3)
#
#        self.l_line = QVBoxLayout()
#        self.r_line = QVBoxLayout()
#        self.h_line = QHBoxLayout()
#        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
#        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft) 
#        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft) 
#        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft) 
#        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft) 
#        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter) 
#        self.h_line.addLayout(self.l_line)  
#        self.h_line.addLayout(self.r_line)        
#        self.setLayout(self.h_line)
