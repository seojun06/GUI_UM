import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
)
from PyQt5.QtCore import Qt


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QHBoxLayout")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Create horizontal box layout
        layout = QVBoxLayout()

        label = QLabel("수직 레이아웃 1", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: red; color: black; font-size: 24px;"
        )
        layout.addWidget(label)

        label = QLabel("수직 레이아웃 2", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: blue; color: black; font-size: 24px;"
        )
        layout.addWidget(label)


        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
