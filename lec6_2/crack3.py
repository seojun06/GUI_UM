import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget) :
    key_pressed = pyqtSignal(str)
    mouse_pressed = pyqtSignal(str)
    mouse_moved = pyqtSignal(str)


    def __init__(self):
        super().__init__()
        self.init_ui()
        self.key_pressed.connect(self.show_message)
        self.mouse_pressed.connect(self.show_message)
        self.mouse_moved.connect(self.show_message)


    def init_ui(self):
        self.setWindowTitle("4")
        self.label = QLabel ("asdfas")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def keyPressEvent(self, event):
            self.key_pressed.emit(f"masdkfj: {event.text()}")

    def mousePressEvent(self, event):
        self.mouse_pressed.emit("mouse")
            

    def mouseMoveEvent(self, event):
        self.mouse_pressed.emit(f"mouse clicekdfesd: {event.pos().x()}, {event.pos().y()}")



    def show_message(self, text):
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())