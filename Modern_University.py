import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from first_page import FirstPage

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    firstpage = FirstPage()
    sys.exit(app.exec_())
