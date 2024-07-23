import prompt


def welcome_user():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def gameplay(question):

    print(f'Question: {question}')
    answer = (input('Your answer: '))
    return answer


def check_answer(answer, correct_answer, name):
    k = 0
    while k < 3:
        
        if answer == correct_answer:
            print('Correct!')
            k += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer} \n Let's try again, {name}!")
            break
    if k == 3:
        print(f'Congratulations, {name}!')
