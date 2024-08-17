# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.


class Value:
    def __init__(self, value:float):
        self.value_meters = value
        self.value_centimeters = value * 10**2
        self.value_millimeters = value * 10**3
    
    def print_value(self):
        print(f'Value in meters = {self.value_meters} m\n'
              f'Value in centimeter = {self.value_centimeters} cm\n'
              f'Value in millimeters = {self.value_millimeters} mm')
        

if __name__ == '__main__':
    while True:
        num = input('Digite um número: ')

        try:
            num = float(num)
            break
        except ValueError:
            print('Valor impossível')

    num = Value(num)
    num.print_value()