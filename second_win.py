from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget,
        QLineEdit, QButtonGroup)

from txt import *
from third_win import *

class Experiment():
    def __init__(self, a, b, c, d,e,g,h,y):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.g = g
        self.h = h
        self.y = y

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
        self.exp = Experiment(self.a, self.b, self.c, self.d,self.e, self.g, self.h, self.y)
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
        self.question1 = QLabel(question1)
        self.btn_next = QPushButton(txt_sendresults, self)
        self.rad_1_1 = QRadioButton(txt_1_1)
        self.rad_1_1.setChecked(True)
        self.rad_1_2 = QRadioButton(txt_1_2)
        self.rad_1_3 = QRadioButton(txt_1_3)
        self.rad_gr_1 = QButtonGroup()
        self.rad_gr_1.addButton(self.rad_1_1, id = 1)
        self.rad_gr_1.addButton(self.rad_1_2, id = 2)
        self.rad_gr_1.addButton(self.rad_1_3, id = 3)
        self.question2 = QLabel(question2)
        self.rad_2_1 = QRadioButton(txt_2_1)
        self.rad_2_1.setChecked(True)
        self.rad_2_2 = QRadioButton(txt_2_2)
        self.rad_2_3 = QRadioButton(txt_2_3)
        self.rad_gr_2 = QButtonGroup()
        self.rad_gr_2.addButton(self.rad_2_1, id = 1)
        self.rad_gr_2.addButton(self.rad_2_2, id = 2)
        self.rad_gr_2.addButton(self.rad_2_3, id = 3)
        self.question3 = QLabel(question3)
        self.rad_3_1 = QRadioButton(txt_3_1)
        self.rad_3_1.setChecked(True)
        self.rad_3_2 = QRadioButton(txt_3_2)
        self.rad_3_3 = QRadioButton(txt_3_3)
        self.rad_gr_3 = QButtonGroup()
        self.rad_gr_3.addButton(self.rad_3_1, id = 1)
        self.rad_gr_3.addButton(self.rad_3_2, id = 2)
        self.rad_gr_3.addButton(self.rad_3_3, id = 3)
        self.question4 = QLabel(question4)
        self.rad_4_1 = QRadioButton(txt_4_1)
        self.rad_4_1.setChecked(True)
        self.rad_4_2 = QRadioButton(txt_4_2)
        self.rad_4_3 = QRadioButton(txt_4_3)
        self.rad_gr_4 = QButtonGroup()
        self.rad_gr_4.addButton(self.rad_4_1, id = 1)
        self.rad_gr_4.addButton(self.rad_4_2, id = 2)
        self.rad_gr_4.addButton(self.rad_4_3, id = 3)
        self.question5 = QLabel(question5)
        self.rad_5_1 = QRadioButton(txt_5_1)
        self.rad_5_1.setChecked(True)
        self.rad_5_2 = QRadioButton(txt_5_2)
        self.rad_5_3 = QRadioButton(txt_5_3)
        self.rad_gr_5 = QButtonGroup()
        self.rad_gr_5.addButton(self.rad_5_1, id = 1)
        self.rad_gr_5.addButton(self.rad_5_2, id = 2)
        self.rad_gr_5.addButton(self.rad_5_3, id = 3)
        self.question6 = QLabel(question6)
        self.rad_6_1 = QRadioButton(txt_6_1)
        self.rad_6_1.setChecked(True)
        self.rad_6_2 = QRadioButton(txt_6_2)
        self.rad_6_3 = QRadioButton(txt_6_3)
        self.rad_gr_6 = QButtonGroup()
        self.rad_gr_6.addButton(self.rad_6_1, id = 1)
        self.rad_gr_6.addButton(self.rad_6_2, id = 2)
        self.rad_gr_6.addButton(self.rad_6_3, id = 3)
        self.question7 = QLabel(question7)
        self.rad_7_1 = QRadioButton(txt_7_1)
        self.rad_7_1.setChecked(True)
        self.rad_7_2 = QRadioButton(txt_7_2)
        self.rad_7_3 = QRadioButton(txt_7_3)
        self.rad_gr_7 = QButtonGroup()
        self.rad_gr_7.addButton(self.rad_7_1, id = 1)
        self.rad_gr_7.addButton(self.rad_7_2, id = 2)
        self.rad_gr_7.addButton(self.rad_7_3, id = 3)
        self.question8 = QLabel(question8)
        self.rad_8_1 = QRadioButton(txt_8_1)
        self.rad_8_1.setChecked(True)
        self.rad_8_2 = QRadioButton(txt_8_2)
        self.rad_8_3 = QRadioButton(txt_8_3)
        self.rad_gr_8 = QButtonGroup()
        self.rad_gr_8.addButton(self.rad_8_1, id = 1)
        self.rad_gr_8.addButton(self.rad_8_2, id = 2)
        self.rad_gr_8.addButton(self.rad_8_3, id = 3)
        self.a = self.rad_gr_1.checkedId()
        self.b = self.rad_gr_2.checkedId()
        self.c = self.rad_gr_3.checkedId()
        self.d = self.rad_gr_4.checkedId()
        self.e = self.rad_gr_5.checkedId()
        self.g = self.rad_gr_6.checkedId()
        self.h = self.rad_gr_7.checkedId()
        self.y = self.rad_gr_8.checkedId()

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
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.l_line.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_1_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_1_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_1_3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.question2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_2_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_2_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_2_3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.question3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_3_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_3_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_3_3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.question4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_4_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_4_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_4_3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.question5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_5_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_5_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_5_3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.question6, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_6_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_6_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_6_3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.question7, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_7_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_7_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_7_3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.question8, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_8_1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_8_2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.rad_8_3, alignment = Qt.AlignLeft)
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
#        self.l_line.addWidget(self.btn_test4, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
#        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter) 
        self.h_line.addLayout(self.l_line)  
        self.h_line.addLayout(self.r_line)        
        self.setLayout(self.h_line)
 
