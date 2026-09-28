import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

def on_click():
    lbl.setText(le.text())
    lbl.adjustSize()

app = QApplication(sys.argv)
window = QWidget()

lbl = QLabel("결과", window)
lbl.move(20, 20)
le = QLineEdit(window)
le.move(20, 50)
btn = QPushButton("출력", window)
btn.move(20, 85)

btn.clicked.connect(on_click)

window.show()
sys.exit(app.exec())
