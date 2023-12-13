class calculator:

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        dot_product = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {dot_product}")

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        add_vector = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is: {add_vector}")

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        add_vector = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {add_vector}")