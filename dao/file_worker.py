import pickle

import numpy as np


def data_str(filename):
    with open(filename, "r", encoding='utf-8'):
        nums = []
        for i in open(filename):
            nums.append(i)  # читання файлу по рядках і заповнення списку результатом
    print(nums)
    return nums


def save_bin_file(arr_to_file, filename):
    """
    Функція запису випадкової/впорядкованної вибірки у файл
    :param arr_to_file: масив випадкових значень - вибірка
    :param filename: ім'я файла
    :return: нічого
    """
    # Сохранение
    with open(filename, "wb") as file:
        pickle.dump(arr_to_file, file)
    return


def read_bin_file(filename: str) -> np.array:
    """
    Функція завантаження випадкової/впорядкованної вибірки з файлу
    :param filename: ім'я файла
    :return: array
    """
    with open(filename, "rb") as file:
        loaded_array = pickle.load(file)
    return loaded_array
