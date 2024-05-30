"""
Gestion du player Humain
"""


class Player:
    def __init__(self, logo, row, col):
        self.logo = logo
        self.row = row
        self.col = col
        self.wall_number = 8
        # self.position = (row, col)

    def move(self, game, current_player):
        # Choix déplacement
        direction = input(
            "Joueur {}, veuillez choisir une direction (up, down, left, right) : ".format(current_player.logo))
        # Efface ancienne position
        game.board[self.row][self.col] = '.'
        # Check déplacement
        if direction == 'up' and self.row != 0 and game.board[self.row - 1][self.col] != "X":
            if game.board[self.row - 2][self.col] == "2":
                self.row -= 4
            else:
                self.row -= 2
        elif direction == 'down' and self.row != 16 and game.board[self.row + 1][self.col] != "X":
            if game.board[self.row + 2][self.col] == "2":
                self.row += 4
            else:
                self.row += 2
        elif direction == 'left' and self.col != 1 and game.board[self.row][self.col - 1] != "X":
            if game.board[self.row][self.col - 2] == "2":
                self.col -= 4
            else:
                self.col -= 2
        elif direction == 'right' and self.col != 17 and game.board[self.row][self.col + 1] != "X":
            if game.board[self.row][self.col + 2] == "2":
                self.col += 4
            else:
                self.col += 2
        else:
            print("Mauvais choix de direction")
            current_player.move(game, current_player)
        # Mise à jour la position joueur
        game.board[current_player.row][current_player.col] = current_player.logo

    def place_a_wall(self, game, current_player):
        while True:
            try:
                x, y = map(int, input("Position du mur (x y) : ").split())
                if 0 <= x <= 18 and 0 <= y <= 16:
                    break
                else:
                    print("Coordonnées en dehors des limites du plateau. Réessayez.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer deux entiers séparés par un espace.")

        # Code pour placer le mur à la position (x, y)
        print("Mur placé à la position ({}, {})".format(x, y))
        # Check placement libre
        if game.board[y][x] in ["-", "|"]:
            # Placement du mur
            game.board[y][x] = "X"
            self.wall_number -= 1
        else:
            print("Case déjà occupée")
            current_player.place_a_wall(game, current_player)
