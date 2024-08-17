# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

class AreaPintura:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self._rendimento = 2
        self._area = largura * altura
        self._tinata_necessaria = self._area / self._rendimento

    @property
    def rendimento(self):
        return self._rendimento
    
    @rendimento.setter
    def alterar_rendimento(self, rendimento):
        self._rendimento = rendimento
        return self._rendimento
    
    def mostrar_informacoes(self):
        print(f'Largura: {self.largura}, Altura: {self.altura}\n'
              f'Rendimento: {self.rendimento},' \
            f'Tinta Necessaria: {self._tinata_necessaria}')

parede = AreaPintura(32, 22)
# parede.alterar_rendimento = 12
parede.mostrar_informacoes()

