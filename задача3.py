# Создайте программу для игры в ""Крестики-нолики"".

pole = [["_","_","_"],["_","_","_"],["_","_","_"]]
players = ["X","0"]
def printpole(array):
    for i in array:
        for j in i:
            print(j,end=" ")
        print()
printpole (pole)
def step_player(xo, array):
    flag = False
    while not flag:
        khod_x = input(f"Ход {xo}, введите через пробел значение хода по вертикали и горизонтали от 1 до 3: ")
        khod = khod_x.split()
        if (array[int(khod[0])-1][int(khod[1])-1] == "_"):
            flag = True
            array[int(khod[0])-1][int(khod[1])-1] = xo
        else:
            print("Данный ход не возможен")
def check_win (array):
    flag = False
    for i in range (0,3):
        if (array[i][0] == array[i][1]) & (array[i][0] == array[i][2]) & (array[i][0] != "_"):
            flag = True
            return flag
            #break       
        if (array[0][i] == array[1][i]) & (array[0][i] == array[2][i]) & (array[0][i] != "_"):
            flag=True
            return flag
            #break
    if (array[0][0] == array[1][1]) & (array[0][0] == array[2][2]) & (array[0][0] != "_"):
        flag=True
        return flag
    if (array[0][2] == array[1][1]) & (array[0][2] == array[2][0]) & (array[0][2] != "_"):
        flag=True
        return flag
    return flag

for i in range (0, 9):
    printpole(pole)
    step_player(players[i%2], pole)
    if check_win(pole):
        print(f"Победил игрок {players[i%2]}")
        printpole(pole)
        break
    if i == 8:
        print("Ничья!")