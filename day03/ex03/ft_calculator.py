class calculator:

    """Creating our own calculator"""
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)
    
    def __truediv__(self, object) -> None:
        try:
            for i in range(len(self.vector)):
                self.vector[i] /= float(object)
            print(self.vector)
        except ZeroDivisionError:
            print("Really??")