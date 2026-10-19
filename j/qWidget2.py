import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 GUI")
window.resize(400, 320)
window.setStyleSheet("background-color: red")

lbl = QLabel("오늘은", window)
lbl.move(160, 90)

name_lbl = QLabel("몇일", window)
name_lbl.move(120, 120)
edit = QLineEdit(window)
edit.move(120, 150)


btn = QPushButton("대답", window)
btn.resize(100, 40)
btn.move(130, 190)

window.show()
sys.exit(app.exec_())
