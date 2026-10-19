import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget) :
    key_typed = pyqtSignal(str)


    def __init__(self):
        super().__init__()
        self.init_ui()
        self.key_typed.connect(self.label.setText)


    def init_ui(self):
        self.setWindowTitle("3")
        self.label = QLabel("if this world were mine")
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
