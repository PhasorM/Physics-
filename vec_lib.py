import math
from typing import Union, Tuple

class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)
    def ab(self: 'Vector2D') -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __mul__(self, scalar: Union[float, int]) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)
    def __div__(self, scalar: Union[float, int]) -> 'Vector2D':
        return Vector2D(self.x / scalar, self.y / scalar)
    def dot (self, other: 'Vector2D') -> float:
        return self.x * other.x + self.y * other.y
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)
    def norm(self) -> 'Vector2D':
        magnitude = self.ab()
        if magnitude == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / magnitude, self.y / magnitude)    

    
        
