#вывод чисел от 1 до 5
i = 0
while i<5:
    i+=1
    print(i)

    
#читаем все числа, пока пользователь не введёт 0
#ввод до 0
a=int(input())
while a!=0:
    #действия
    a=int(input())

print("КОНЕЦ!")

    
#сумма чётных чисел введённых пользователем. 0 - конец ввода
a=int(input())
s=0
while a!=0:
    if a%2==0:
        s+=a
    a=int(input())
print(s)


#Наименьшее число. 0 - конец ввода
a=int(input())
mini = 10000000
while a!=0:
    if a < mini:
        mini = a
    a=int(input())
print(mini)

#Индекс наименьшего числа. 0 - конец ввода
a=int(input())
i=0
imini = 0
mini = 10000000
while a!=0:
    if a < mini:
        mini = a
        imini = i
    a=int(input())
    i+=1
print(mini, imini)

