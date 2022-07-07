from Utils.Point import Point
from random import random

class Entity:
    def __init__ (self, name:str, x:int, y:int, hp:int, ap:int, rp:int, luck:int):
        """
        Entity (name:str, x:int, y:int, hp:int, ap:int, rp:int, luck:float [0, 1))
        name: name of the entity
        x: x position of the entity
        y: y position of the entity
        hp: health points
        ap: attack points
        rp: range points
        luck: chance of dodging an attack
        """
        self.name = name
        self.point = Point(x, y)
        self.hp = hp
        self.ap = ap
        self.rp = rp
        self.luck = luck

    def defend (self, attacker):
        """
        defend (attacker:Entity)
        This entity defends the attacker's attack.
        Returns True if the defender is still alive after the attack.
        """
        if (self.point.distanceTo(attacker.point) <= attacker.rp):
            if (random() > self.luck):
                self.hp-=attacker.ap
                if (self.hp <= 0):
                    print(attacker.name, " has killed ", self.name, "!", sep="")
                    return False
                print(attacker.name, " has drained some health from ", self.name, sep="")
                return True
            print(attacker.name, "could not hit", self.name)
            return True
        print(attacker.name, "is way too far from", self.name, "to attack.")
        return True

    def toString (self):
        """
        toString (void)
        Returns a text-based representation of this entity
        """
        return str(self.name)  + " [" + str(self.name)[0] + "] (" + str(self.point.x) + "," + str(self.point.y) + ")" + " hp:" + str(self.hp) + " ap:" + str(self.ap) + " rp:" + str(self.rp) + " luck:" + str(self.luck)

class Sniper (Entity):
    def __init__ (self, name, x, y):
        """
        Sniper (name:str, x:int, y:int)
        Creates a new Sniper.
        """
        super().__init__(name, x, y, 5, 150, 100, 0.7)

class Shotgunner (Entity):
    def __init__ (self, name, x, y):
        """
        Shotgunner (name:str, x:int, y:int)
        Creates a new Shotgunner.
        """
        super().__init__(name, x, y, 75, 75, 1, 0.2)