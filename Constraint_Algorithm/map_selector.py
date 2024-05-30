def map_choice():
    """
    Permet à l'utilisateur de choisir sa map
    :return : le gameplay privilégié de la map
    """

    map_gameplay = {
        "Gibraltar": "dive", "Ilios": "dive", "Busan": "dive", "Nepal": "dive",
        "King's Row": "rush", "Dorado": "rush", "Hollywood": "rush", "Junkertown": "rush",
        "Numbani": "rush", "Route 66": "rush", "Eichenwalde": "rush"
    }

    print("Parmis la liste suivante :"
          "\nBlizzard World \nEichenwalde \nHollywood \nKing's Row \nNumbani \nDorado \nJunkertown"
          "\nRialto \nRoute 66 \nIlios \nLijiang Tower \nNepal \nOasis \nBusan \nGibraltar")
    print("------------------------------------------------------------------------------")
    ow_map = input("Sur quelle Map jouez-vous ?")

    if ow_map in map_gameplay:
        style = map_gameplay[ow_map]
    else:
        style = "poke"

    return style
