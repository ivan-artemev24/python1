from random import *
#r = randint(1,10)
#print(r)
#характеристики персонажа
hp = 100
attack = 10
armor = 5
money = 0

#характеристики врага
enemy_hp = 80
enemy_attack = 10
enemy_armor = 5
enemy_money = 0

while True:
    print(f"Ваша атака: {attack} Ваша здоровье: {hp}")
    print(f"Атака врага: {enemy_attack} Здоровье врага: {enemy_hp}")
    print('Выберите действие:')
    print('1 - атака')
    print('2 - защита')
    n = input()
    if n == '1':
        r = randint(1,100)
        if r <= 90:
            damage = attack + randint(-3,3)
            enemy_hp -= damage
            print(f"Вы попали по врагу! Ваш урон: {damage}. У врага {enemy_hp} здоровья")
            if enemy_hp <= 0:
                print("Враг повержен!")
                break
        else:
            print("Вы промахнулись!")
    elif n == "2":
        print("Защита")
    else:
        print("неверный вариант")

    #действия врага
    n = randint(1,3)
    if n == 1:
        pass

        
        






    
