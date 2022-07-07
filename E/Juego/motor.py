from Entity.Entity import *
from Utils.Point import Point
from Utils.Board import Board
from Utils.Menu import Menu

menu = Menu ("Game actions", "~~> ")
menu.add("move", 1)
menu.add("attack", 2)

moveMenu = Menu ("Move menu", "-/>")
moveMenu.add("Left", 4)
moveMenu.add("Up", 8)
moveMenu.add("Right", 6)
moveMenu.add("Down", 2)

b = Board (5)
b.spawn (Shotgunner('alex', 0, 0))
b.spawn (Sniper ('eva', 3, 4))
current_round = 0

b.showBoard()
print("Turn:", b.entities.get(current_round%b.entities.size).toString())
option = menu.runSelection()
while (option != 0):
    if (option == 1):
        mm = moveMenu.runSelection()
        if (mm == 2):
            b.move(b.entities.get(current_round%b.entities.size), Point (0, -1))
        elif (mm == 4):
            b.move(b.entities.get(current_round%b.entities.size), Point(-1, 0))
        elif (mm == 6):
            b.move(b.entities.get(current_round%b.entities.size), Point(1, 0))
        elif (mm == 8):
            b.move(b.entities.get(current_round%b.entities.size), Point(0, 1))
    elif (option == 2):
        b.attack(b.entities.get(current_round%b.entities.size), b.entities.get((current_round+1)%b.entities.size))
    current_round+=1
    print("Turn:", b.entities.get(current_round%b.entities.size).toString())
    b.showBoard()
    option = menu.runSelection()



"""
b = Board(5)
alex = Sniper('alex', 0, 0)
eva = Shotgunner('eva', 4, 4)
b.spawn(alex)
b.spawn(eva)
b.move(eva, Point(0, 1))
# b.attack(alex, eva)
b.attack(eva, alex)
b.showBoard()
"""
