import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Event Handling Example")
        label = QLabel(
            """<p>Press the <b>ESC</b> key to quit this program.</p>""")
        self.setCentralWidget(label)
        self.show()

    def keyPressEvent(self, event):
        self.event_fn1()
        self.event_fn2()
        self.event_fn3()

    def event1(self):
        print("Event 1 triggered!")

    def event2(self):
        print("Event 2 triggered!")

    def event3(self):
        print("Event 3 triggered!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

