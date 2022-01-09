import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtChart import QLineSeries, QChart, QValueAxis, QDateTimeAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QDateTime

def appendData(self, currPrice):
    if (len(self.priceData)) == self.viewLimit:
        self.priceData.remove(0)
    dt = QDateTime.currentDateTime()
    self.priceData.append(dt.toMSecsSinceEpoch(), currPrice)
    self.__updataAxis()
class ChartWidget(QWidget):
    def __init__(self, parent = None, ticker = "BTC"):
        super().__init__(parent)
        uic.loadUi("chart.ui", self)
        self.ticker = ticker
        self.viewLimit = 128

        self.priceData = QLineSeries()

        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)
        self.priceView.legend().hide

        axisX = QDateTimeAxis()
        axisX.setFormat("hh:mm:ss")
        axisX.setTickCount(4)
        dt = QDateTime.currentDateTime()
        axisX.setRange(dt, dt.addSecs(self.viewLimit))

        axisY = QValueAxis()
        axisY.setVisible(False)
        self.priceChart.addAxis(axisX, Qt.AlignBottom)
        self.priceChart.addAxis(axisY, Qt.AlignRight)
        self.priceData.attachAxis(axisX)
        self.priceData.attchAxis(axisY)
        self.priceChart.layout().setContentsMargins(0,0,0,0)

        self.priceView.setChart(self.priceChart)
        self.priceView.setRenderHints(QPainter.Antialiasing)

        def __updataAxis(self):
            pvs = self.priceData.pointVector()
            dtStart = QDateTime.fromMSecsSinceEpoch(int(pvs[0].x()))
            if len(self.priceData) == self.viewLimit:
                dtLast = QDateTime.fromMSecsSinceEpoch(int(pvs[-1].x()))
            else:
                dtLast = dtStart.addSecs(self.viewLimit)

            ax = self.priceChart.axisX()
            ax.setRange(dtStart, dtLast)

            ay = self.priceChart.axisY()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cw = ChartWidget("BTC")
    cw.show()
    exit(app.exec_())

