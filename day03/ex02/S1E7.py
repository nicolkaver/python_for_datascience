from S1E9 import Character

class Baratheon(Character):
    
    default_family_name = "Baratheon"
    default_eyes = "brown"
    default_hairs = "dark"
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):  
        return super().die()

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        return f"of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

class Lannister(Character):
    
    default_family_name = "Lannister"
    default_eyes = "blue"
    default_hairs = "light"
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        return super().die()
    
    @classmethod
    def create_lannister(cls, name, is_alive=True):
        return cls(name)

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"