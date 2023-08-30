
# Задание 1
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания.

num1=int(input('Vvedite 1oe chislo:'))
num2=int(input('Vvedite 2oe chislo:'))
if(num1!=num2):
    if(num2>num1):
       print(num1,num2)
    else:
        print(num2,num1)
else:
    print('Chisla ravni')



# Задание 2
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

mesac=int(input('Vvedite mesac:'))
if(mesac==1):
    print('Yanvar')
elif(mesac==2):
    print('Fevral')
elif (mesac == 3):
    print('Mart')
elif (mesac == 4):
    print('Aprel')
elif (mesac == 5):
    print('May')
elif(mesac == 6):
    print('Iyun')
elif (mesac == 7):
    print('Iyul')
elif (mesac == 8):
    print('Avqust')
elif (mesac == 9):
    print('Sentyabr')
elif (mesac == 10):
    print('Okyabr')
elif (mesac == 11):
    print('Noyabr')
elif (mesac == 12):
    print('Dekabr')
else:
    print('V qodu 12 mesasev!')

# Задание 3
# Пользователь вводит с клавиатуры диаметр окружности. В зависимости от выбора пользователя посчитать
# площадь или периметр окружности.
diam=int(input('Vvedite diametr: '))
oper=input("Viberite ploshad(S) ili perimetr(P): ")
if oper == 'S':
    print(3.14*diam/2*diam/2)
elif oper == 'P':
    print(3.14*diam)
else:
    print("Vvedite S ili P")