from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    def add_area(self, other):
        if not isinstance(other, Figure):
            raise ValueError("Should be a Figure")
        return self.area + other.area
