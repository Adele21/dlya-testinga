# Задание 1
# Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел. Результат
# вычислений вывести на экран.
num1=int(input('Vvedite 1oe chislo:'))
num2=int(input('Vvedite 2oe chislo:'))
num3=int(input('Vvedite 3ee chislo:'))
print(' Summa:',num1+num2+num3,'\n','Proizvedenie:', num1*num2*num3)
# Задание 2
# Пользователь вводит с клавиатуры три числа. Первое
# число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке,
# третье число — задолженность за коммунальные услуги. Необходимо вывести
# на экран сумму, которая останется у пользователя после
# всех выплат.
num1=int(input('Zarplata:'))
num2=int(input('Kredit v banke:'))
num3=int(input('Kommunalnie:'))
print('posle oplati ostanetsa:',num1-num2-num3)
#
# Задание 3
# Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его
# диагоналей.
d1=int(input('Dlina 1oy diaqonali:'))
d2=int(input('Dlina 2oy diaqonali:'))
print('Ploshad:',d1*d2/2)