"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody area i perimeter we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie
pola (get_area) i obwodu (get_perimeter) figury
na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych lub None (jeżeli przekątne nie są równe).
- Zwiąż ze sobą atrybuty a, b, e i f w klasie Square.
"""
import math

class Figure:

    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def name(cls):
        return cls.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )
class Circle(Figure):   
    
    r=None
    
    def __init__(self, arg):
        self.r=arg
        
    @staticmethod
    def get_area(r):
        return math.pi*r**2
     
    @staticmethod
    def get_perimeter(r):
        return math.pi*r*2
    
    @property
    def area(self):
        return math.pi*self.r**2
        
    @property   
    def perimeter(self):
       return 2*math.pi*self.r

class Rectangle(Figure):
    
    __a=None
    __b=None

    def __init__(self, arg1, arg2):
        self.a=arg1
        self.b=arg2
        self.f_name='Rectangle'
    
    @property
    def a(self):
        return self.__a
    
    @a.setter  
    def a(self,new_value):
        self.__a=new_value
        
    @property
    def b(self):
        return self.__b
    
    @b.setter  
    def b(self,new_value):
        self.__b=new_value
        
    @staticmethod
    def get_area(a,b):
        return a*b
     
    @staticmethod
    def get_perimeter(a,b):
        return 2*a+2*b
        
    @property
    def area(self):
        return self.a*self.b
    
    @property    
    def perimeter(self):
        return 2*self.a+2*self.b


class Diamond(Figure):

    __e=None
    __f=None

    def __init__(self, arg1, arg2):
        self.e=arg1
        self.f=arg2
        self.f_name='Diamond'
    
    @property
    def e(self):
        return self.__e
    
    @e.setter  
    def e(self,new_value):
        self.__e=new_value
        
    @property
    def f(self):
        return self.__f
    
    @f.setter  
    def f(self,new_value):
        self.__f=new_value
        
    @staticmethod
    def get_area(e,f):
        return e*f*0.5
     
    @staticmethod
    def get_perimeter(e,f):
        return 2*(e**2+f**2)**0.5
        
    @property
    def area(self):
        return self.e*self.f*0.5
    
    @property    
    def perimeter(self):
        return 2*(self.e**2+self.f**2)**0.5

    def are_diagonals_equal(self):
        return self.e==self.f
     
    def to_square(self):
        if self.are_diagonals_equal():
            return Square(self.e/2**0.5)
            
class Square(Rectangle, Diamond):   
        
    def __init__(self, arg1):
        self.a=arg1
    
    
    def get_a(self):
        return self.__a
    
    
    def set_a(self,value):
        self.__a=value
        self.__b=value
        self.__e=value*2**0.5
        self.__f=value*2**0.5
    
    a=property(get_a,set_a)
    
    def get_b(self):
        return self.__b
    
    
    def set_b(self,value):
        self.__a=value
        self.__b=value
        self.__e=value*2**0.5
        self.__f=value*2**0.5
    
    b=property(get_b,set_b)
    
    
    def get_e(self):
        return self.__a
    
    
    def set_e(self,value):
        self.__a=value*2**-0.5
        self.__b=value*2**-0.5
        self.__e=value
        self.__f=value
    
    e=property(get_e,set_e)
    
    def get_f(self):
        return self.__f

    def set_f(self, value):
        self.__a=value*2**-0.5
        self.__b=value*2**-0.5
        self.__e=value
        self.__f=value
        
    f=property(get_f,set_f)    


if __name__ == '__main__':
    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'
    
    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'