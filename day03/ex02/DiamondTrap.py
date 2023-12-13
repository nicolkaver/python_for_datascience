from S1E7 import Lannister, Baratheon

class King(Baratheon, Lannister):

    """This is the King!"""
    def __init__(self, first_name, is_alive=True):
        # Baratheon.__init__(self,first_name, is_alive)
        # Lannister.__init__(self, first_name, is_alive)
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        return f"of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

