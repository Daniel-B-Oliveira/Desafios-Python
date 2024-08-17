# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

string = input('Digite alguma coisa: ')

tentativas = dict(alnum = string.isalnum(), alpha = string.isalpha(),
                  ascii = string.isascii(), decimal = string.isdecimal(),
                  digit = string.isdigit(), identifier = string.isidentifier(),
                  lower = string.islower(), numeric = string.isnumeric(),
                  printable = string.isprintable(), space = string.isspace(),
                  title = string.istitle(), upper = string.isupper(),
                )


for key, value in tentativas.items():
    print(f'is{key}? ', value)