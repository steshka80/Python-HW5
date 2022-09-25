# Создайте программу для игры с конфетами человек против человека.

from random import random
import random
sweets = 2021
players = ["player1", "player2-bot"]
rand_player = players[random.randint(0,1)]
print (f"{rand_player} начинает первым")
print (f"в вазе конфет: {sweets}")
if rand_player == players[1]:
    p2=random.randint(1,28)
    sweets -= p2
    print (f"{rand_player} взял конфет {p2}, осталось {sweets}")
    print (f"в вазе конфет: {sweets}")
while sweets > 0:
    p1=int(input(f"введите количество конфет от 1 до 28 для {players[0]}: "))
    sweets -= p1

    print (f"в вазе конфет: {sweets}")
    if sweets <= 0:
        print (f"Победил {players[1]}")
        break
    if (sweets == 1):
        p2 = 1
    if (sweets <= 29) & (sweets != 1):
        p2 = sweets - 1
    else:
        p2=random.randint(1,28)
    sweets -= p2

    print (f"{rand_player} взял конфет {p2}, осталось {sweets}")
    if sweets <= 0:
        print (f"Победил {players[0]}")
        