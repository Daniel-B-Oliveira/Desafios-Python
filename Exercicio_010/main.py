# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
from open_currency import open_country
import os

country_currency = []

request = input('Aupdate data ? [1] = True ')

if request == '1':
    country_currency = open_country()

try:
    currecy_name, currency_value = country_currency[4] 
except:
    country_currency = open_country()
    currecy_name, currency_value = country_currency[4]

while True:
    while True:
        question = input(f'Do you want to continue with this currency'\
                        f'\n({currecy_name}) [y] [n]? ').lower()
        
        if question == 'y':
            break
        elif question == 'n':
            for i, currency_information in enumerate(country_currency):
                print(i, currency_information[0])  # currency_name
            print('Select a currency by its index')
            index = input('Index: ')

            try:
                index = int(index)
                currecy_name, currency_value = country_currency[index]
                os.system('cls')
                break
            except ValueError:
                os.system('cls')
                print('Value error')
                continue
            except IndexError:
                os.system('cls')
                print('Index error')
                continue
        else:
            print('This answer not exist')
    os.system('cls')
    while True:
        print(f'Press [-1] to return\ncurrency({currecy_name})')
        value_to_convert = input('enter the value you want to convert: ')

        if value_to_convert == '-1':
            break

        try:
            value_to_convert = float(value_to_convert)
            converted_value = value_to_convert / float(currency_value)
            converted_value = converted_value.__round__(2)
            print(f'{value_to_convert} {currecy_name} = {converted_value} dollars')
        except ValueError:
            print('Value error')
            continue
    os.system('cls')
