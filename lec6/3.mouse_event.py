import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt, QTime

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.start_time = None
        self.is_dark = False
        self.font_size = 12
        self.control_pressed = False

        self.setMouseTracking(True)

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Mouse Press Example")
        self.label = QLabel("<p>Click anywhere with any mouse button.</p>")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.show()

    def mousePressEvent(self, event):
        self.start_time = QTime.currentTime()
        # 어떤 버튼이 눌렸는지 확인
        if event.button() == Qt.MouseButton.LeftButton:
            button = "Left"
        elif event.button() == Qt.MouseButton.RightButton:
            button = "Right"
        elif event.button() == Qt.MouseButton.MiddleButton:
            button = "Middle"
        else:
            button = "Other"
        x, y = event.pos().x(), event.pos().y()
        print(f"{button} button pressed at ({x}, {y})")
        self.label.setText(f"<p><b>{button}</b> button pressed at ({x}, {y})</p>")

    def mouseReleaseEvent(self, event): 
        
        if self.start_time is not None:
            current_time = QTime.currentTime()

            elapsed_time = self.start_time.msecsTo(current_time)
            seconds = elapsed_time / 1000

            print(f"Mouse button released after {seconds:.2f} seconds")

            self.label.setText(
                f"<p>Mouse button released<br>"
                f"Held for <b>{seconds:.2f} seconds</b></p>"
            )

            # 시간 초기화
            self.start_time = None

        print("Mouse button released")

    def mouseMoveEvent(self, event):
        x,y = event.pos().x(), event.pos().y()
        self.label.setText(f"<p>Mouse position: ({x},{y})</p>")


    def mouseDoubleClickEvent(self, event):
        self.is_dark = not self.is_dark
        if self.is_dark:
            self.setStyleSheet("background-color: black; color: white;") 
        else:
            self.setStyleSheet("")
            print("Double-clicked! Dark mode: ", self.is_dark)   

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0 and self.control_pressed:
            self.font_size = min(self.font_size + 2,60)
        elif event.angleDelta().y() < 0 and self.control_pressed:
            self.font_size = max(self.font_size -2, 6)

        else:
            return
        print("Font size:", self.font_size)
        self.update_font()   
         

    def update_font(self):
        font = self.label.font()
        font.setPointSize(self.font_size)
        self.label.setFont(font)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Control:
            self.control_pressed = True

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Control:
            self.control_pressed = False     


    def enterEvent(self, event) :
        print("Mouse entered")
        self.label.setText("<p>가세요</p>")
        self.setStyleSheet("background-color: lightgreen;")

    def leaveEvent(self, event):
        print("Mouse left")
        self.label.setText("<p>가지마요</p>")
        self.setStyleSheet("background-color: lightpink;")


    def resizeEvent(self, event):
        size = event.size()
        print(f"resized: {size.width()} x {size.height()}")
        self.update_label()

    def update_label(self):
        self.label.setText(
            f"<p>Size: <b>{self.width()} x {self.height()}</b></p>"
            f"<p>Position: <b>({self.x()}, {self.y()})</b></p>"
        )    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
