# Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

num_1: int|float = input('Digite um número: ')
num_2: int|float = input('Digite outro número:')

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
except ValueError:
    print('Estes valores digitados não condizem com os requisitados')