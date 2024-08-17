# Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

while True:
    nome:str = input('Digite seu nome: ')
    if not nome.isnumeric() and not nome.isalnum():
        print(f'Olá {nome}, seja bem vindo(a)')
        continue
    print('Hum... isso não me parce um nome')