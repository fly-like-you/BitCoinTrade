import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

class MySignal(QObject):    #MySignal 클래스 정의
    signal1 = pyqtSignal()  #pyqt의 클래스의 객체 생성 인스턴스 변수가 아니라 클래스 변수로 만듦
    signal2 = pyqtSignal(int, int)
    def run(self):          # emit을 호출하는 메소드
        self.signal1.emit() #emit 메소드를 호출하여 시그널 발생
        self.signal2.emit(1,2)
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        mysignal = MySignal() #mysignal 클래스 객체 생성
        mysignal.signal1.connect(self.signal1_emitted)#사용자 정의 시그널과 이를 처리하는 메소드 연결
        mysignal.signal2.connect(self.signal2_emitted)
        mysignal.run()
    @pyqtSlot()
    def signal1_emitted(self):      #시그널이 방출될때 호출되는 메소드
        print("signal emitted")
    @pyqtSlot(int, int)
    def signal2_emitted(self,arg1, arg2):
        print("signal2 emitted", arg1, arg2)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()