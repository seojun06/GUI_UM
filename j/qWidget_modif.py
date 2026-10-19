import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 GUI")
window.resize(400, 320)
window.setStyleSheet("background-color: blue")

window.show()
sys.exit(app.exec())

