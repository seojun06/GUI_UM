import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    # int 두 개를 함께 보내는 signal
    clicked_at = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.clicked_at.connect(self.show_position)

    def init_ui(self):
        self.setWindowTitle("4. Signal with two ints")
        self.label = QLabel("Click anywhere")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        # emit(x, y) -> show_position(x, y)
        self.clicked_at.emit(event.x(), event.y())

    # slot
    def show_position(self, x, y):
        self.label.setText(f"Clicked at ({x}, {y})")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

