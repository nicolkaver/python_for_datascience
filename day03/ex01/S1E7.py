from S1E9 import Character

class Baratheon(Character):
    
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        return super().die()

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        return f"of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

class Lannister(Character):
    
    def __init__(self, first_name, is_alive=True, family_name="Lannister", eyes="blue", hairs="light"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        return super().die()
    
    @classmethod
    def create_lannister(cls, name, is_alive=True):
        return cls(name)

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"