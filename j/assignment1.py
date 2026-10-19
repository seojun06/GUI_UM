import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

# ==============================================================================
# [과제 1 자기 설명 및 AI 사용 명시]
# 학번: 20251122
# 이름: 엄서준
#
# Q1. State -> Event -> Action -> Update -> Feedback 설명:
# State: 현재 프로그램의 상태로, 이름과 학번이 입력된 상태를 의미한다.
# Event: 사용자가 학생증 발급 버튼이나 초기화 버튼을 클릭하는 것이다.
# Action: 입력된 학번을 검사하고 입학년도, 인증코드, 등급을 계산한다.
# Update: 계산된 결과를 화면의 라벨과 학생증 이미지에 반영한다.
# Feedback: 발급 완료 메시지와 인증코드, 등급 등을 사용자에게 보여준다.
#
# Q2. 학번 인증코드 계산 로직 설명:
# 8자리 학번의 각 자릿수를 하나씩 정수로 변환하여 모두 더한다.
# 예를 들어 20251122는 2+0+2+5+1+1+2+2 = 15가 된다.
#
# Q3. AI 도구 사용 여부 및 수정 내용:
# AI 도구를 사용하여 TODO 부분의 구현 방법과 코드 구조를 참고하였다.
# 이후 과제에서 요구하는 학번, 이름, 인증코드, 등급 및 화면 출력 조건에 맞게
# 코드를 수정하고 적용하였다.
#
# ==============================================================================


class StudentCardApp(QWidget):
    def __init__(self):
        super().__init__()

        self.img_path = Path(__file__).parent / "profile.png"
        

        self.init_ui()

    def init_ui(self):
        # TODO 1: 윈도우 제목 설정 및 창 크기 고정
        self.setWindowTitle("20251122 엄서준 - 스마트 학생증 발급기")
        self.setFixedSize(450, 420)

        self.lbl_status = QLabel(
            "이름과 학번을 입력한 후 발급 버튼을 누르세요.",
            self
        )
        self.lbl_status.setAlignment(Qt.AlignCenter)
        self.lbl_status.resize(400, 30)
        self.lbl_status.move(25, 20)

        self.le_name = QLineEdit(self)
        self.le_name.setPlaceholderText("이름을 입력하세요")
        self.le_name.resize(250, 30)
        self.le_name.move(100, 60)

        self.le_id = QLineEdit(self)
        self.le_id.setPlaceholderText("학번 8자리를 입력하세요")
        self.le_id.resize(250, 30)
        self.le_id.move(100, 100)

        self.btn_issue = QPushButton("학생증 발급", self)
        self.btn_issue.resize(120, 35)
        self.btn_issue.move(95, 150)

        # TODO 2: 학생증 발급 버튼 클릭 이벤트 연결
        self.btn_issue.clicked.connect(self.on_click_issue)

        self.btn_clear = QPushButton("초기화", self)
        self.btn_clear.resize(120, 35)
        self.btn_clear.move(235, 150)

        # TODO 3: 초기화 버튼 클릭 이벤트 연결
        self.btn_clear.clicked.connect(self.on_click_clear)

        self.lbl_photo = QLabel(self)
        self.lbl_photo.resize(120, 120)
        self.lbl_photo.move(165, 200)
        self.lbl_photo.hide()

        self.lbl_info = QLabel("", self)
        self.lbl_info.setAlignment(Qt.AlignCenter)
        self.lbl_info.resize(400, 60)
        self.lbl_info.move(25, 330)

    def on_click_issue(self):
        name = self.le_name.text().strip()
        student_id = self.le_id.text().strip()

        # TODO 4: 입력 검증
        if name == "":
            QMessageBox.warning(
                self,
                "입력 오류",
                "이름을 입력하세요."
            )
            return

        if len(student_id) != 8 or not student_id.isdigit():
            QMessageBox.warning(
                self,
                "입력 오류",
                "학번은 8자리 숫자로 입력하세요."
            )
            return

        # TODO 5: 학번 앞 4자리로 입학년도 추출
        admission_year = student_id[:4]

        # TODO 6: 학번 8자리 숫자의 각 자릿수 합 계산
        checksum = sum(int(digit) for digit in student_id)

        # TODO 7: 학번 끝자리의 홀수/짝수에 따라 등급 구분
        last_digit = int(student_id[-1])

        if last_digit % 2 == 1:
            grade = "BLUE 등급 (일반)"
        else:
            grade = "GOLD 등급 (우수)"

        # TODO 8: 결과 안내 문구 표시
        self.lbl_status.setText(
            f"{name} 학생 ({admission_year}학번) 발급 완료! "
            f"[인증코드: {checksum}]"
        )

        self.lbl_info.setText(
            f"입학년도: {admission_year}\n"
            f"등급: {grade}"
        )

        # profile.png 이미지 로드
        pixmap = QPixmap(str(self.img_path))
        

        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                120,
                120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.lbl_photo.setPixmap(pixmap)
            self.lbl_photo.setAlignment(Qt.AlignCenter)
            self.lbl_photo.show()

        else:
            QMessageBox.warning(
                self,
                "이미지 오류",
                "profile.png 파일을 찾을 수 없습니다."
            )

    def on_click_clear(self):
        # TODO 9: 입력창 지우기, 라벨 초기화, 사진 숨기기

        self.le_name.clear()
        self.le_id.clear()

        self.lbl_status.setText(
            "이름과 학번을 입력한 후 발급 버튼을 누르세요."
        )

        self.lbl_info.clear()

        self.lbl_photo.clear()
        self.lbl_photo.hide()


# ==============================================================================
# 프로그램 실행
# ==============================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = StudentCardApp()
    window.show()

    sys.exit(app.exec_())

