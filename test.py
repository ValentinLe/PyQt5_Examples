
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        button = QPushButton("test")
        button.clicked.connect(self.openDialog)
        self.setCentralWidget(button)

    def openDialog(self):
        print("ok")
        w = TestWidget(self)
        w.show()


class TestWidget(QWidget):
    def __init__(self, parent=None):
        super(TestWidget, self).__init__(parent)

        label = QLabel("oulala")
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(label, 0, 0)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
