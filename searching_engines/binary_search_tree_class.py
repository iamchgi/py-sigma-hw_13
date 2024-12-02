"""
Приклад пошуку на бінарному дереві -
Time complexity: O(h), де h – висота BST.
Auxiliary Space: O(h), максимальний обсяг простору, необхідний для зберігання стека рекурсії пропорційний - h.

"""
from busy_time_meter import busy_time_meter


class Node:
    # Конструктор для створення нового вузла
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinThree:
    def __init__(self):
        self.root = None

    # Функція вставки нового вузла із заданим ключем у BST
    def insert(self, key) -> None:
        # Якщо дерево порожнє, створіть новий вузол
        if self.root is None:
            self.root = Node(key)
            return
        # В іншому випадку рухайтесь до низу дерева
        marker  = self.root
        while True:
            if key < marker.key:
                if marker.left is None:
                    marker.left = Node(key)
                    return
                marker = marker.left
            else:
                if marker.right is None:
                      marker.right = Node(key)
                      return
                marker = marker.right

    @busy_time_meter
    # Функція пошуку ключа в BST
    def search(self, key) -> Node:
        # Базові випадки: root має значення null або ключ присутній у корені
        # if self.root is None or self.root.key == key:
        #     return self.root
        # В іншому випадку рухайтесь до низу дерева
        marker = self.root
        while marker is not None and marker.key != key:
            if key < marker.key:
                  marker = marker.left
            else: marker = marker.right

        return marker