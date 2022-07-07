class Point:
    def __init__ (self, x, y):
        """
        Point(x:int, y:int)
        Creates a new point with coordinates x and y
        """
        self.x = x
        self.y = y

    def distanceTo (self, point):
        """
        distanceTo (point:Point)
        Returns the distance from this point to the other point passed as parameter
        """
        return (((self.x - point.x) ** 2) + ((self.y - point.y) ** 2)) ** (1/2)
