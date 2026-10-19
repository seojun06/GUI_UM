import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.is_dark = False  # 현재 배경 상태

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Double Click Example")
        self.label = QLabel("<p><b>Double-click</b> to change the background.</p>")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self.show()

    def mouseDoubleClickEvent(self, event):
        self.is_dark = not self.is_dark
        if self.is_dark:
            self.setStyleSheet("background-color: red; color: white;")
        else:
            self.setStyleSheet("")
        print("Double-clicked! Dark mode:", self.is_dark)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
