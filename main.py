import numpy as np


def sum_of_main_diagonal(arr) -> int:
    a = np.asarray(arr)

    # Если это не двумерный массив
    if a.ndim != 2:
        raise ValueError("Входные данные должны быть двумерной матрицей")

    # Длина главной диагонали
    n = min(a.shape)

    # Пустая матрица
    if n == 0:
        return 0

    idx = np.arange(n)
    return int(np.sum(a[idx, idx]))

# Примеры
arr1 = np.array([[11,  2,  3,  4],
                 [ 5, 11,  7,  8],
                 [ 9, 10, 11, 12],
                 [13, 14, 15, 11]])

arr2 = np.array([[1, 1],
                 [1, 2]])

arr3 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr4 = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])

print(f"Пример 1:\n{arr1}\nОтвет: {sum_of_main_diagonal(arr1)}\n")

print(f"Пример 2:\n{arr2}\nОтвет: {sum_of_main_diagonal(arr2)}\n")

print(f"Пример 3:\n{arr3}\nОтвет: {sum_of_main_diagonal(arr3)}\n")

print(f"Пример 4:\n{arr4}\nОтвет: {sum_of_main_diagonal(arr4)}\n")



# Тесты
def test() -> None:
    # Квадратные
    assert sum_of_main_diagonal([[1, 2], [3, 4]]) == 5
    assert sum_of_main_diagonal(np.eye(4, dtype=int)) == 4

    # Прямоугольные
    assert sum_of_main_diagonal([[1, 2, 3],
                                 [4, 5, 6]]) == 1 + 5

    assert sum_of_main_diagonal([[1, 2],
                                 [3, 4],
                                 [5, 6]]) == 1 + 4

    # Пустые
    assert sum_of_main_diagonal(np.empty((0, 0))) == 0
    assert sum_of_main_diagonal(np.empty((0, 5))) == 0
    assert sum_of_main_diagonal(np.empty((5, 0))) == 0

    print("Все тесты пройдены")


if __name__ == "__main__":
    test()
