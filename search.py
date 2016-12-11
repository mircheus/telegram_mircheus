import database
answers = []
questions = ["Как тебя зовут?", "Сколько тебе лет?", "Кто твой любимый супергерой?"]

def qna(message):
    if message == 'Заполнить анкету':
        qst = questions[0]
        questions.remove(qst)
        return qst
    elif not questions:
        answers.append(message)
        database.insert(answers)
        return 'Анкета заполнена'
    else:
        answers.append(message)
        qst = questions[0]
        questions.remove(qst)
        return qst

song = ''
def find(message):
    question = ['Введите название песни']
    if message == 'Найти текст песни':
        qst = question[0]
        question.remove(qst)
        return qst
    elif not question:
        song = message
        print(song)
        return song

