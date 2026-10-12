import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QLineEdit,
    QPushButton, QMessageBox, QRadioButton, QButtonGroup
)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QTextEdit and QLineEdit")
        self.setFixedSize(500, 260)

        # label
        self.text_label = QLabel("?", self)
        self.text_label.setGeometry(20, 20, 100, 30)

        # radio buttons
        self.male_radio = QRadioButton("알랄라", self)
        self.male_radio.setGeometry(20, 60, 100, 30)

        self.female_radio = QRadioButton("하무드하비비", self)
        self.female_radio.setGeometry(20, 100, 100, 30)

        #self.male_radio.clicked.connect(lambda: self.result_label.seText(self.male_radio.text()))


        self.sex_group = QButtonGroup(self)
        self.sex_group.addButton(self.male_radio)
        self.sex_group.addButton(self.female_radio)


        # Button
        self.button = QPushButton("제출", self)
        self.button.setGeometry(20, 140, 100, 30)
        self.button.clicked.connect(self.on_click)

        # result display label
        self.result_label = QLabel("Result", self)
        self.result_label.setGeometry(20, 180, 460, 100)
        self.result_label.hide()

    def on_click(self):
        selected = self.sex_group.checkedButton()
        if selected:
            self.result_label.setText(f"반갑습니다! {selected.text()}님.")
        else:
            self.result_label.setText("?을 선택해주세요.")
        self.result_label.show()        


    """  def on_click(self):
        if self.male_radio.isChecked():
            self.result_label.setText("사용자의 성별은 남성입니다.")
        elif self.female_radio.isChecked():
            self.result_label.setText("사용자의 성별은 여성입니다.")
        else:
            self.result_label.setText("성별을 선택해주세요.")
        self.result_label.show()"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
