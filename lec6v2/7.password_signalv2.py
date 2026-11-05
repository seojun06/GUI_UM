import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    # "clicked" 보다 의미 있는 signal 을 직접 만듦
    login_ok = pyqtSignal(str)       # 사용자 이름을 보냄
    login_failed = pyqtSignal(str)   # 실패 이유를 보냄

    def __init__(self):
        super().__init__()
        # 사용자 3명: {아이디: 비밀번호}
        self.users = {
            "user1": "1111",
            "user2": "2222",
            "user3": "3333",
        }
        self.init_ui()
        self.login_ok.connect(self.welcome)
        self.login_failed.connect(self.show_error)

    def init_ui(self):
        self.setWindowTitle("7. Password Check Signal v2")
        self.user_edit = QLineEdit()
        self.user_edit.setPlaceholderText("User (user1, user2, user3)")
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Password")
        self.edit.setEchoMode(QLineEdit.EchoMode.Password)
        button = QPushButton("Login")
        button.clicked.connect(self.check_password)   # 내장 signal
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.user_edit)
        layout.addWidget(self.edit)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def check_password(self):
        user = self.user_edit.text()
        password = self.edit.text()
        # 결과에 따라 다른 signal 을 보냄
        if user not in self.users:
            self.login_failed.emit(f"Unknown user: {user}")
        elif self.users[user] != password:
            self.login_failed.emit("Wrong password")
        else:
            self.login_ok.emit(user)

    # slot
    def welcome(self, name):
        self.label.setText(f"Welcome, {name}!")

    # slot
    def show_error(self, reason):
        self.label.setText(reason)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
