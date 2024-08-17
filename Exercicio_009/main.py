# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

def multiplication(num:int):
    multiplication_table = {}
    for i in range(1, 11):
        multiplication_table[f'{i} X {num}'] = i*num

    return multiplication_table

if __name__ == '__main__':
    while True:
        num = input('Digite um número')
        try:
            num = int(num)
            break
        except ValueError:
            print('Valor impossível')

    tabuada = multiplication(num)

    for key, value in tabuada.items():
        print(f'{key} = {value}')