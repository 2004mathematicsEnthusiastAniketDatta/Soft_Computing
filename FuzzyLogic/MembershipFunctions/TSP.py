import random



dist_matrix =[
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
]
cities = list(range(len(dist_matrix)))

def order_decode(order,cities):
    available=cities[:]
    path=[]
    for idx in order:
        path.append(available.pop(idx))
    return path

def path_distance(path):
    return sum(dist_matrix[path[i]][path[(i+1)%len(path)]] for i in range(len(path)))

def random_chromosome(n):
     return [random.randint(0,n-i-1)for i in range(n)]
def crossover(p1,p2):
    point = random.randint(1,len(p1)-2)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2

def mutate(chromosome):
    idx = random.randint(0, len(chromosome)-1)
    max_value = len(chromosome) - idx - 1
    if(max_value > 0):
        chromosome[idx] = random.randint(0, max_value)
    return chromosome
def tournament_selection(pop, k=3):
    selected = random.sample(pop, k)
    selected.sort(key=lambda c: path_distance(order_decode(c, cities)))
    return selected[0]  
def genetic_algorithm(pop_size=50, generations=100,mutation_rate=0.1):
    population = [random_chromosome(len(cities)) for _ in range(pop_size)]
    best_solution = None
    best_distance =float('inf')
    for gen in range(generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1,child2 = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child1)
            if random.random() < mutation_rate:
                mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
        for chrom in population:
            path = order_decode(chrom, cities)
            dist = path_distance(path)
            if dist < best_distance:
                best_distance = dist
                best_solution = path
            if(gen%10==0):
                print(f"Generation {gen}: Best Distance = {best_distance}")
        return best_solution, best_distance
best_path, best_distance = genetic_algorithm()
print("Best path found:", best_path)
print("Total distance:", best_distance)





