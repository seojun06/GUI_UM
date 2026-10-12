import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QMessageBox)
from PyQt5.QtCore import Qt

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Close Event Example")
        label = QLabel("<p>Try closing this window with the <b>X</b> button.</p>")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        self.show()

    def closeEvent(self, event):
        # 창을 닫기 전에 확인
        answer = QMessageBox.question(
            self, "Quit", "Are you sure you want to quit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            print("Closing the window.")
            event.accept()   # 닫기 진행
        else:
            print("Close cancelled.")
            event.ignore()   # 닫기 취소

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
