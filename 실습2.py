import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습2 - 사용자 정보 입력")
window.resize(500, 400)
window.setStyleSheet("background-color: lightgreen")

lbl = QLabel("안녕하세요, PyQt5!", window)
lbl.move(170, 90)


btn = QPushButton("클릭", window)
btn.resize(120, 40)
btn.move(180, 190)

window.show()
sys.exit(app.exec_())
