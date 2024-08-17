# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

class Number:
    def __init__(self, value: int):
        self._value = value
        self._value_antecessor: int = None
        self._value_sucessor: int = None

    def antecessor(self):
        antecessor_num = self._value - 1
        self._value_antecessor = antecessor_num
        return self._value_antecessor
    
    def sucessor(self):
        sucessor_num = self._value + 1
        self._value_sucessor = sucessor_num
        return self._value_sucessor
    
    def print_numbers(self):
        print(f'{self._value_antecessor}, {self._value}, {self._value_sucessor}')


num = Number(int(input('Digite um número: ')))
num.sucessor()
num.antecessor()
num.print_numbers()