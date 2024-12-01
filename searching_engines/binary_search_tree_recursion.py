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

# Функція вставки нового вузола із заданим ключем у BST
def insert_node(node, key):
    # Якщо дерево порожнє, поверніть новий вузол
    if node is None:
        return Node(key)
    # В іншому випадку рухайтесь до низу дерева
    if key < node.key:
        node.left = insert_node(node.left, key)
    elif key > node.key:
        node.right = insert_node(node.right, key)
    # Return the (unchanged) node pointer
    return node


# Функція пошуку ключа в BST
def search_node(root, key):
     # Базові випадки: root має значення null або ключ присутній у корені
     if root is None or root.key == key:
        return root
     # Ключ більший за ключ root
     if root.key < key:
         return search_node(root.right, key)
     # Ключ менший за ключ root
     return search_node(root.left, key)

@busy_time_meter
def search_node_recursion(root, key):
    return search_node(root, key)