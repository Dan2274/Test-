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
