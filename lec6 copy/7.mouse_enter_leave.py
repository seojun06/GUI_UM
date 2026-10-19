import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Enter / Leave Example")
        self.label = QLabel("<p>Move the mouse in and out of the window.</p>")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self.show()

    def enterEvent(self, event):
        # 마우스가 창 안으로 들어왔을 때
        print("Mouse entered")
        self.label.setText("<p>Hello! 👋</p>")
        self.setStyleSheet("background-color: lightgreen;")

    def leaveEvent(self, event):
        # 마우스가 창 밖으로 나갔을 때
        print("Mouse left")
        self.label.setText("<p>Bye! Come back~</p>")
        self.setStyleSheet("background-color: lightpink;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
