from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        self.is_alive = False

class Stark(Character):

    """Docstring for the class."""
    def __init__(self, first_name, is_alive=True):
        """Docstring for the constructor."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Docstring for the method die."""
        return super().die()
