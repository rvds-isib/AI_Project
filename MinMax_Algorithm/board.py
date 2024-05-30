"""
Création de la table de jeu
"""


class QuoridorBoard:
    def __init__(self, size=9):
        self.size = size
        self.board = []

    def board_creator(self):
        # Création du board
        ligne_pair = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
        ligne_impair = ["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+",
                        "-", "+"]
        for i in range(self.size * 2 + 1):
            if i % 2 == 0:
                self.board.append(ligne_impair.copy())  # copy pour pas avoir de problème avec le 1
            else:
                self.board.append(ligne_pair.copy())

    def print_board(self):
        # Indices horizontaux
        txt = ('   ' + ' '.join(str(i) for i in range(10)))
        print(txt + ' ' + ''.join(str(i) for i in range(10, 19)))
        # Indices verticaux + print du board
        i = 0
        for row in self.board:
            print(f'{i:2} ' + ' '.join(row))
            i += 1
