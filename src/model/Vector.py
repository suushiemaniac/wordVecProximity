import numpy as np


class Vector:
    def __init__(self, *components: float):
        self.np_vec = np.array(list(components))

    def scale(self, scalar: int) -> 'Vector':
        return Vector(* self.np_vec * scalar)

    def add(self, other: 'Vector') -> 'Vector':
        return Vector(* self.np_vec + other.np_vec)

    def sub(self, other: 'Vector') -> 'Vector':
        return self.add(other.scale(-1))

    def dot(self, other: 'Vector') -> float:
        return self.np_vec.dot(other.np_vec)

    def norm(self) -> float:
        return np.linalg.norm(self.np_vec)

    def dim(self) -> int:
        return self.np_vec.size

    def in_radius(self, center: 'Vector', radius: float) -> bool:
        return Vector.distance(center, self) <= radius

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.add(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self.sub(other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        elif isinstance(other, int):
            return self.scale(other)

    def __str__(self):
        return self.np_vec.__str__()

    def __iter__(self):
        return self.np_vec.__iter__()

    @staticmethod
    def span(one: 'Vector', two: 'Vector') -> 'Vector':
        return Vector(* two - one)

    @staticmethod
    def distance(one: 'Vector', two: 'Vector') -> float:
        return Vector.span(one, two).norm()
