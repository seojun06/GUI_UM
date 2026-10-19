import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.font_size = 12  # 글자 크기
        self.init_ui()
        self.control_pressed = False  # Control 키 상태를 추적하는 변수

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Wheel Event Example")
        self.label = QLabel("Scroll the wheel!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self.update_font()
        self.show()

    def wheelEvent(self, event):
        # angleDelta().y() > 0 : 위로 스크롤, < 0 : 아래로 스크롤
        if event.angleDelta().y() > 0 and self.control_pressed:
            self.font_size = min(self.font_size + 2, 60)
        elif event.angleDelta().y() < 0 and self.control_pressed:
            self.font_size = max(self.font_size - 2, 6)
        else:
            return  # Control 키가 눌리지 않은 경우 글자 크기 변경하지 않음
        print("Font size:", self.font_size)
        self.update_font()

    def update_font(self):
        font = self.label.font()
        font.setPointSize(self.font_size)
        self.label.setFont(font)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Control:
            self.control_pressed = True

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Control:
            self.control_pressed = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
