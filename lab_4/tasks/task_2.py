"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""


class Vector:
    dim = None  # Wymiar vectora
    list_of_values=[]
    def __init__(self, *args):
        self.vec=args

    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        return Vector.from_points(beg, end).vec
        

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        if len(end) == len(beg):
            points = cls(*end) - cls(*beg)
            return points
        else:
            raise ValueError
        
    @property
    def dim(self):
        return len(self.vec)
    
    def __len__(self):
        elemts = list(i*i for i in self.vec)
        newVector = sum(elemts) ** 0.5
        return int(newVector)

 
    
    def __add__(self, second):
        if self.dim == second.dim:
            elemts = list(i+j for i, j in zip(self.vec, second.vec))
            newVector = Vector(*elemts)
            return newVector
        else:
            raise ValueError
    
    def __sub__(self, second):
        if self.dim == second.dim:
            elemts = list(i-j for i, j in zip(self.vec, second.vec))
            newVector = Vector(*elemts)
            return newVector
        else:
            raise ValueError
            
    def __mul__(self, second):
        if isinstance(second, Vector):
            if self.dim == second.dim:
                elemts = list(i*j for i, j in zip(self.vec, second.vec))
                newVector = sum(elemts)
                return newVector
            else:
                raise ValueError
        else:
            elemts = list(i*second for i in self.vec)
            newVector = Vector(*elemts)
            return newVector
            
    def __eq__(self, second):
        if self.dim == second.dim:
            for i, j in zip(self.vec, second.vec):
                if i != j:
                    return False
            return True        
        


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
