import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    key_pressed = pyqtSignal(str)
    mouse_pressed = pyqtSignal(str)
    mouse_moved = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        # signal 두 개 -> 같은 slot 하나
        self.key_pressed.connect(self.show_message)
        self.mouse_pressed.connect(self.show_message)
        self.mouse_moved.connect(self.show_message)

    def init_ui(self):
        self.setWindowTitle("6. Two Signals, One Slot")
        self.label = QLabel("Type a key or click")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def keyPressEvent(self, event):
        self.key_pressed.emit(f"Key: {event.text()}")

    def mousePressEvent(self, event):
        self.mouse_pressed.emit("Mouse clicked")
    
    def mouseMoveEvent(self, event):
        self.mouse_moved.emit("Mouse moved to " + str(event.pos()))

    # slot
    def show_message(self, text):
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
