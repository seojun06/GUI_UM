import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    key_typed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()
        # signal 하나 -> slot 두 개 (emit 한 번에 둘 다 실행)
        self.key_typed.connect(self.label.setText)   # slot 1
        self.key_typed.connect(self.count_key)       # slot 2

    def init_ui(self):
        self.setWindowTitle("5. One Signal, Two Slots")
        self.label = QLabel("Type any key")
        self.count_label = QLabel("Keys: 0")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.count_label)
        self.setLayout(layout)
        self.show()

    def keyPressEvent(self, event):
        self.key_typed.emit(event.text())

    # slot 2
    def count_key(self, text):
        self.count += 1
        self.count_label.setText(f"Keys: {self.count}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

