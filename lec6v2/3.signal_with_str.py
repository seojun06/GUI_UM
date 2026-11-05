import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    # str 데이터를 함께 보내는 signal
    key_typed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        # emit 한 str -> label.setText(str) 로 전달
        self.key_typed.connect(self.label.setText)

    def init_ui(self):
        self.setWindowTitle("3. Signal with str")
        self.label = QLabel("Type any key")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def keyPressEvent(self, event):
        self.key_typed.emit(event.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

