def processLines(lines) -> str:

    N = int(lines[0])  # Nombre de sprints
    T = int(lines[1])  # Nombre de tâches dans le backlog initial
    
    # Initialisation  backlog avec le nombre de tâches initial
    backlog = T
    
    # Pour chaque sprint, mettre à jour le backlog
    for i in range(2, N + 2):
        V, U = map(int, lines[i].split())  
        backlog -= V  
        backlog += U
    
    if backlog != 0:
        return "KO"
    else:
        return "OK"

# Exemple d'appel
lines = [
    "3",      # Nombre de sprints
    "10",     # Nombre de tâches initiales
    "3 2",    # 3 tâches validées, 2 tâches ajoutées
    "4 -1",   # 4 tâches validées, 1 tâche supprimée
    "3 0"     # 3 tâches validées, aucune modification
]

print(processLines(lines))  
