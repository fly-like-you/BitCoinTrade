import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit
form_class = uic.loadUiType("myWindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)   # when buttons clicked,  start function inquiry

        '''
        QTimer를 사용하려면 윈도우가 생성될 때 QTimer 객체를 생성해야한다. 객체에는 interval설정이 필요하다. interval은 얼마나 자주 이벤트가 발생하는지 의미하며,
        현재코드는 1초를 기준으로 두었다.
        '''
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)


    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

'''
    할리스 10,300 원 나 악기
    큐브락 21,000 원 나 악기
    미스터 피자 51,600 나 악기 재호 문어 인당 12,900원
    보겜 음료 17,600 나 악기 재호 문어  인당 4,400 원
    보겜 15,900원 나 악기 재호 문어  음료 재호 4500 나 4500 문어 ?? 악기 ??
    문어 1
'''