#проверка на кратность
a=5
if a%2==0:
    print("чётное")
else:
    print("нечётное")
#проверка последней цифры
if a % 10 == 3:
    print("ПОСЛЕДНЯЯ ЦИФРА 3")


#логические операции
print(1 and 0 or 1)#1
print(0 and 1 and 1 or 1 and 1)#1
print(1 or 1 and 0)#1

#Цвета колеса рулетки 🌶 (начало решения)️
a = int(input())
if a == 0:
    print("зеленый")
elif 1<=a<=10 or 19<=a<=28:
    if a%2==0:
        print("черный")
    else:
        print("красный")
elif 11<=a<=18 or 29<=a<=36:
    if a%2!=0:
        print("черный")
    else:
        print("красный")
else:
    print("ошибка ввода")






