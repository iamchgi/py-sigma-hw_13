import numpy as np

from busy_time_meter import busy_time_meter


@busy_time_meter
def np_search(key, s):
    """
    Функція пошуку
    :param key: ключ пошуку
    :param s: масив на якому реалізується пошук
    :return: позиція елемента
    """
    key_position =np.where(s == key)
    return key_position