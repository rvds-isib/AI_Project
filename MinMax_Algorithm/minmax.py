def check_victory(player):
    """
    Check victoire d'un player
    :return: Booléen
    """

    if player.logo == '1':
        return player.row == 17  # Joueur '1' atteint la dernière ligne return True
    elif player.logo == '2':
        return player.row == 1  # Joueur '2' atteint la première ligne


def possible_moves(player, game, other_player):
    """
    Génère tous les mouvements possibles pour un joueur donné dans un état de jeu donné.

    :param player: L'objet représentant le joueur pour lequel les mouvements sont générés.
    :param game: L'objet représentant l'état actuel du jeu, contenant le plateau de jeu.
    :param other_player : L'objet représentant l'autre joueur (adversaire).
    :return: Une liste de mouvements possibles.
    """
    moves = []
    # Générer les mouvements verticaux
    if player.row != 1 and game.board[player.row - 1][player.col] != "X":
        if (player.row - 2, player.col) == (other_player.row, other_player.col):
            moves.append(('up', (player.row - 4, player.col)))
        else:
            moves.append(('up', (player.row - 2, player.col)))
    if player.row != 17 and game.board[player.row + 1][player.col] != "X":
        if (player.row + 2, player.col) == (other_player.row, other_player.col) and other_player.row != 17:
            moves.append(('down', (player.row + 4, player.col)))
        else:
            moves.append(('down', (player.row + 2, player.col)))
    # Générer les mouvements horizontaux
    if player.col != 1 and game.board[player.row][player.col - 1] != "X":
        if (player.row, player.col - 2) == (other_player.row, other_player.col):
            moves.append(('left', (player.row, player.col - 4)))
        else:
            moves.append(('left', (player.row, player.col - 2)))
    if player.col != 17 and game.board[player.row][player.col + 1] != "X":
        if (player.row, player.col + 2) == (other_player.row, other_player.col):
            moves.append(('right', (player.row, player.col + 4)))
        else:
            moves.append(('right', (player.row, player.col + 2)))

    # Générer tous les placements de murs possibles
    for row in range(19):
        for col in range(19):
            if game.board[row][col] == "|" or game.board[row][col] == "-":
                if player.wall_number > 0:
                    moves.append(("wall", (row, col)))

    return moves


def make_move(move, player, board):
    """
    Effectue un mouvement pour un joueur sur le plateau de jeu.

    :param move : Un tuple représentant l'action.
    :param player : L'objet représentant le joueur qui effectue le mouvement.
    :param board : La grille de jeu actuelle.
    :return : La grille de jeu mise à jour après le mouvement.
    """
    direction, position = move
    # Gestion des déplacements
    if direction in ['up', 'down', 'left', 'right']:
        new_row, new_col = position
        board[player.row][player.col] = ' '  # Efface la position actuelle
        player.row, player.col = new_row, new_col  # Mise à jour de la position
        board[player.row][player.col] = player.logo  # Mise à jour du board
    elif direction == 'wall':
        # Gestion des murs
        if player.wall_number > 0:
            row, col = position
            board[row][col] = 'X'
            player.wall_number -= 1

    return board


def evaluate(board, player1, player2):
    """
    Évalue l'état actuel du jeu pour déterminer une évaluation de la position des joueurs.

    :param board : La grille actuelle du jeu.
    :param player1 : Le premier joueur (humain).
    :param player2: Le second joueur (IA).
    :return: Un score numérique représentant l'évaluation de l'état actuel du jeu.
    """
    score = 0

    # Le garder le plus loin (grand) possible
    distance_to_goal_p1 = 10 - player1.row
    score += distance_to_goal_p1 * 100

    # Le plus proche (petit) possible
    distance_to_goal_p2 = (player2.row - 7)
    score -= distance_to_goal_p2 * 100

    # Dernière chance
    if player1.row == 15 and player2.row != 3:
        if board[16][player1.col] == 'X':
            score += 50000

    if player2.col == 1 or player2.col == 17:
        if board[player2.row - 1][player2.col] == 'X':
            score -= 75

    if player2.col == 3 or player2.col == 15:
        if board[player2.row - 1][player2.col] == 'X':
            score -= 55

    if player2.col == 5 or player2.col == 13:
        if board[player2.row - 1][player2.col] == 'X':
            score -= 35

    if player2.col == 7 or player2.col == 11:
        if board[player2.row - 1][player2.col] == 'X':
            score -= 15

    if player2.col == 9 or player2.col == 11:
        if board[player2.row - 1][player2.col] == 'X':
            score -= 5

    if (board[player2.row - 1][player2.col] == 'X' and
            (board[player2.row][player2.col - 1] == 'X' and
             board[player2.row][player2.col + 1] == 'X')):
        score -= 100

    if (board[player2.row - 1][player2.col] == 'X' and
            (board[player2.row][player2.col - 1] == 'X' or
             board[player2.row][player2.col + 1] == 'X')):
        score -= 50

    if player1.col == 1 or player1.col == 17:
        if board[player1.row - 1][player1.col] == 'X':
            score += 75

    if player1.col == 3 or player1.col == 15:
        if board[player1.row - 1][player1.col] == 'X':
            score += 55

    if player1.col == 5 or player1.col == 13:
        if board[player1.row - 1][player1.col] == 'X':
            score += 35

    if player1.col == 7 or player1.col == 11:
        if board[player1.row - 1][player1.col] == 'X':
            score += 15

    if player1.col == 9 or player1.col == 11:
        if board[player1.row - 1][player1.col] == 'X':
            score += 5

    if (board[player1.row - 1][player1.col] == 'X' and
            (board[player1.row][player1.col - 1] == 'X' and
             board[player1.row][player1.col + 1] == 'X')):
        score += 100

    if (board[player1.row - 1][player1.col] == 'X' and
            (board[player1.row][player1.col - 1] == 'X' or
             board[player1.row][player1.col + 1] == 'X')):
        score += 50

    if (board[player1.row - 1][player1.col] == 'X' and
            board[player1.row + 1][player1.col] == 'X' and
            board[player1.row][player1.col - 1] == 'X' and
            board[player1.row][player1.col + 1] == 'X'):
        score -= 1000000

    if (board[player2.row - 1][player2.col] == 'X' and
            board[player2.row + 1][player2.col] == 'X' and
            board[player2.row][player2.col - 1] == 'X' and
            board[player2.row][player2.col + 1] == 'X'):
        score -= 1000000

    return score


