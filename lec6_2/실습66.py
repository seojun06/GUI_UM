import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal


class startWindow(QWidget):
    window_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

        self.window_clicked.connect(self.add_one)

    def init_ui(self):
        self.setWindowTitle("2. My Own Slot")
        self.setFixed(300, 200)
        self.label = QLabel("Clicked: 0")

        self.click_me = QLabel("CLCICICICICICICIIC")
        self.click_me.setStyleSheet("font-size: 16px; color: gray; background-color: red")
        self.click_me.setFixedHeight(50)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addwidget(self.click_me)
        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        if self.click_me.geometry().contains(event.pos()):

            self.window_clicked.emit()



    def add_one(self):
        self.count += 1
        self.label.setText(f"Clicked: {self.count}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

