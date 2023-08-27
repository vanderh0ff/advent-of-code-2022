from math import sqrt
class Position():
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z
        pass
    
    def __repr__(self) -> str:
        return f'x:{self.x} y:{self.y} z:{self.z}'

    def __eq__(self, other) -> bool:
        if isinstance( other, Position):
            if self.x == other.x and self.y == other.y and self.z == other.z:
                return True
            return False
        if isinstance( other, Node):
            return self.__eq__(other.position)
        return False
    
    def get_direction(self, position):
        dx = self.x - position.x
        dy = self.y - position.y
        if dy == 1:
            return 'V'
        if dy == -1:
            return '^'
        if dx == 1:
            return '>'
        if dx == -1:
            return '<'

    def get_distance(self, dest):
        dx = self.x - dest.x
        dy = self.y - dest.y
        dz = self.z - dest.z
        return sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        #return abs(dx) + abs(dy) + abs(dz)

class Node():
    def __init__(self, position :Position, parent=None ):
        self.position = position
        self.parent = parent
        self.f = 1000
        self.g = 1000
        self.h = 1000
        
    def __repr__(self):
        return f'position:{self.position}\nf:{self.f} g:{self.g} h:{self.h}\n'
    
    def __eq__(self, node):
        return node.position == self.position

    def __lt__(self, node):
        return self.f < node.f

    def get_distance(self, dest :Position):
        self.position.get_distance(dest)

    def get_direction(self):
        if self.parent:
            return self.position.get_direction(self.parent.position)
        return ' '

    def get_traversed(self):
        if not self.parent:
            return 1
        return self.parent.get_traversed() + 1


    def calc_values(self, end):
        self.g = self.get_traversed()
        self.h = self.position.get_distance(end)
        self.f = self.g + self.h

