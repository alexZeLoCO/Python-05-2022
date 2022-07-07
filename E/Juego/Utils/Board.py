from Utils.Point import Point
from Utils.EntityLL import EntityLL
from Entity.Entity import Entity


class Board:
    def __init__(self, size):
        """
        Board (size:int)
        Creates a new empty board of size by size
        """
        if (size <= 0):
            print("Err. size must be positive.")
            return False
        self.board = []
        for i in range(0, size, 1):
            self.board.append([])
            for j in range(0, size, 1):
                self.board[i].append(0)
        self.entities = EntityLL()

    def showBoard(self):
        """
        showBoard (void)
        Shows the current board
        """
        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board[i]), 1):
                print(self.board[i][j], end=" ")
            print()

    def validPosition(self, position):
        """
        validPosition (position:Point)
        Checks if the position is valid.
        A position is valid if it is contained in the boards limits and is not
        occupied by an entity.
        Returs True if the position is valid.
        """
        return (position.x >= 0 and position.x < len(self.board)
                and position.y >= 0 and position.y < len(self.board[0])
                and self.board[len(self.board)-position.y-1][position.x] == 0)

    def spawn(self, entity):
        """
        spawn (entity:Entity)
        Spawns the entity. By doing so, the entity will appear on the board
        and will be added to this game's entities structure.
        Checks if the position is valid.
        Returns True if the position of this entity is valid and therefore, the entity was spawned.
        """
        if (self.validPosition(Point(entity.point.x, entity.point.y))):
            print("Spawning:", entity.toString())
            self.entities.add(entity)
            self.board[len(self.board)-entity.point.y -
                       1][entity.point.x] = entity.name[0]
            return True
        return False

    def despawn(self, entity):
        """
        despawn (entity:Entity)
        Despawns the entity. By doing so, the entity will no longer appear on the board
        and will be removed from this game's entities structure.
        """
        print("Despawning: ", entity.toString())
        self.entities.remove(entity)
        self.board[len(self.board)-entity.point.y-1][entity.point.x] = 0

    def move(self, entity, new_position):
        """
        move (entity:Entity, new_position:Point)
        Moves the entity to the new_position.
        By doing so, the board will no longer show the entity on the old point
        and will instead show it on the new_position.
        Checks if the new_position is valid.
        The board representation, entities structure and entity data will be updated.
        Returns True if the movement was successful
        """
        if (self.validPosition(new_position)):
            self.board[len(self.board)-new_position.y -
                       1][new_position.x] = entity.name[0]
            self.board[len(self.board)-entity.point.y-1][entity.point.x] = 0
            old_entity = entity
            entity.point.x = new_position.x
            entity.point.y = new_position.y
            self.entities.switch(old_entity, entity)
            return True
        return False

    def attack(self, attacker, target):
        """
        attack (attacker:Entity, target:Entity)
        attacker: attacks the target
        target: defends from the attacker's attack
        Returns True if the target survives
        """
        if (not target.defend(attacker)):
            self.despawn(target)
            return False
        return True
