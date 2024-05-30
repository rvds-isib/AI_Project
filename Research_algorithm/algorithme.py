import random
from heuristic_eval import heuristic
from data import world


def bfs(start_node, goal_node):
    """
    Algorithme BFS → Parcours en largeur l'arbre world

    :param start_node : Serveur de départ
    :param goal_node : Serveur d'arrivée

    :return : Le chemin correct entre le serveur de départ et d'arrivée,
              Le temps de transit de ce chemin en ms
              Le nombre d'itérations
    """
    queue = [(start_node, [start_node], 0)]
    visited = set()
    itterations = 0

    while queue:
        itterations += 1
        current_node, path, current_time = queue.pop(0)
        visited.add(current_node)
        # print(path)

        if current_node == goal_node:
            return path, current_time, itterations

        for neighbor, transit_time in world[current_node].items():
            if neighbor not in visited:
                new_path = path + [neighbor]
                total_time = current_time + transit_time
                queue.append((neighbor, new_path, total_time))

    return "Aucun chemin trouvé", 0, itterations


def random_search(start_node, goal_node):
    """
    Random Search → Sélectionne aléatoirement un noeud enfant disponible dans l'arbre
    :return : Le chemin correct entre le serveur de départ et d'arrivée,
              Le temps de transit de ce chemin en ms
              Le nombre d'itérations
    """
    queue = [(start_node, [start_node], 0)]
    visited = set()
    itterations = 0

    while queue:
        itterations += 1
        random_index = random.randint(0, len(queue) - 1)
        current_node, path, current_time = queue.pop(random_index)
        visited.add(current_node)
        # print(path)

        if current_node == goal_node:
            return path, current_time, itterations

        for neighbor, transit_time in world[current_node].items():
            if neighbor not in visited:
                new_path = path + [neighbor]
                total_time = current_time + transit_time
                queue.append((neighbor, new_path, total_time))

    return "Aucun chemin trouvé", 0, itterations


def greedy_search(start, goal):
    """
    Sélectionne l'heuristique la plus faible parmis tous les nœuds enfants disponibles
    :return : Le chemin correct entre le serveur de départ et d'arrivée,
              Le temps de transit de ce chemin en ms
              Le nombre d'itérations
    """
    # La queue contient des tuples de la forme (noeud, chemin, temps de transit, heuristique)
    queue = [(start, [start], 0, heuristic(start, goal))]
    visited = set()
    iterations = 0

    while queue:
        queue.sort(key=lambda x: x[3])
        # print(queue)
        current_node, path, current_time, _ = queue.pop(0)
        iterations += 1

        if current_node == goal:
            return path, current_time, iterations

        # Retirer les boucles infinies
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, transit_time in world[current_node].items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    total_time = current_time + transit_time
                    # Calcul heuristique
                    heuristic_value = heuristic(neighbor, goal)
                    queue.append((neighbor, new_path, total_time, heuristic_value))

    return "Aucun chemin trouvé", 0, iterations


def beam_search(start, end, beam_width):
    """
    Sélectionne "beam" nœuds dont l'heuristique la plus faible parmis tous les nœuds enfants disponibles
    :return : Le chemin correct entre le serveur de départ et d'arrivée,
              Le temps de transit de ce chemin en ms
              Le nombre d'itérations
    """
    # La queue contient des tuples de la forme (noeud, chemin, temps de transit, heuristique)
    queue = [(start, [start], 0, heuristic(start, end))]
    visited = set()
    iterations = 0

    while queue:
        queue.sort(key=lambda x: x[3])
        candidates = queue[:beam_width]
        # print(candidates)
        queue = queue[beam_width:]
        iterations += 1

        for current_node, path, current_time, _ in candidates:
            if current_node == end:
                return path, current_time, iterations

            # Retirer les boucles infinies
            if current_node not in visited:
                visited.add(current_node)
                for neighbor, transit_time in world[current_node].items():
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        total_time = current_time + transit_time
                        # Calcul heuristique
                        heuristic_value = heuristic(neighbor, end)
                        queue.append((neighbor, new_path, total_time, heuristic_value))

    return "Aucun chemin trouvé", 0, iterations


def a_star(start, end):
    """
    Sélectionne la fonction d'évaluation la plus faible parmis tous les nœuds enfants disponibles
    La fonction d'évaluation est égale à la somme du temps de transit et de l'heuristique
    :return : Le chemin correct entre le serveur de départ et d'arrivée,
              Le temps de transit de ce chemin en ms
              Le nombre d'itérations
    """
    queue = [(start, [start], 0, heuristic(start, end))]
    visited = {start: 0}
    iteration = 0

    while queue:
        queue.sort(key=lambda x: x[3])
        # print(queue)
        current_node, path, current_time, _ = queue.pop(0)
        iteration += 1

        if current_node == end:
            return path, current_time, iteration

        for neighbor, transit_time in world[current_node].items():
            new_path = path + [neighbor]
            # Uniform Cost
            total_time = current_time + transit_time
            # Fonction d'évaluation (sous-estimation)
            eval_function = total_time + heuristic(neighbor, end)

            # Branch and Bound and redundant path deletion
            # Vérifier si le voisin n'a pas encore été exploré ou si ce chemin est plus court
            if neighbor not in visited or total_time < visited[neighbor]:
                visited[neighbor] = total_time
                # Supprimer tout chemin plus long menant au même nœud dans la queue
                queue = [node for node in queue if node[0] != neighbor or node[2] > total_time]
                queue.append((neighbor, new_path, total_time, eval_function))

    return "Aucun chemin trouvé", 0, iteration
