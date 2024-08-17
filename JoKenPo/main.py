from game import Jkpop
from game import Question

main_menu = Question("Menu")
main_menu.set_answers = ["Novo jogo"]


while True:
    main_menu.get_answer()

    if main_menu.current_ans == "Novo jogo":
        while True:
            try:
                number = int(input("Numero de jogadas: "))
                if number % 2 != 0:
                    gamet = Jkpop(number)
                    break
            except ValueError:
                pass


            print("\nValor inválido, o número de jogadas deve ser ímpar e maior ou igual à 3\n")

        main_menu.add_answers("Jogar", "Renomear jogadas", "Ver placar")
    
    elif main_menu.current_ans == "Jogar":
        while True:
            play_menu = Question("Opções de jogo")
            play_menu.set_answers = ["Jogar", "Ver regras", "Renomear jogadores","Retornar"]
            play_menu.get_answer()

            if play_menu.current_ans == "Retornar":
                break

            elif play_menu.current_ans == "Ver regras":
                gamet.matchups()

            elif play_menu.current_ans == "Renomear jogadores":
                player_index = int(input("Digite o numero do jogador (1 ou 2): "))
                player_dict = f"Player{player_index}"
                player_name = input(f"{gamet.score[player_dict][0]} será renomeado para: ")
                gamet.new_name(player_index, player_name)

            elif play_menu.current_ans == "Jogar":
                gamet.show_score()
                while True:
                    try:
                        
                        gamet.show_moves()

                        p1 = int(input(f"Digite o movimento de {gamet.score['Player1'][0]}: "))
                        p2 = int(input(f"Digite o movimento de {gamet.score['Player2'][0]}: "))

                        result = gamet.play(p1,p2)

                        print(f"{gamet.score[result][0]} ganhou.")
                        gamet.show_score()

                        back = Question("Deseja sair")
                        back.get_answer()
                        if back.current_ans == "Yes":
                            break

                    except IndexError:
                        pass
    
    elif main_menu.current_ans == "Renomear jogadas":
        while True:
            gamet.show_moves()

            rename_menu = Question("Renomear")
            rename_menu.set_answers = ["Renomear todas as jogadas", "Renomear uma jogada", "Retornar"]

            rename_menu.get_answer()

            if rename_menu.current_ans == "Retornar":
                break

            elif rename_menu.current_ans == "Renomear todas as jogadas":
                new_names = input(f"Digite todos os {len(gamet.moves)} novos nomes separados por espaço: ").split(" ")
                gamet.new_moves = new_names

            elif rename_menu.current_ans == "Renomear uma jogada":
                new_name = input("Digite o novo nome: ")
                new_name_index = int(input("Número do movimento que você deseja mudar: "))

                gamet.rename_move(new_name_index, new_name)

    elif main_menu.current_ans == "Ver placar":
        gamet.show_score()
