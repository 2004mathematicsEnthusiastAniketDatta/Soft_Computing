#0/1 Knapsack Problem

# Item | Weight | Value
# 0 | 2 | 3
# 1 | 3 | 4
# 2 | 4 | 5
# 3 | 5 | 8
# 4 | 9 | 10

# Knapsack
Capacity = 15


import random

# Item list (weight, value)
items = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10)]
capacity = 15
num_items = len(items)

# Fitness function
def fitness(chromosome):
    total_weight = total_value = 0
    for i in range(num_items):
        if chromosome[i] == 1:
            total_weight += items[i][0]
            total_value += items[i][1]
    if total_weight > capacity:
        return 0
    return total_value

# Generate a random binary chromosome
def random_chromosome():
    return [random.randint(0, 1) for _ in range(num_items)]

# One-point crossover
def crossover(p1, p2):
    point = random.randint(1, num_items - 1)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

# Mutation: flip one bit
def mutate(chromosome, mutation_rate=0.1):
    for i in range(num_items):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]

# Tournament selection
def tournament_selection(pop, k=3):
    selected = random.sample(pop, k)
    selected.sort(key=lambda c: fitness(c), reverse=True)
    return selected[0]

# Main GA
def genetic_algorithm(pop_size=20, generations=50):
    population = [random_chromosome() for _ in range(pop_size)]
    best_solution = None
    best_fit = 0

    for gen in range(generations):
        new_population = []

        for _ in range(pop_size // 2):
            p1 = tournament_selection(population)
            p2 = tournament_selection(population)
            c1, c2 = crossover(p1[:], p2[:])
            mutate(c1)
            mutate(c2)
            new_population.extend([c1, c2])

        population = new_population

        for chrom in population:
            f = fitness(chrom)
            if f > best_fit:
                best_fit = f
                best_solution = chrom[:]

        if gen % 10 == 0:
            print(f"Generation {gen}: Best Fitness = {best_fit}")

    return best_solution, best_fit

# Run it
solution, value = genetic_algorithm()
print("Best solution:", solution)
print("Total value:", value)

# Show included items
included_items = [i for i in range(num_items) if solution[i] == 1]
total_weight = sum(items[i][0] for i in included_items)
print("Items included:", included_items)
print("Total weight:", total_weight)


