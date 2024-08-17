# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

class Number:
    def __init__(self, value: float) -> None:
        self.value = value
        self._twice: float = None
        self._triple: float = None 
        self._square_root: float = None
    
    def twice(self):
        self._twice = self.value * 2
        return self._twice
    
    def triple(self):
        self._triple = self.value * 3
        return self._triple

    def square_root(self):
        self._square_root = self.value ** (1/2)
        return round(self._square_root, 3)

if __name__ == '__main__':

    while True:
        num = input('Digite um número: ')
        try:
            num = float(num)
            break
        except ValueError:
            print('Value Error')
            pass
        
    num = Number(num)
    print('twice: ', num.twice(),
          'triple: ', num.triple(),
          'square_root: ', num.square_root())
    