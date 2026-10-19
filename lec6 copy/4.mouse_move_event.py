import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Mouse Move Example")
        self.label = QLabel("<p>Move the mouse inside the window.</p>")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        # 기본값은 버튼을 누른 상태에서만 mouseMoveEvent 발생
        # setMouseTracking(True) 이면 버튼을 누르지 않아도 발생
        self.setMouseTracking(True)
        # label 이 마우스 이벤트를 가로채지 않도록 (창으로 전달됨)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.show()

    def mouseMoveEvent(self, event):
        x, y = event.pos().x(), event.pos().y()
        self.label.setText(f"<p>Mouse position: ({x}, {y})</p>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