def undo_last_test_p2(move, board, current_row, current_col, player2, game):
    """
    Bug de position dernier mouvement de player2
    """
    wall_row, wall_col = move[1]
    if move[0] != "wall":
        board[move[1][0]][move[1][1]] = ' '
        player2.row, player2.col = current_row, current_col
        game.board[player2.row][player2.col] = player2.logo
    if move[0] == "wall" and wall_row % 2 == 0:
        board[move[1][0]][move[1][1]] = '-'
        player2.wall_number += 1
    elif move[0] == "wall" and wall_row % 2 != 0:
        board[move[1][0]][move[1][1]] = '|'
        player2.wall_number += 1


def undo_last_test_p1(move, board, current_row, current_col, player1, game):
    """
    Bug de position dernier mouvement de player1
    """
    if move[0] != "wall":
        board[move[1][0]][move[1][1]] = ' '
        player1.row, player1.col = current_row, current_col
        game.board[player1.row][player1.col] = player1.logo
    elif move[0] == "wall" and move[1][0] % 2 == 0:
        board[move[1][0]][move[1][1]] = '-'
        player1.wall_number += 1
    else:
        board[move[1][0]][move[1][1]] = '|'
        player1.wall_number += 1


def minimax_with_alpha_beta(board, depth, alpha, beta, maximizing_player, player1, player2, game):
    """
    Implémente l'algorithme Minimax avec élagage alpha-bêta pour déterminer le meilleur mouvement.

    :param board : L'état actuel du plateau de jeu.
    :param depth : La profondeur actuelle de la recherche dans l'arbre de jeu.
    :param alpha : La valeur alpha pour l'élagage alpha-bêta.
    :param beta : La valeur bêta pour l'élagage alpha-bêta.
    :param maximizing_player : Booléen indiquant si le joueur actuel est le joueur maximisant.
    :param player1: L'objet représentant le premier joueur.
    :param player2: L'objet représentant le second joueur.
    :param game: L'objet représentant le jeu.
    :return : Un tuple contenant l'évaluation de la position et le meilleur mouvement trouvé.
    """
    if depth == 0 or check_victory(player1) or check_victory(player2):
        return evaluate(board, player1, player2), None

    if maximizing_player:
        max_eval = float("-inf")
        best_move = None
        current_row, current_col = player2.row, player2.col
        for move in possible_moves(player2, game, player1):
            # print("Considering P2 move:", move)
            new_board = make_move(move, player2, board)
            # for row in new_board:
            # print(' '.join(row))
            new_eval, _ = minimax_with_alpha_beta(new_board, depth - 1, alpha, beta, False, player1, player2, game)
            # print("Max Move:", move, "Eval:", eval)
            max_eval = max(max_eval, new_eval)
            if max_eval > alpha:
                alpha = max_eval
                best_move = move
            if beta <= alpha:
                undo_last_test_p2(move, board, current_row, current_col, player2, game)
                break
            undo_last_test_p2(move, board, current_row, current_col, player2, game)
        # print("Max eval: ", max_eval, "best_move :", best_move)
        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None
        current_row, current_col = player1.row, player1.col
        for move in possible_moves(player1, game, player2):
            # print("Considering P1 move:", move)
            new_board = make_move(move, player1, board)
            # for row in new_board:
            #    print(' '.join(row))
            new_eval, _ = minimax_with_alpha_beta(new_board, depth - 1, alpha, beta, True, player1, player2,
                                                  game)
            # print("Min Move:", move, "Eval:", eval)
            min_eval = min(min_eval, new_eval)
            if min_eval < beta:
                beta = min_eval
                best_move = move
            if beta <= alpha:
                undo_last_test_p1(move, board, current_row, current_col, player1, game)
                break
            undo_last_test_p1(move, board, current_row, current_col, player1, game)
        # print("Min eval: ", min_eval, ", best_move :", best_move)
        return min_eval, best_move
