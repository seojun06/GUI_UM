import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal

class startWindow(QWidget):
    click_me_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()
        # slot 은 내가 만든 메서드도 됩니다
        self.click_me_clicked.connect(self.add_one)

    def init_ui(self):
        self.setWindowTitle("2. My Own Slot v2")
        self.resize(350, 220)

        self.label = QLabel("Clicked: <span style='color: red;'>0</span>")
        self.label.setStyleSheet(
            "font-size: 24px; padding-left: 40px; background-color: white; color: black;")

        # 버튼이 아니라 그냥 label
        self.click_me = QLabel("Click me")
        self.click_me.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.click_me.setFixedHeight(50)
        self.click_me.setStyleSheet(
            "font-size: 24px; background-color: #a0a0a0; color: black; border-top: 2px solid black;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)   # 창 테두리까지 꽉 채움
        layout.setSpacing(0)
        layout.addWidget(self.label)
        layout.addWidget(self.click_me)
        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        # 클릭한 위치가 "Click me" label 안쪽일 때만 signal 을 보냄
        if self.click_me.geometry().contains(event.pos()):
            self.click_me_clicked.emit()

    # slot
    def add_one(self):
        self.count += 1
        self.label.setText(f"Clicked: <span style='color: red;'>{self.count}</span>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
