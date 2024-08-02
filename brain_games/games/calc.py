from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
START = 1
STOP = 10


def generate_question_and_answer():

    operation = choice(['+', '-', '*'])
    num_1 = randint(START, STOP)
    num_2 = randint(START, STOP)
    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    else:
        correct_answer = num_1 * num_2
    question = (f'{num_1}{operation}{num_2}')
    return question, correct_answer
