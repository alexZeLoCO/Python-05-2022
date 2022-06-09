class Board:
    def __init__ (self, size):
        if (size <= 0):
            print("Err. size must be positive.")
            return False
        self.board = []
        for i in range (0, size, 1):
            self.board.append([])
            for j in range (0, size, 1):
                self.board[i].append(0)

    def showBoard (self):
        for i in range (0, len(self.board), 1):
            for j in range (0, len(self.board[i]), 1):
                print(self.board[i][j], end=" ")
            print()

    def validPosition (self, position):
        return (position.x >= 0 and position.x < len(self.board)
            and position.y >= 0 and position.y < len(self.board[0])
            and self.board[len(self.board)-position.y-1][position.x] == 0)

    def spawn (self, entity):
        if (self.validPosition(Point(entity.point.x, entity.point.y))):
            self.board[len(self.board)-entity.point.y-1][entity.point.x] = entity.name[0]
            return True
        return False

    def move (self, entity, new_position):
        if (self.validPosition(new_position)):
            self.board[len(self.board)-new_position.y-1][new_position.x] = entity.name[0]
            self.board[len(self.board)-entity.point.y-1][entity.point.x] = 0
            entity.x = new_position.x
            entity.y = new_position.y
            return True
        return False

class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def setX (x):
        self.x = x

    def setY (y):
        self.y = y

class Entity:
    def __init__ (self, name:str, x:int, y:int):
        self.name = name
        self.point = Point(x, y)

    def toString (self):
        return str(self.name) + " (" + str(self.point.x) + "," + str(self.point.y) + ")"

b = Board(5)
b.showBoard()
alex = Entity('alex', 0, 1)
print("Spawning: ", alex.toString())
b.spawn(alex)
b.move(alex, Point(0, 2))
b.showBoard()