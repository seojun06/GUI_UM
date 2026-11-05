import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import pyqtSignal

# 위젯: 색 버튼 3개, 색을 고르면 signal 을 보냄
class ColorPicker(QWidget):
    color_chosen = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        for color in ["red", "green", "blue"]:
            button = QPushButton(color)
            button.clicked.connect(self.on_click)
            layout.addWidget(button)
        self.setLayout(layout)

    def on_click(self):
        # 눌린 버튼의 글자(색 이름)를 signal 로 보냄
        self.color_chosen.emit(self.sender().text())

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("9. Custom Widget Signal")
        self.label = QLabel("Pick a color")
        picker = ColorPicker()
        # QPushButton.clicked 처럼, 내 위젯의 signal 에 연결
        picker.color_chosen.connect(self.set_color)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(picker)
        self.setLayout(layout)
        self.show()

    # slot
    def set_color(self, color):
        self.label.setText(color)
        self.label.setStyleSheet(f"color: {color}; font-size: 20px;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
