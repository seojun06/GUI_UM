import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Mouse Press Example")
        self.label = QLabel("<p>Click anywhere with any mouse button.</p>")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self.show()

    def mousePressEvent(self, event):
        # 어떤 버튼이 눌렸는지 확인
        if event.button() == Qt.MouseButton.LeftButton:
            button = "Left"
        elif event.button() == Qt.MouseButton.RightButton:
            button = "Right"
        elif event.button() == Qt.MouseButton.MiddleButton:
            button = "Middle"
        else:
            button = "Other"
        x, y = event.pos().x(), event.pos().y()
        print(f"{button} button pressed at ({x}, {y})")
        self.label.setText(f"<p><b>{button}</b> button pressed at ({x}, {y})</p>")

    def mouseReleaseEvent(self, event):
        print("Mouse button released")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
