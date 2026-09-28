import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


def on_click():
    user_message = line_edit1.text()

    if user_message:
        lable2.setText(user_message)
        image_label.show()
        window2.show()
    #window2.show()
    #lable2.setText(user_message)
    #lable1.setText("1")


def on_click_clear():
    lable2.clear()  
    window2.hide()

app = QApplication(sys.argv)

#window1
window1 = QWidget()
window1.setWindowTitle("Window 1")
window1.setStyleSheet("background-color: lightblue")
window1.setFixedSize(400,300)


#window2
window2 = QWidget()
window2.setWindowTitle("Window2")
window2.setStyleSheet("background-color: lightblue")
window2.setFixedSize(400,300)




lable1=QLabel("맨체스터시티의 챔스우승 횟수는?",window1)
lable1.setStyleSheet("font-size: 18px; font-weight: bold; color: darkgreen")
lable1.resize(400,100)
lable1.setAlignment(Qt.AlignCenter)



lable2=QLabel(window2)
lable2.setStyleSheet("font-size: 18px; font-weight: bold; color: darkgreen")
lable2.resize(400,100)
lable2.setAlignment(Qt.AlignCenter)





line_edit1 = QLineEdit(window1)
line_edit1.resize(250, 30)
line_edit1.move(80,100)
line_edit1.setStyleSheet("font-size: 14px; padding: 5px; border: 2px solid darkblue; border-radius: 10px")

#line_edit1.setText("정답을 적어주세요")
line_edit1.setPlaceholderText("정답을 적어주세요")

button1 = QPushButton("확인",window1)
button1.setStyleSheet("background-color: lightgreen; font-size:16px; font-weight: bold; color: darkgreen")
button1.resize(100,80)
button1.move(100,180)
button1.clicked.connect(on_click)

button_clear = QPushButton("지우기",window1)
button_clear.resize(100, 80)
button_clear.move(200, 180)
button_clear.clicked.connect(on_click_clear)

pixmap = QPixmap("/Users/User/Documents/GUI프로그래밍/GUI-Programming/assets/image.png")
image_label = QLabel(window2)
image_label.setPixmap(pixmap)
image_label.resize(200,200)
image_label.move(125,100)
image_label.setScaledContents(True)


window1.show()
sys.exit(app.exec_())