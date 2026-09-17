#проверка на кратность
a=5
if a%2==0:
    print("чётное")
else:
    print("нечётное")
#проверка последней цифры
if a % 10 == 9:
    print("ПОСЛЕДНЯЯ ЦИФРА 9")


#и, and
print(0 and 0)#0
print(0 and 1)#0
print(1 and 0)#0
print(1 and 1)#1


#или, or
print(0 or 0)#0
print(0 or 1)#1
print(1 or 0)#1
print(1 or 1)#1


#Времена года
m = int(input())
if m == 12 or m==1 or m==2:
    print("зима")
elif 3<=m<=5:
    print("весна")
elif 6<=m<=8:
    print("лето")
elif 9<=m<=11:
    print("осень")
else:
    print("ошибка")
    

#Принадлежность 3
x = int(input())
if -30<x<=-2 or 7<x<=25:
    print("Принадлежит")
else:
    print("Не принадлежит")




