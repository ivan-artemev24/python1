#range(начало, конец, шаг)
for i in range(5):#0 1 2 3 4
    print(i)
for i in range(5,8):#5 6 7
    print(i)
for i in range(1,7,2):#1 3 5
    print(i)
for i in range(10,2,-2):#10 8 6 4
    print(i)

#сумма 5 чисел
summa = 0
for i in range(5):
    a = int(input())
    summa = summa+a#summa+=a
print(summa)

#сумма n чисел
summa = 0
n = int(input())
for i in range(n):
    a = int(input())
    summa = summa+a#summa+=a
print(summa)



#количество чётных чисел
k = 0
n = int(input())
for i in range(n):
    a = int(input())
    if a%2==0:
        k=k+1#k+=1
      
print(k)


#наименьшее из чисел
minimum = 1000000
n = int(input())
for i in range(n):
    a = int(input())
    if a < minimum:
        minimum = a
print(minimum)


#флаг
#есть ли среди чисел кратное 5
flag = 0
n = int(input())
for i in range(n):
    a = int(input())
    if a % 5 == 0:
        flag = 1

if flag:
    print("Есть")
else:
    print("Нет")


#если все числа положительные
flag = 1
n = int(input())
for i in range(n):
    a = int(input())
    if a<=0:
        flag = 0

if flag:
    print("Все положительные")
else:
    print("Не все")






