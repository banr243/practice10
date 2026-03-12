# ввод параметров
def input_matrix(name):
    rows = int(input(f"Количество строк матрицы {name}: "))
    cols = int(input(f"Количество столбцов матрицы {name}: "))

    matrix = []
    print(f"Вводи матрицу {name} построчно (через пробел):")

    for i in range(rows):
        while True:
            row = input(f"Строка {i + 1}: ").split()
            if len(row) != cols:
                print("❌ Неверное количество элементов, попробуй ещё раз")
                continue
            matrix.append([int(x) for x in row])
            break

    return matrix


# отрисовка матриц
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{x:5}" for x in row))
    print()


# сложение 
def add_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Матрицы должны быть одного размера")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


# умножение
def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Количество столбцов A должно совпадать с количеством строк B")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s += A[i][k] * B[k][j]
            row.append(s)
        result.append(row)
    return result


# транспонирование матриц
def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result


# вывод операций
if __name__ == "__main__":
    print("=== КАЛЬКУЛЯТОР МАТРИЦ ===")

    A = input_matrix("A")
    B = input_matrix("B")

    print("\nМатрица A:")
    print_matrix(A)

    print("Матрица B:")
    print_matrix(B)

    # Сложение складок Савелия
    try:
        print("A + B:")
        print_matrix(add_matrices(A, B))
    except ValueError as e:
        print("Сложение невозможно:", e)

    # Умножение - наверное, не 100%
    try:
        print("A * B:")
        print_matrix(multiply_matrices(A, B))
    except ValueError as e:
        print("Умножение невозможно:", e)

    # Транспонирование
    print("Транспонированная A:")
    print_matrix(transpose_matrix(A))

