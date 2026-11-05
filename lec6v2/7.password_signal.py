import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    # "clicked" 보다 의미 있는 signal 을 직접 만듦
    login_ok = pyqtSignal(str)
    login_failed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.login_ok.connect(self.welcome)
        self.login_failed.connect(self.show_error)

    def init_ui(self):
        self.setWindowTitle("7. Password Check Signal")
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Password (1234)")
        self.edit.setEchoMode(QLineEdit.EchoMode.Password)
        button = QPushButton("Login")
        button.clicked.connect(self.check_password)   # 내장 signal
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def check_password(self):
        # 결과에 따라 다른 signal 을 보냄
        if self.edit.text() == "1234":
            self.login_ok.emit("Student")
        else:
            self.login_failed.emit()

    # slot
    def welcome(self, name):
        self.label.setText(f"Welcome, {name}!")

    # slot
    def show_error(self):
        self.label.setText("Wrong password")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
