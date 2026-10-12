import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout,QVBoxLayout
)
from PyQt5.QtCore import Qt



class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Layout Test")
        self.setFixedSize(400,400)
        self.setStyleSheet("background-color:#f0f0f0;")

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        label = QLabel("1",self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color:yellow; color: black; font-size = 24px;"
        )    
    
        h_layout.addWidget(label)

        v_boxes = {"red":"a", "blue": "b", "cyan":"c", "green": " d"}

        for i, color in enumerate(v_boxes.keys()):
            label = QLabel(v_boxes.get(color),self)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(
                f"background-color : {color}; color: black; font-size: 24px;"
            )
            v_layout.addWidget(label)

        v_layout.addLayout(v_layout)
        self.setLayout(h_layout)    
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
