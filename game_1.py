"""угадай число ( комп сам загадывает и сам угадывает)"""
import numpy as np
def random_predict(number:int=1) -> int: # int=1 - это по умолчанию, -> int это что на выходе
    """ рандомно угадываем число 

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: количество попыток
    """
    count=0
    while True:
        count += 1
        predict_number=np.random.randint(1,101) # предпологаемое число
        if number == predict_number: # если загаданное равно предпологаемому, то выход
           break
    return count # количество попыток компьютера отгадать загаданное руками число

def score_game(predict_number) -> int:
    """ за какое в среднем количество попыток за 1000 подходов происходит угадывание

    Args:
        predict_number (_type_): число угадований

    Returns:
        int: среднее количество попыток
    """
    count_ls=[]
    np.random.seed(1)  # фиксация генерации random, это для воспроизводимости результата
    random_array=np.random.randint(1,101,size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score=int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за:{score}попыток')
    return score
# RUN
# здесь в качестве аргумента вызывается другая функция
if __name__ == '__main__':
     score_game(random_predict) # первый раз вызываем по умолчанию с number = 1
#print(f'количество попыток:{random_predict(10)}') # загаданное число руками
# а здесь загадывает рандомно компьютер
#print(f'количество попыток:{random_predict(np.random.randint(1,101))}')
