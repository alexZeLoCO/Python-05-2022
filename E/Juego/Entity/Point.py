class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    """
    def setX (self, x):
        self.x = x

    def setY (self, y):
        self.y = y
    """
    def distance (self, position):
        return ((self.x - position.x) ** 2 + (self.y - position.y) ** 2) ** (1/2)

p = Point (0, 0)
print(p.distance(Point (1, 2)))