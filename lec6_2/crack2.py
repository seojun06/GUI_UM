import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget) :
    clicked_at = pyqtSignal(int, int)


    def __init__(self):
        super().__init__()
        self.init_ui()
        self.clicked_at.connect(self.show_position)


    def init_ui(self):
        self.setWindowTitle("4")
        self.label = QLabel ("asdfas")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()


    def mousePressEvent(self, event):
        self.clicked_at.emit(event.x(),event.y())


    def show_position(self, x , y):
        self.label.setText(f"clicked at ({x},{y})")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())