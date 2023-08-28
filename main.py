from abc import ABC, abstractmethod
from math import pi


class FormaGeometrica(ABC):
    qtd_figura = 0
    l_figura = list()

    @classmethod
    def get_qtd_figura(cls):  # método de classe, não de instância
        return cls.qtd_figura

    @classmethod
    def mostra_figura(cls):
        print('Veículos: ')
        for Quadrado in cls.l_figura:
            print(f"{Quadrado.area()}")

    def __init__(self):
        FormaGeometrica.qtd_figura += 1
        FormaGeometrica.l_figura.append(self)

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetro(self):
        ...

    @staticmethod
    def mensagem():
        print("Há apenas quadrados e círculos!")

    def mensagem2(self):
        print(f"Você chamou {self}")
        print(f"Você chamou {self.__class__}")
        print(f"Você chamou {self.__class__.__name__}")


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, novo_lado):
        if type(novo_lado) == int:
            self.lado = novo_lado
            print("Lado atualizado!")
        else:
            print("Lado tem que ser int")

    def area(self):
        return f"Área: {self.lado*self.lado}"

    def perimetro(self):
        return f"Perímetro: {self.lado*4}"


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def get_raio(self):
        return self.raio

    def set_raio(self, novo_raio):
        if type(novo_raio) == int or type(novo_raio) == float:
            self.raio = novo_raio
            print("Raio atualizado!")
        else:
            print("Erro! Raio tem que ser int ou float")

    def area(self):
        return f"Área: {pi*self.raio*self.raio:.2f}"

    def perimetro(self):
        return f"Perímetro: {2*pi*self.raio:.2f}"


if __name__ == "__main__":
    # obj_forma = FormaGeometrica()  #erro
    # Não pode criar um objeto se não colocar o método
    q1 = Quadrado(4)
    c1 = Circulo(5)
    print(q1.area())
    print(q1.perimetro())
    q1.set_lado(5)
    print(q1.area())
    print(q1.perimetro())
    q1.mensagem()
    q1.mensagem2()

    print(c1.area())
    print(c1.perimetro())
    c1.set_raio(4)
    print(c1.area())
    print(c1.perimetro())
    c1.mensagem()
    c1.mensagem2()
    print(q1.qtd_figura)

    print(q1.l_figura)
    q1.mostra_figura()
