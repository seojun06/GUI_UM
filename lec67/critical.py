import sys
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox,QLayout, QLabel,QLineEdit)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("4. matttt v2 ")
        self.edit = QLineEdit()
        self.edit.setPla
        button = QPushButton("67")
        button.clicked.connect(self.show_error)
        
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()


    def show_error(self):
        QMessageBox.critical(self,"Error","76767676767676767676767676767676767")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())                