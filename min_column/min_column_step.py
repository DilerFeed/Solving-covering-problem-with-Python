"""
Програма для побудови покриття методом мінімального стовпчика - максимального рядка.
6КН-22б, Іщенко Гліб
Працює тільки з матрицями (таблицями) на 7 рядків та 10 стовпців (10-й - ціни)!
"""

# Матриця за умовою
I = [1, 0, 0, 1, 0, 0, 0, 0, 1, 2] #1
O = [1, 0, 0, 0, 0, 0, 1, 0, 1, 1] #2
P = [1, 0, 1, 0, 0, 1, 0, 1, 0, 3] #3
A = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2] #4
S = [0, 1, 0, 1, 1, 0, 1, 0, 1, 4] #5
D = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1] #6
F = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1] #7
matrix = [I, O, P, A, S, D, F]

matrix_ad = [I[:], O[:], P[:], A[:], S[:], D[:], F[:]] # 2-а матриця. Копія оригінальної мітриці для копіювання рядків у масив формування покриття
matrix_ed = [I[:], O[:], P[:], A[:], S[:], D[:], F[:]] # 3-я матриця. Копія оригінальної матриці для видалення в ній стовпців

Cover = [1, 1, 1, 1, 1, 1 ,1 , 1, 1] # Покриття для перевірки
Temp = [0, 0, 0, 0, 0, 0, 0 ,0, 0] # Тимчасовий масив для операцій з рядками матриці

total_cost = 0 # Лічильник затраченої ціни
used_rows = [] # Лічильник використаних рядків для формування покриття
columns = 9 # Лічильнник стовпців 3-ї матриці
ones_indexes = [] # Лічильник стовпців, які були видалені в 3-й матриці

# Цикл алгоритму сетоду мінімального стовпчика - максимального рядка
# Поки тимчасовий масив покриття не дорівнює покриттю
while Temp != Cover:
    # Кількість стовпців 3-ї матриці оновлюємо згідно кількості одиниць в отриманому в кінці минулої ітерації циклу рядку
    columns -= len(ones_indexes)
    # Оновлюємо лічільники
    top_ones = 10
    cur_ones = 0
    top_column = 0
    column_rows_with_ones = []
    top_row = 0

    # Знаходимо стовпчик з найменшою кількістю одиниць з стовпчиків 3-ї матриці
    for i in range(columns):
        cur_ones = 0
        for j in range(7):
            cur_ones += matrix_ed[j][i]
        if cur_ones < top_ones:
            top_ones = cur_ones
            top_column = i
    print(f"Стовпчик з найменшою кількістю одиниць з стовпчиків 3-ї матриці - {top_column + 1}")

    # Виписуємо в окремий масив номера рядків, які мають одиницю в стовпчику, який ми тільки що отримали
    for j in range(7):
        if matrix_ed[j][top_column] == 1:
            column_rows_with_ones.append(j)

    # Знаходимо з цих рядків у 2-й матриці той, що має найбільшу кількість одиниць
    top_ones = 0
    for row_num in column_rows_with_ones:
        cur_ones = 0
        for i in range(9):
            cur_ones += matrix_ad[row_num][i]
        if cur_ones > top_ones:
            top_ones = cur_ones
            top_row = row_num
    print(f"Рядок, який має одиницю в обраному ствпчику, і в той ж час має найбільшу кількість одиниць - {top_row + 1}")

    # Копіюємо з отриманого рядка одиниці в тимчасовий масив, а також записуємо номер цього рядка та його ціну
    for i in range(9):
        if matrix_ad[top_row][i] == 1:
            Temp[i] = 1
            if i not in ones_indexes:
                ones_indexes.append(i)
    total_cost += matrix_ad[top_row][9]
    used_rows.append(top_row)
    print(f"Вигляд тимчасового масива на даний момент - {Temp}, затрачена ціна на даний момент - {total_cost}, використано рядки - {used_rows}")

    # Робимо поправку індексів стовпчиків для викреслення, так як після їх викреслення індекси будуть змінюватися
    for k in range(len(ones_indexes)):
        if k != 0:
            ones_indexes[k] -= k

    # Вертаємо 3-ю матрицю в оригінальний стан, а потім видаляємо необхідні стовпчики
    matrix_ed = [I[:], O[:], P[:], A[:], S[:], D[:], F[:]]
    for column_index in ones_indexes:
        for j in range(7):
            del matrix_ed[j][column_index]
    print(f"Вигляд 3-ї матриці на даний момент - {matrix_ed}")

print(f"Знайдено покриття за ЦІНУ {total_cost} за {len(used_rows)} РЯДКИ(ІВ), а саме: ", end="")
for row in used_rows:
    if row != used_rows[-1]:
        print(f"{row + 1}, ", end="")
    else:
        print(f"{row + 1}.")