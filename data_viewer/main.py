# using PyQt5, PyQtWebEngine

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineCore import *

app = QApplication([])

window = QWidget()

gmap = QWebEngineView()
gmap.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
gmap.load(QUrl.fromLocalFile(QDir.current().absoluteFilePath('data_viewer/map.html')))

model = QWebEngineView()
model.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
model.load(QUrl.fromLocalFile(QDir.current().absoluteFilePath('data_viewer/map.html')))

generalLayout = QHBoxLayout()
rightLayout = QVBoxLayout()
leftLayout = QVBoxLayout()

rightLayout.addWidget(gmap)
rightLayout.addWidget(QLabel('General stats here'))

leftLayout.addWidget(model)
leftLayout.addWidget(QLabel("more stats"))

generalLayout.addLayout(rightLayout)
generalLayout.addLayout(leftLayout)

window.setLayout(generalLayout)
window.show()

app.exec_()