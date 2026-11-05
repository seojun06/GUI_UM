
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QGridLayout,
    QPushButton,
    QMessageBox
)

from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.expression = ""
        self.result_shown = False

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("2025112206 엄서준 - 계산기")
        self.setFixedSize(380, 520)

        # 결과 표시창
        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(64)

        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #222222;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 30px;
                padding-right: 12px;
            }
        """)

        # GridLayout
        grid = QGridLayout()
        grid.setSpacing(8)
        grid.setContentsMargins(12, 12, 12, 12)

        grid.addWidget(self.display, 0, 0, 1, 4)

        # 숫자 버튼
        numbers = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3"
        ]

        for i, text in enumerate(numbers):
            button = QPushButton(text)
            button.setFixedSize(73, 66)

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FAFAFA;
                    color: black;
                    border: 1px solid #CCCCCC;
                    border-radius: 7px;
                    font-size: 20px;
                }
                QPushButton:pressed {
                    background-color: #DDDDDD;
                }
            """)

            button.clicked.connect(self.number_clicked)

            row = i // 3 + 2
            col = i % 3

            grid.addWidget(button, row, col)

        # C 버튼
        clear_button = QPushButton("C")
        clear_button.setFixedSize(73, 66)

        clear_button.setStyleSheet("""
            QPushButton {
                background-color: #D6D6D6;
                color: black;
                border: none;
                border-radius: 7px;
                font-size: 18px;
            }
        """)

        clear_button.clicked.connect(self.clear_display)
        grid.addWidget(clear_button, 1, 0)

        # 삭제 버튼
        back_button = QPushButton("←")
        back_button.setFixedSize(73, 66)

        back_button.setStyleSheet("""
            QPushButton {
                background-color: #D6D6D6;
                color: black;
                border: none;
                border-radius: 7px;
                font-size: 22px;
            }
        """)

        back_button.clicked.connect(self.backspace)
        grid.addWidget(back_button, 1, 1) ##여까지 했음 일단

        # 연산자 버튼
        operators = ["÷", "×", "-", "+"]

        for i, text in enumerate(operators):
            button = QPushButton(text)
            button.setFixedSize(73, 66)

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FF9900;
                    color: white;
                    border: none;
                    border-radius: 7px;
                    font-size: 22px;
                }
                QPushButton:pressed {
                    background-color: #DD8000;
                }
            """)

            button.clicked.connect(self.operator_clicked)

            if i < 2:
                grid.addWidget(button, 1, i + 2)
            else:
                grid.addWidget(button, i, 3)

        # 0 버튼
        zero_button = QPushButton("0")
        zero_button.setFixedSize(154, 66)

        zero_button.setStyleSheet("""
            QPushButton {
                background-color: #FAFAFA;
                color: black;
                border: 1px solid #CCCCCC;
                border-radius: 7px;
                font-size: 20px;
            }
        """)

        zero_button.clicked.connect(self.number_clicked)
        grid.addWidget(zero_button, 5, 0, 1, 2)

        # 소수점 버튼
        dot_button = QPushButton(".")
        dot_button.setFixedSize(73, 66)

        dot_button.setStyleSheet("""
            QPushButton {
                background-color: #FAFAFA;
                color: black;
                border: 1px solid #CCCCCC;
                border-radius: 7px;
                font-size: 20px;
            }
        """)

        dot_button.clicked.connect(self.number_clicked)
        grid.addWidget(dot_button, 5, 2)

        # = 버튼
        equal_button = QPushButton("=")
        equal_button.setFixedSize(73, 146)

        equal_button.setStyleSheet("""
            QPushButton {
                background-color: #315CE0;
                color: white;
                border: none;
                border-radius: 7px;
                font-size: 24px;
            }
            QPushButton:pressed {
                background-color: #2445AD;
            }
        """)

        equal_button.clicked.connect(self.calculate)
        grid.addWidget(equal_button, 4, 3, 2, 1)

        self.setLayout(grid)

    # 화면 표시
    def update_display(self):
        text = self.expression
        text = text.replace("*", "×")
        text = text.replace("/", "÷")

        if text == "":
            text = "0"

        self.display.setText(text)

    # 숫자 입력
    def number_clicked(self):
        digit = self.sender().text()
        self.input_number(digit)

    def input_number(self, digit):
        if self.result_shown:
            self.expression = ""
            self.result_shown = False

        # 소수점 중복 입력을 허용
        # 여러 개 입력해도 계산할 때 오류 검사
        self.expression += digit

        self.update_display()

    # 연산자 입력
    def operator_clicked(self):
        operator = self.sender().text()

        if operator == "×":
            operator = "*"
        elif operator == "÷":
            operator = "/"

        self.input_operator(operator)

    def input_operator(self, operator):
        if self.result_shown:
            self.result_shown = False

        if self.expression == "":
            if operator == "-":
                self.expression = "-"
            else:
                return
        else:
            self.expression += operator  ##여가짜ㅣ

        self.update_display()

    # 전체 초기화
    def clear_display(self):
        self.expression = ""
        self.result_shown = False
        self.display.setText("0")

    # 마지막 글자 삭제
    def backspace(self):
        if self.result_shown:
            self.clear_display()
            return

        self.expression = self.expression[:-1]
        self.update_display()

    # 수식 계산
    def calculate(self):
        if self.expression == "":
            return

        expression = self.expression

        try:
            numbers = []
            operators = []

            current = ""
            expect_number = True

            # 숫자와 연산자 분리
            for ch in expression:

                if ch.isdigit() or ch == ".":
                    current += ch

                elif ch in "+-*/":

                    if current == "":
                        if ch == "-" and expect_number:
                            current = "-"
                            continue
                        raise ValueError

                    # 소수점이 여러 개면 잘못된 수식
                    if current.count(".") > 1:
                        raise ValueError

                    # 소수점만 입력한 경우도 오류
                    if current == "." or current == "-.":
                        raise ValueError

                    numbers.append(float(current))
                    current = ""

                    operators.append(ch)
                    expect_number = True

                else:
                    raise ValueError

                if ch.isdigit() or ch == ".":
                    expect_number = False

            # 마지막 숫자 확인
            if current == "" or current == "-" or current == ".":
                raise ValueError

            if current.count(".") > 1:
                raise ValueError

            numbers.append(float(current))

            if len(numbers) != len(operators) + 1:
                raise ValueError

            # 곱셈과 나눗셈 먼저 계산
            i = 0

            while i < len(operators):

                if operators[i] == "*":
                    numbers[i] = numbers[i] * numbers[i + 1]
                    numbers.pop(i + 1)
                    operators.pop(i)

                elif operators[i] == "/":

                    if numbers[i + 1] == 0:
                        raise ZeroDivisionError

                    numbers[i] = numbers[i] / numbers[i + 1]
                    numbers.pop(i + 1)
                    operators.pop(i)

                else:
                    i += 1

            # 덧셈과 뺄셈 계산
            result = numbers[0]

            for i in range(len(operators)):

                if operators[i] == "+":
                    result += numbers[i + 1]

                elif operators[i] == "-":
                    result -= numbers[i + 1]

            # 결과 표시
            result = round(result, 10)

            if result == int(result):
                result = int(result)

            self.expression = str(result)
            self.update_display()
            self.result_shown = True

        except ZeroDivisionError:

            QMessageBox.critical(
                self,
                "오류",
                "0으로 나눌 수 없습니다.",
                QMessageBox.Ok
            )

            self.clear_display()

        except Exception:

            # 오류 수식도 계산기 기호로 표시
            error_expression = expression.replace("*", "×")
            error_expression = error_expression.replace("/", "÷")

            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("잘못된 수식")
            msg.setText("계산할 수 없는 수식입니다.")
            msg.setInformativeText(error_expression)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()

    # 키보드 입력
    def keyPressEvent(self, event):
        key = event.key()
        text = event.text()

        if text != "" and (text.isdigit() or text == "."):
            self.input_number(text)

        elif text in ["+", "-", "*", "/"] and text != "":
            self.input_operator(text)

        elif key == Qt.Key_Return or key == Qt.Key_Enter:
            self.calculate()

        elif key == Qt.Key_Backspace:
            self.backspace()

        elif key == Qt.Key_Escape:
            self.clear_display()

        else:
            super().keyPressEvent(event)

    # 창 종료 확인
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "종료 확인",
            "계산기를 종료할까요?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
