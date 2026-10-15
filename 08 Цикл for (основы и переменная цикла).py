#цикл for
for i in range(5):
    print("Привет")

for i in range(3):
    print("*")
    print("---")


#Переменная цикла
for i in range(5):
    print(i)


#сумма чисел от 0 до 100
s = 0
for i in range(101):
    s = s + i#s+=i

print(s)


#range(начало, конец, шаг)
for i in range(5):#0,5,1
    print(i)


for i in range(5,10):#5,10,1
    print(i)


for i in range(1,10,2):#1 3 5 7 9
    print(i)


for i in range(10,1,-2):#10 8 6 4 2
    print(i)


for i in range(10):
    print(i+1, 10-i)


#Вывод чисел от a до b (a<b)
a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)

#Вывод чисел от a до b (a>b)
a = int(input())
b = int(input())
for i in range(a,b-1,-1):
    print(i)




















