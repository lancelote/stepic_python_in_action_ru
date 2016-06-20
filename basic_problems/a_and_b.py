"""A and B
Задача на работу со строками.

Многим знакома детская загадка:

    А и Б сидели на трубе.
    А упало, Б пропало.
    Что осталось на трубе?

Перевод, (какой я смог найти):

    A and B sat in the tree.
    A had fallen, B was stolen.
    What's remaining in the tree?

Напишите программу, которая считывает два имени и выводит стихотворение,
в котором вместо A и B используются эти имена.

Формат ввода:
    Два имени, разделённых переносом строки. Первое имя должно заменять A,
    второе −− B.

Формат вывода:
    Три строки стихотворения с заменёнными A и B.

Sample Input:
    X
    Y

Sample Output:
    X and Y sat in the tree.
    X had fallen, Y was stolen.
    What's remaining in the tree?
"""


TEXT = "{X} and {Y} sat in the tree.\n" \
       "{X} had fallen, {Y} was stolen.\n" \
       "What's remaining in the tree?"


def a_and_b():
    x = input().rstrip()
    y = input().rstrip()
    data = {'X': x, 'Y': y}
    print(TEXT.format(**data))

if __name__ == '__main__':
    a_and_b()
