import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget
import random
from test2 import SocialSurvey


class CaptchaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Капча")
        self.label = QLabel("Введите капчу:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)
        self.generate_captcha()

        self.timer_label = QLabel("Таймер: 10")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.setStyleSheet(open("style.css").read())

    def verify_captcha(self):
        captcha = self.textbox.text()
        print("Проверка капчи:", captcha)

        if captcha.lower() == self.label.text():
            self.accept()
        else:
            self.textbox.setDisabled(True)
            self.timer_counter = 11
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Неправильная капча")

    def start_timer(self):
        self.timer_counter = 10
        self.timer.start()

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")

        if self.timer_counter == 0:
            self.timer.stop()
            self.textbox.setDisabled(False)
            self.generate_captcha()

    def generate_captcha(self):
        captcha1 = str(random.randint(1000, 9999))
        self.label.setText(captcha1)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно входа")

        self.label_username = QLabel("Имя пользователя:")
        self.textbox_username = QLineEdit()
        self.label_password = QLabel("Пароль:")
        self.textbox_password = QLineEdit()
        self.textbox_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_login = QPushButton("Войти")
        self.button_login.clicked.connect(self.login)

        self.captcha_dialog = CaptchaDialog(parent=self)
        self.captcha_dialog.setModal(True)

        self.login_attempts = 0

        layout = QVBoxLayout(self)
        layout.addWidget(self.label_username)
        layout.addWidget(self.textbox_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.textbox_password)
        layout.addWidget(self.button_login)

        self.setStyleSheet(open("style.css").read())

    def login(self):
        username = self.textbox_username.text()
        password = self.textbox_password.text()

        if username == "1" and password == "1":
            self.test = SocialSurvey()
            self.test.show()
        else:
            self.captcha_dialog.start_timer()

            if self.captcha_dialog.exec() == QDialog.DialogCode.Accepted:
                QMessageBox.information(self, "Успех", "Вход выполнен после капчи")
            else:
                QMessageBox.warning(self, "Ошибка", "Неверные данные и капча")
                self.login_attempts = 0
                self.generate_captcha()


app = QApplication(sys.argv)
exe = LoginWindow()
exe.show()
sys.exit(app.exec())
