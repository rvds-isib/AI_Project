from ortools.sat.python import cp_model
from heroes_data import heroes, gameplay, win_rate


class OverwatchTeamBuilder:
    def __init__(self):
        self.model = cp_model.CpModel()
        self.selected = {}
        self.tanks = None
        self.damages = None
        self.supports = None

    def define_variables(self, team_size):
        """
        Crée un dictionnaire pour représenter les héros sélectionnés avec une valeur binaire
        Crée une variable pour chaque rôle représentant le nombre de places disponible pour ce rôle
        """
        self.selected = {hero: self.model.NewBoolVar(hero) for hero in heroes}
        self.tanks = self.model.NewIntVar(1, 1, "tanks")
        self.damages = self.model.NewIntVar(2, 2, "damages")
        self.supports = self.model.NewIntVar(2, 2, "supports")

    def add_role_constraints(self):
        """
        Ajoute 3 contraintes :
        Le nombre de tanks sélectionnés doit être validé (1)
        Le nombre de damages sélectionnés doit être validé (2)
        Le nombre de supports sélectionnés doit être validé (2)
        """
        self.model.Add(sum(self.selected[hero] for hero, role in heroes.items() if role == "tank") == self.tanks)
        self.model.Add(sum(self.selected[hero] for hero, role in heroes.items() if role == "damage") == self.damages)
        self.model.Add(sum(self.selected[hero] for hero, role in heroes.items() if role == "support") == self.supports)

    def add_team_size_constraint(self, team_size):
        """
        Not use → contrainte autovalidée par les contraintes précédentes
        :param team_size:
        :return:
        """
        self.model.Add(sum(self.selected.values()) == team_size)

    def win_rate_constraint(self):
        """
        Ajoute 1 contrainte :
        Objectif maximiser le winrate des héros sélectionnés pour former une équipe
        """
        total_points = sum(win_rate[hero] * self.selected[hero] for hero in win_rate)
        self.model.Maximize(total_points)

    def select_hero(self):
        """
        Ajoute 1 contrainte :
        Selection du héro choisi par l'utilisateur
        """
        chosen_hero = input("Quel héros voulez-vous jouer ? ")
        if chosen_hero in heroes:
            self.model.Add(self.selected[chosen_hero] == 1)
        else:
            print("Ce héros n'est pas disponible.")
            self.select_hero()

    def add_gameplay_constraint(self, style):
        """
        Ajoute 1 contrainte :
        Vérifie que les héros sélectionnés ont l'un des 'styles' de gameplay correspondant au style de la map
        :param style : style de gameplay de la map
        """
        self.model.Add(sum(self.selected[hero] for hero, styles in gameplay.items() if style in styles)
                       == sum(self.selected.values()))

    def solve_model(self):
        """
        Création d'un solver
        :return : le solver ainsi que le status
        """
        solver = cp_model.CpSolver()
        status = solver.Solve(self.model)
        return solver, status

    def status_handling(self, solver, status):
        """
        Gère le traitement du statut de la résolution du modèle.
        :param :
            solver: Le solveur utilisé pour résoudre le modèle.
            status: Le statut de la résolution du modèle.
        """
        if status == cp_model.OPTIMAL:
            team = [hero for hero in heroes if solver.Value(self.selected[hero])]
            moyenne = sum(win_rate[hero] / 5 for hero in team)
            print("Equipe optimale :", team)
            print("Moyenne :", "{:.3f}".format(moyenne))
            print("--------------------------------------------")

        elif status == cp_model.FEASIBLE:
            print("Solution faisable trouvée.")

        elif status == cp_model.INFEASIBLE:
            print("Héro non-recommandé pour cette map")

        else:
            print("Aucune solution trouvée")
