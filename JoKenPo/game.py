"""
    Desafio Jan Kentillion Plus One Pon ou JKPOP

    JKPOP é uma generalização do jogo pedra-papel-tesoura e
    do jogo pedra-papel-tesoura-lagarto-Spock (https://pt.wikipedia.org/wiki/Pedra-papel-tesoura-lagarto-Spock)

    Essa é a ideia, ainda falta tazer o projeto
"""

class Jkpop:
    def __init__(self, size:int):
        self.size       = size
        self._moves     = [f"p{i+1}" for i in range(0,size)]
        self.n_of_clahs = int((size - 1) / 2)
        self.score      = {"Player1" : ["Player1" ,0],
                           "Player2" : ["Player2", 0]}

    @property
    def moves(self):
        return self._moves
    
    @moves.setter
    def new_moves(self, new_moves):
        
        if len(new_moves) == self.size:
            self._moves = new_moves
        elif len(new_moves) < self.size:
            for i in range(len(new_moves)):
                self._moves[i] = new_moves[i]
        else:
            raise ValueError("List of names greater than number of movements")
        return self._moves

    def rename_move(self, index:int, new_move:str):
        self.moves[index] = new_move

    def show_moves(self):
        n = 1
        longer_name = len(f"{len(self.moves)}")

        for move in self.moves:
            if len(move) > longer_name:
                longer_name = len(move)

        for move in self.moves:
            print(n,end='')
            for i in range(longer_name - len(str(n)) + 1):
                print(end=' ')
            n +=1
        print()

        for move in self.moves:
            print(move,end='')
            for i in range(longer_name - len(move) + 1):
                print(end=' ')
        print()

    def add_score(self, winner):
        self.score[winner][1] += 1

    def show_score(self):
        print("="*20)
        print(f"{self.score['Player1'][0]}: {self.score['Player1'][1]}")
        print(f"{self.score['Player2'][0]}: {self.score['Player2'][1]}")
        print("="*20)

    def new_name(self, player, name):
        self.score[f"Player{player}"][0] = name

    def play(self, player1, player2):
        if player1 not in range(1,len(self.moves)+1):
            raise IndexError
        elif player2 not in range(1,len(self.moves)+1):
            raise IndexError
        elif player1 == player2:
            return "Draw"
        elif player1 < player2:
            if player2 - player1 <= self.n_of_clahs:
                self.add_score("Player1")
                return "Player1"
            else:
                self.add_score("Player2")
                return "Player2"
        else:
            if player2 - player1 <= self.n_of_clahs / 2:
                self.add_score("Player2")
                return "Player2"
            else:
                self.add_score("Player1")
                return "Player1"
        
    def matchups(self):
        for n_winner in range(0, self.size):

            print(f"\n{self.moves[n_winner]} wins: ", end='')

            n_loser = n_winner + 1

            for i in range(0, self.n_of_clahs):
                if n_loser == self.size: n_loser = 0
                print(self.moves[n_loser], end=' ')
                n_loser += 1
        print()
    
class Question():
    def __init__(self, question) -> None:
        self.question = question
        self._answers = ["Yes", "No"]
        self.current_ans = "Yes"

    @property
    def answers(self):
        return self._answers
    
    @answers.setter
    def set_answers(self, new_answers):
        self._answers = new_answers
        return self._answers
    
    def remove_answer(self, index_answer):
        self.answers.remove(index_answer)

    def remove_answers(self, *index_answers):
        for index_answer in index_answers:
            self.remove_answer(index_answer)

    def add_answer(self, new_answer):
        if new_answer not in self.answers:
            self.answers.append(new_answer)

    def add_answers(self, *new_answers):
        for new_answer in new_answers:
            self.add_answer(new_answer)

    def show_question(self):
        print()
        print(self.question)
        i = 1
        for answer in self.answers:
            print(f"{i}) {answer}")
            i += 1
    
    def get_answer(self):
        self.show_question()
        while True:
            try:
                choice = int(input("\n-> "))
                if choice not in range(1, len(self.answers) + 1):
                    raise IndexError
                self.current_ans = self.answers[choice - 1]
                break
            except ValueError:
                print("Try again")
                pass
            except IndexError:
                print("Try again")
                pass
        

class Menu(Question):
    def __init__(self, question) -> None:
        super().__init__(question)

    
    
    
    




    



        

        

