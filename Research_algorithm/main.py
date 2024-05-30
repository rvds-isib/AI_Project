from algorithme import bfs, random_search, greedy_search, beam_search, a_star
from graph import graph_draw
import tracemalloc
import time


start_node = 'Helsinki'
goal_node = 'Tunis'
total_iterations = 0
total_time = 0

num_trials = 1000  # Pour RANDOM SEARCH
beam_width = 2  # si 1 = Greedy

print("Comparaison des Algorithmes de Recherche")
print("=========================================================")
print(f"Start Node : {start_node} | End Node : {goal_node}")
print("=========================================================")

# BFS
print("BFS : ")
start_time = time.time()
tracemalloc.start()
BFS_path, BFS_total_time, BFS_itterations = bfs(start_node, goal_node)
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time()
print("Chemin trouvé :", ' -> '.join(BFS_path))
print("Temps total de transit :", BFS_total_time, "millisecondes")
print("Nombre d'itérations :", BFS_itterations)
memory_in_kilobytes = memory[1] / 1024
print("Espace maximal utilisé par la fonction :", memory_in_kilobytes, "Ko")
print("Temps écoulé :", end_time - start_time, "secondes")
print("=========================================================")

# RANDOM SEARCH
print("Random Search :  ")
start_time = time.time()
tracemalloc.start()
RS_path, RS_total_time, RS_iterations = random_search(start_node, goal_node)
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time()
print("Exemple d'un chemin trouvé :", ' -> '.join(RS_path))
print("Temps total de transit :", RS_total_time, "millisecondes")
print("Nombre d'itérations :", RS_iterations)
memory_in_kilobytes = memory[1] / 1024
print("Espace maximal utilisé par la fonction :", memory_in_kilobytes, "Ko")
print("Temps écoulé :", end_time - start_time, "secondes")
print(" ")

for _ in range(num_trials):
    _, rand_time, iterations = random_search(start_node, goal_node)
    total_time += rand_time
    total_iterations += iterations

average_time = total_time / num_trials
average_iterations = total_iterations / num_trials
print("Temps total de transit moyen sur", num_trials, "essais:", average_time, "millisecondes ")
print("Nombre moyen d'itérations sur", num_trials, "essais:", average_iterations)
print("=========================================================")

# Greedy Search
print("Greedy Search :  ")
start_time = time.time()
tracemalloc.start()
path, total_time, itterations = greedy_search(start_node, goal_node)
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time()
if path:
    print("Chemin trouvé :", ' -> '.join(path))
    print("Temps total de transit:", total_time, "millisecondes")
    print("Nombre d'itérations:", itterations)
    memory_in_kilobytes = memory[1] / 1024
    print("Espace maximal utilisé par la fonction :", memory_in_kilobytes, "Ko")
    print("Temps écoulé :", end_time - start_time, "secondes")
else:
    print("Aucun chemin trouvé.")
print("=========================================================")

# Beam Search
print("Beam Search avec un beam = ", beam_width, ":  ")
start_time = time.time()
tracemalloc.start()
result = beam_search(start_node, goal_node, beam_width)
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time()
if result:
    path, total_time, itterations = result
    print("Chemin trouvé :", ' -> '.join(path))
    print("Temps total de transit:", total_time, "millisecondes")
    print("Nombre d'itérations: ", itterations)
    memory_in_kilobytes = memory[1] / 1024
    print("Espace maximal utilisé par la fonction :", memory_in_kilobytes, "Ko")
    print("Temps écoulé :", end_time - start_time, "secondes")
else:
    print(f"Aucun chemin trouvé de {start_node} à {goal_node}.")
print("=========================================================")

# ASTAR
print("ASTAR :  ")
start_time = time.time()
tracemalloc.start()
result = a_star(start_node, goal_node)
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time()
if result:
    path, total_time, iterations = result
    print("Chemin trouvé :", ' -> '.join(path))
    print("Temps total de transit:", total_time, "millisecondes")
    print("Nombre d'itérations:", iterations)
    memory_in_kilobytes = memory[1] / 1024
    print("Espace maximal utilisé par la fonction :", memory_in_kilobytes, "Ko")
    print("Temps écoulé :", end_time - start_time, "secondes")
else:
    print(f"Aucun chemin trouvé de {start_node} à {goal_node}.")
print("=========================================================")

graph_draw()
