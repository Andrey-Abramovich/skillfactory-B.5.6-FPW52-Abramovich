import random # для игры против компьютера (тупого)


field = [[' ']*3 for i in range(3)] # задаем игровое поле 3х3

def greet(): # приветствие
    print('-'*22)
    print('    Вас приветствует')
    print("         игра  ")
    print('-' * 22)
    print("    Крестики-Нолики ")
    print('-' * 22)
    print("   Формат ввода: x,y")
    print("   x - это строка")
    print("   y - это столбец")
    print('-' * 22)
    print("       НАЧИНАЕМ!")
    print('-' * 22)


def show_field(f): # вывод игрового поля
    print(' ' * 16)
    print(f'   | 0 | 1 | 2 |')
    print('-' * 16)

    for i, row in enumerate(field):
        row_str = f' {i} | {" | ".join(field[i])} |'
        print(row_str)
        print('-' * 16)

def ask_user(f): # запрашиваем у игрока координаты Х
    while True:
        coordinate = input(' Введите координаты x, y от 0 до 2: ').split()

        if len(coordinate) != 2:
            print('Введите 2 значения: ')
            continue

        x, y = coordinate
        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите только цифры')
            continue

        x, y = int(x), int(y)
        if not(0 <= x <= 2) or not (0 <= y <= 2):
            print('Введите верные значения от 0 до 2')
            continue

        if field[x][y] != ' ':
            print('Эта клетка занята')
            continue
        return x, y

def ask_comp(): # запрос координат от компьютера за 0
    while True:
        coordinate_x = random.randrange(0, 3)
        coordinate_y = random.randrange(0, 3)


        x, y = coordinate_x, coordinate_y


        if field[x][y] != ' ':

            continue
        return x, y

def win(f): # проверка условия победы
    coordinate_win = (((0,0), (0,1), (0,2)),
                      ((1,0), (1,1), (1,2)),
                      ((2,0), (2,1), (2,2)),
                      ((0,0), (1,0), (2,0)),
                      ((0,1), (1,1), (2,1)),
                      ((0,2), (1,2), (2,2)),
                      ((0,0), (1,1), (2,2)),
                      ((0,2), (1,1), (2,0))
    )
    for i in coordinate_win:

        list = []
        for point in i:
            list.append(field[point[0]][point[1]])
        if list == ['X', 'X', 'X']:
            print(f'Поздравляю! выиграл игрок {crossname} за Крестик!')
            return True
        if list == ['0', '0', '0']:
            print(f'Поздравляю! выиграл Terminator за Нолик!')
            return True
    return False



greet()
crossname = input('Введите имя игрока за Крестик: ')

count = 0
while True:

    count +=1
    show_field(field)
    if count % 2 == 0:
        print(f'Сейчас ходит Terminator за  Нолик ')
        x, y = ask_comp()

    else:
        print(f"Сейчас ходит {crossname} за Крестик ")
        x, y = ask_user(field)



    if count % 2 == 0:
        field[x][y] = '0'
    else:
        field[x][y] = 'X'

    if win(field):
        show_field(field)
        break


    if count == 9:
        print('Ничья!')
        break