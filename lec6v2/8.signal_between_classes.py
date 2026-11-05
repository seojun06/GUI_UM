import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal

# 화면이 없는 클래스: 숫자만 세고, 바뀌면 signal 을 보냄 (누가 받는지는 모름)
class Counter(QObject):
    changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.value = 0

    def add_one(self):
        self.value += 1
        self.changed.emit(self.value)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = Counter()
        self.init_ui()
        # Counter 의 signal -> 창의 slot
        self.counter.changed.connect(self.show_value)

    def init_ui(self):
        self.setWindowTitle("8. Signal Between Classes")
        self.label = QLabel("0")
        button = QPushButton("+1")
        button.clicked.connect(self.counter.add_one)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()

    # slot
    def show_value(self, value):
        self.label.setText(str(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

