import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton

class CarQuiz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Quiz")
        self.questions = [
            {
                'question': "Какая форма кузова вам нравится?",
                'options': ["Седан", "Хэтчбек", "Внедорожник", "Купе"]
            },
            {
                'question': "Какой тип топлива вы предпочитаете?",
                'options': ["Бензин", "Дизель", "Электричество", "Гибрид"]
            },
            {
                'question': "Какой размер вам важен?",
                'options': ["Компактный", "Средний", "Большой", "Огромный"]
            },
            {
                'question': "Какой у вас бюджет?",
                'options': ["Низкий", "Средний", "Высокий"]
            }
        ]
        self.answers = []
        self.current_question = 0
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.question_label = QLabel()
        layout.addWidget(self.question_label)

        self.options = []
        for _ in range(len(self.questions[self.current_question]['options'])):
            option = QRadioButton()
            layout.addWidget(option)
            self.options.append(option)

        next_button = QPushButton("Далее")
        next_button.clicked.connect(self.next_question)
        layout.addWidget(next_button)

        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.setText(question['question'])

        options = question['options']
        for i in range(len(options)):
            self.options[i].setText(options[i])
            self.options[i].setChecked(False)

    def next_question(self):
        selected_option = None
        for option in self.options:
            if option.isChecked():
                selected_option = option.text()
                break

        if selected_option is not None:
            self.answers.append(selected_option)
            self.current_question += 1

            if self.current_question < len(self.questions):
                self.show_question()
            else:
                self.show_result()

    def show_result(self):
        result_label = QLabel()
        result_label.setText("Ваша идеальная марка машины: " + self.calculate_result())
        layout = self.layout()
        layout.itemAt(layout.count() - 1).widget().hide()
        layout.addWidget(result_label)

    def calculate_result(self):
        # В этом примере просто используем фиктивные результаты
        return "Toyota"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quiz = CarQuiz()
    quiz.show()
    sys.exit(app.exec())
