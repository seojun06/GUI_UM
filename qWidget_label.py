import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.resize(300,50)

lbl = QLabel("안녕하세요", window)
lbl.setText("내용이 바뀌었습니다.")
lbl.setAlignment(Qt.AlignmentFlag.AlignLeft) #위치
lbl.resize(window.size())

window.show()
sys.exit(app.exec())