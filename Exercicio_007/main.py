# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

class Student:
    def __init__(self, note_1, note_2):
        self._grade_one = note_1
        self._grade_two = note_2
        self._averege = None

    def averege(self):
        self._averege = (self._grade_one+ self._grade_two)/2
        self._averege= round(self._averege, 2)
        return self._averege
    
    def print_averege(self):
        print(f'A média entre as notas '\
              f'{self._grade_one} e {self._grade_two} '\
              f'foi {self._averege}')
    

if __name__ == '__main__':
    while True:
        grade_1 = input('Digite a primeira nota: ')
        grade_2 = input('Digite a segunda nota: ')

        try:
            grade_1 = float(grade_1)
            grade_2 = float(grade_2)
            break
        except ValueError:
            print('Valores impossiveis, tente novamente.')

    student = Student(grade_1, grade_2)
    student.averege()
    student.print_averege()
    