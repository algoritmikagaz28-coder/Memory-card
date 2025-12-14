from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QRadioButton,
                             QVBoxLayout, 
                             QHBoxLayout, 
                             QLabel, 
                             QGroupBox, 
                             QPushButton,
                             QButtonGroup)
from random import shuffle, randint
#подгрузка необходимых библиотек

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#класс

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Синий', 'Белый'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Иглу', 'Хата', 'Юрта'))
questions_list.append(Question('Какой цвет темнее?', 'FireBrick', 'Red', 'Crimson', 'Salmon'))
questions_list.append(Question('Какой цвет светлее?', 'LemonChiffon', 'Moccasin', 'PaleGoldenrod', 'Khaki'))
questions_list.append(Question('Какое оружие можно найти в экспериментальном воздушном грузе, НО нельзя эвакуироваться с ним (Arena Breakout)', 'RPG', 'Golden Deagle', 'Bizon', 'M3A1'))
questions_list.append(Question('Выбери перевод слова "переменная"', 'variable', 'variation', 'variant', 'changing'))
questions_list.append(Question('Какое оружие может быть парным (Blood Strike)?', 'Glock, Uzi', 'Magnum', 'P90', 'Deagle'))

#добавление вопросов в список

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo Card')

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Чулымцы')
rbtn3 = QRadioButton('Смурфы')
rbtn4 = QRadioButton('Алеуты')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
#создание виджетов

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
#присоединение виджетов

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')
#создание виджетов

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
#присоединение виджетов

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
#создание виджетов

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
#присоединение виджетов

RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
#присоединение виджетов

layout_card = QVBoxLayout()
#создание виджета

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
#присоединение виджетов

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
#показать результат

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
#показать вопрос

answers = [rbtn1, rbtn2, rbtn3, rbtn4] #массив ответов

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
#создание вопроса

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
#показать следующий вопрос

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')
#проверка ответа

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
#вызов нужной функции

#q = Question('Выбери перевод слова "переменная"', 'variable', 'variation', 'variant', 'changing')
#ask(q)
#надо чтобы программа задала первый вопрос

btn_OK.clicked.connect(click_OK) #присоединение к функции

window.setLayout(layout_card)
window.resize(400, 300)
window.show()

window.score = 0
window.total = 0

next_question()

app.exec()
