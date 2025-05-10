# Дан граф друзей в социальной сети, где:
# Ключ словаря — имя пользователя (вершина графа).
# Значение — список друзей (смежные вершины).

# Пример входных данных:
friends_graph = {
    "Анна": ["Борис", "Виктор", "Дарья"],
    "Борис": ["Анна", "Виктор"],
    "Виктор": ["Анна", "Борис", "Дарья"],
    "Дарья": ["Анна", "Виктор", "Елена"],
    "Елена": ["Дарья"]
}

# Написать функции, которые выполняют следующие операции:
# 1. Поиск друзей (соседей) для заданного пользователя.
# 2. Проверка, являются ли два пользователя друзьями (есть ли ребро между вершинами).
# 3. Поиск изолированных пользователей (вершин без рёбер).


def findFrends(person):
    print(friends_graph[person])


findFrends(input('person >> '))


def checkFriendship(person1, person2):
    if person1 in friends_graph[person2]:
        return True
    else:
        return False


print(checkFriendship(input('person1 >> '), input('person2 >> ')))


def searchSingles(person):
    if len(friends_graph[person]) < 1:
        return True
    else:
        return False


print(searchSingles(input('person >> ')))
