import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout,QVBoxLayout,QGridLayout,QPushButton,QLineEdit
)
from PyQt5.QtCore import Qt

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("practice 2026-10-08")
        self.setFixedSize(400,200)
        self.setStyleSheet("background-color: #f0f0f0;")

        main_layout = QGridLayout()



        label1 = QLabel("",self)
        label1.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet(
            f"background-color:Yellow;"
        )

        layout2 = QVBoxLayout ()

        label2 = QLabel("",self)
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet(
            f"background-color:red;"
        )

        label3 = QLabel("",self)
        label3.setAlignment(Qt.AlignCenter)
        label3.setStyleSheet(
            f"background-color:blue;"
        )

        label4 = QLabel("",self)
        label4.setAlignment(Qt.AlignCenter)
        label4.setStyleSheet(
            f"background-color:green;"
        )

        main_layout.addWidget(label1,0,0,2,1)
        main_layout.addWidget(label2,0,1)
        main_layout.addWidget(label3,1,1)
        
        self.setLayout(main_layout)

        #버튼
        button1 = QPushButton("버튼1")
        button1.setFixedSize(100,100)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        
        main_layout.addLayout(button_layout, 0, 1)

        #글자
        text_input = QLineEdit()
        text_input.setPlaceholderText("이름 입력하세요")
        main_layout.addWidget(text_input,0, 1)
        main_layout.addLayout(button_layout, 2, 1)
        


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
