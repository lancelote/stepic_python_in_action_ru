"""
Тренировочная задача для того, чтобы научиться считывать данные с клавиатуры
и выводить информацию на экран.

От вас требуется написать программу, которая читает переданную через
стандартный ввод строку, используя функцию input, и выводит её же на
стандартный вывод, используя функцию print.

Обратите внимание на то, что необходимо использовать функцию input без
параметров, а также то, что выводить нужно только то, что было передано
на вход программе.

Формат ввода:
    Одна строка, содержащая произвольные символы, в том числе и пробельные.

Формат вывода:
    Единственная строка, содержащая строку, поданную на вход.

Sample Input 1:
    Hello World!
Sample Output 1:
    Hello World!

Sample Input 2:
    Word
Sample Output 2:
    Word
"""

import sys

for line in sys.stdin:
    print(line.rstrip())
