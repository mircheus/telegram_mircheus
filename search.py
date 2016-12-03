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

        return 'Анкета заполнена'
    else:
        answers.append(message)
        qst = questions[0]
        questions.remove(qst)
        return qst

