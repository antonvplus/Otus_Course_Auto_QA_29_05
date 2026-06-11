from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, other):
        if not isinstance(other, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area + other.get_area
