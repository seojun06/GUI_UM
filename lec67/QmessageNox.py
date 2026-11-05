import sys
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox,QLayout, QLabel)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("3. KC ")
   
        button = QPushButton("luther")
        button.clicked.connect(self.ask)
        self.label = QLabel("")
        

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()


    def ask(self):
        answer = QMessageBox.question(
            self,"Question","If this World were mine"
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.label.setText("You got it")
        else:
            self.label.setText("You can't choose one")    
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())                