from player import Player
from minmax import minimax_with_alpha_beta, check_victory, make_move
from board import QuoridorBoard


def play():
    """
    Cette fonction gère le déroulement principal du jeu de Quoridor, en alternant les tours entre les joueurs,
    en permettant aux joueurs de placer des murs ou de se déplacer, et en vérifiant les conditions de victoire.
    player1 = Humain
    player2 = IA
    :return: None
    """
    # Initialisation du board
    game = QuoridorBoard()
    game.board_creator()

    # Initialisation des Player sur le board
    player1 = Player('1', 1, 9)
    game.board[player1.row][player1.col] = player1.logo
    player2 = Player('2', 17, 9)
    game.board[player2.row][player2.col] = player2.logo

    difficulty_choice = "Avec quelle difficulté voulez-vous jouer ? " \
                        "\n 1 : Débutant " \
                        "\n 2 : Amateur" \
                        "\n 3 : Normal" \
                        "\n 4 : Expert " \
                        "\n "

    depth = int(input(difficulty_choice))
    while depth not in [1, 2, 3, 4]:
        depth = int(input(difficulty_choice))

    game.print_board()
    current_player = player1

    # Boucle Principale
    while True:
        if current_player == player1:
            choice = input(
                "Joueur {}: \nIl vous reste {} murs, voulez-vous placer un mur (w) ou vous déplacer (d) ? "
                .format(current_player.logo, current_player.wall_number))
            while choice not in ["w", "d"]:
                choice = input(
                    "Joueur {}: \nIl vous reste {} murs voulez vous placer un mur (w) ou vous déplacer (d) ? "
                    .format(current_player.logo, current_player.wall_number))

            if current_player.wall_number == 0:
                print("Vous n'avez plus de murs, vous êtes obligé de vous déplacer")
                choice = "d"

            if choice == "d":
                current_player.move(game, current_player)
                game.print_board()

                # Check for victory
                if check_victory(current_player):
                    print("Joueur {} a gagné !".format(current_player.logo))
                    break

            elif choice == "w":
                current_player.place_a_wall(game, current_player)
                game.print_board()

        else:
            # Utilisation de minimax avec alpha beta pour la sélection du meilleur coup
            # print(game.possible_moves(player2))
            # print(game.possible_moves(player1))

            _, best_move = minimax_with_alpha_beta(game.board, depth, float("-inf"), float("inf"), True,
                                                   player1, player2, game)
            # print("Best move:", best_move)
            print("Player 2 has played", best_move)
            make_move(best_move, current_player, game.board)
            game.print_board()
            # Check for victory
            if check_victory(current_player):
                print("Joueur {} a gagné !".format(current_player.logo))
                break

        # Switch entre les player
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
