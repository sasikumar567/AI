import itertools

def tsp_brute_force(graph):
    num_cities = len(graph)
    all_cities = set(range(num_cities))
    min_cost = float('inf')
    best_path = None

    for path in itertools.permutations(range(1, num_cities)):
        current_cost = 0
        current_path = [0] + list(path) + [0]

        for i in range(num_cities - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return min_cost, best_path

# Example graph with distances between cities
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp_brute_force(graph)
print("Minimum Cost:", cost)
print("Optimal Path:", path)
