from random import * #случайные числа


attack = 25 #атака
hp = 100 #здоровье
max_hp = 100 #максимальное
flag_block = 0 #блок
money = 10 #деньги

#функция для боя
def fight():
    global money, attack, hp, flag_block#делаем, чтобы функция увидела переменные
    #характеристики врага
    enemy_attack = 25
    enemy_hp = 100
    enemy_block = 0
    while True:
        if enemy_hp <= 0:
            print("Враг повержен!")
            break  # прерываем цикл
        if hp <= 0:
            print("Вы проиграли!")
            break
        #наши действия
        print(f"Ваша атака: {attack} Ваша здоровье: {hp}")
        print(f"Атака врага: {enemy_attack} Здоровье врага: {enemy_hp}")
        print('Выберите действие:')
        print('1 - атака')
        print('2 - защита')
        print('3 - улучшить атаку')
        n = input()
        if n == '1':
            if enemy_block == 1:#если враг выставил защиту
                print("Враг блокирует ваш удар!")
                enemy_block = 0
            else:
                r = randint(1, 100)
                if r <= 90:  # попадание
                    damage = attack + randint(-10, 10)
                    enemy_hp -= damage
                    print(f"Вы попали! Ваш урон: {damage}. Здоровье врага: {enemy_hp}")
                    if enemy_hp <= 0:
                        print("Враг повержен!")
                        break#прерываем цикл
                else:  # промах
                    print(f"Промах!")
        elif n == "2":
            print("Вы успешно выставили защиту")
            flag_block = 1
        elif n == "3":
            r = randint(3,10)
            attack += r
            print(f"Вы улучшили атаку на {r}, ваша атака {attack}")
        else:
            print("Неверное значение. Ход переходит врагу.")
        #действия врага
        n = randint(1,3)
        if n == 1:
            if flag_block == 1:#игрок выставил защиту
                print("Враг атакует, но вы успешно блокируете удар врага!")
                flag_block = 0
            else:
                r = randint(1,100)
                if r <= 90:  # попадание
                    damage = enemy_attack + randint(-10, 10)
                    hp -= damage
                    print(f"Враг попал! Его урон: {damage}. Ваше здоровье {hp}")
                    if hp <= 0:
                        print("Вы проиграли!")
                        break
                else:  # промах
                    print(f"Враг промахнулся!")
        elif n == 2:
            print("Враг выставил защиту")
            enemy_block = 1
        elif n == 3:
            r = randint(3, 10)
            enemy_attack += r
            print(f"Враг улучшил атаку на {r}, атака врага {enemy_attack}")

#функция для лекаря
def health():
    global money, hp, max_hp
    if money >= 5:#если денег хватает
        hp = max_hp
        money-=5
        print(f"Вы исцелены! Осталось монет {money}")
    else:
        print("У тебя нет денег!")

#главное меню
while True:
    print('Выберите действие:')
    print('1 - пойти в бой')
    print('2 - пойти к лекарю (5 монет)')
    n = input()
    if n == '1':
        fight()
    elif n == '2':
        health()
    else:
        print("неверный выбор")  

