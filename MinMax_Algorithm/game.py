def possible_moves(player):
    moves = []
    # Générer les mouvements verticaux
    if player.row != 1 and game.board[player.row - 1][player.col] != "X":
        if (player.row - 2, player.col) == (player1.row, player1.col):
            moves.append(('up', (player.row - 4, player.col)))
        else:
            moves.append(('up', (player.row - 2, player.col)))
    if player.row != 17 and game.board[player.row + 1][player.col] != "X":
        if (player.row + 2, player.col) == (player1.row, player1.col):
            moves.append(('down', (player.row + 4, player.col)))
        else:
            moves.append(('down', (player.row + 2, player.col)))
    # Générer les mouvements horizontaux
    if player.col != 1 and game.board[player.row][player.col - 1] != "X":
        if (player.row, player.col - 2) == (player1.row, player1.col):
            moves.append(('left', (player.row, player.col - 4)))
        else:
            moves.append(('left', (player.row, player.col - 2)))
    if player.col != 17 and game.board[player.row][player.col + 1] != "X":
        if (player.row, player.col + 2) == (player1.row, player1.col):
            moves.append(('right', (player.row, player.col + 4)))
        else:
            moves.append(('right', (player.row, player.col + 2)))

    # Générer tous les placements de murs possibles
    for row in range(16):
        for col in range(19):
            if game.board[row][col] == "|" or game.board[row][col] == "-":
                if current_player.wall_number > 0:
                    moves.append(("wall", (row, col)))

    return moves


def make_move(move, player, board):
    direction, position = move

    if direction in ['up', 'down', 'left', 'right']:
        new_row, new_col = position
        board[player.row][player.col] = '.'  # Clear current position
        player.row, player.col = new_row, new_col  # Update player's position
        board[player.row][player.col] = player.logo  # Update board with player's new position
    elif direction == 'wall':
        # Handle wall placement
        if player.wall_number > 0:
            row, col = position
            board[row][col] = 'X'
            player.wall_number -= 1

    # Return the updated game state
    return board


def evaluate(board):
    score = 0

    # Distance to goal for player1 -> Le plus loin possible
    distance_to_goal_p1 = 10 - player1.row
    score += distance_to_goal_p1 * 10

    # Distance to goal for player2 -> Le plus proche possible
    distance_to_goal_p2 = (player2.row - 1) // 2
    score -= distance_to_goal_p2 * 10

    if player1.row == 14 and player2.row != 2:
        if board[15][player1.col] == 'X':
            score += 500

    # Check if player2 is blocked by a wall in front and on its side
    if player2.row != 0 and player2.row != 16:
        if (board[player2.row - 2][player2.col] == 'X' and
                (board[player2.row - 2][player2.col - 2] == 'X' or
                 board[player2.row - 2][player2.col + 2] == 'X')):
            # Penalize if player2 is blocked and can't move forward or sideways
            score -= 50
        elif board[player2.row - 2][player2.col] == 'X':
            # Reward if player2 is blocked only in front, encourage moving to the opposite side
            score += 20
        else:
            # Encourage moving backward if not blocked in front
            score += 10

    return score