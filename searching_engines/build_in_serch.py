import numpy as np

from busy_time_meter import busy_time_meter


@busy_time_meter
def np_search(key, S):
    '''
    Функція пошуку
    :param key: ключ пошуку
    :param S: масив на якому реалізується пошук
    :return: позиція елемента
    '''
    key_position =np.where(S == key)
    return key_position