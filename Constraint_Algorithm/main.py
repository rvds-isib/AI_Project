from overwatch import OverwatchTeamBuilder
from map_selector import map_choice


def main():
    """
    Create the best overwatch team possible around your character choice and map choice !!
    """
    team_size = 5
    team_builder = OverwatchTeamBuilder()
    team_builder.define_variables(team_size)

    team_builder.add_role_constraints()  # Contraintes nombre de rôles dans une équipe (3 contraintes)
    # team_builder.add_team_size_constraint(team_size)

    team_builder.win_rate_constraint()  # Contrainte : maximiser le win rate de l'équipe
    team_builder.select_hero()  # Contrainte sélection du héro

    style = map_choice()
    team_builder.add_gameplay_constraint(style)  # Contrainte style de map / gameplay héro

    solver, status = team_builder.solve_model()
    team_builder.status_handling(solver, status)


if __name__ == "__main__":
    while True:
        main()
        x = input("Continuer ? O/N : ").upper()
        if x in ['N', 'NON', 'NO']:
            break
