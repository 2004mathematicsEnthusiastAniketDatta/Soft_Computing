import random  # Import the random module for generating random numbers

# Distance matrix representing distances between cities (5x5 matrix)
dist_matrix =[
    [0, 2, 9, 10, 7],   # Distances from city 0 to all cities
    [2, 0, 6, 4, 3],    # Distances from city 1 to all cities
    [9, 6, 0, 8, 5],    # Distances from city 2 to all cities
    [10, 4, 8, 0, 6],   # Distances from city 3 to all cities
    [7, 3, 5, 6, 0]     # Distances from city 4 to all cities
]
cities = list(range(len(dist_matrix)))  # Create a list of city indices [0, 1, 2, 3, 4]

def order_decode(order, cities):
    """Convert the chromosome order to an actual path by selecting from available cities"""
    available = cities[:]  # Create a copy of the cities list
    path = []  # Initialize an empty path
    for idx in order:  # For each index in the order list
        path.append(available.pop(idx))  # Remove and add the city at position idx from available cities
    return path

def path_distance(path):
    """Calculate the total distance of a path including return to start"""
    return sum(dist_matrix[path[i]][path[(i+1)%len(path)]] for i in range(len(path)))  # Sum distances between consecutive cities

def random_chromosome(n):
    """Generate a random chromosome of length n with valid indices"""
    return [random.randint(0, n-i-1) for i in range(n)]  # Generate valid indices for the order representation

def crossover(p1, p2):
    """Perform single-point crossover between two parent chromosomes"""
    point = random.randint(1, len(p1)-2)  # Choose a random crossover point (avoiding endpoints)
    child1 = p1[:point] + p2[point:]  # Create first child: first part from p1, second part from p2
    child2 = p2[:point] + p1[point:]  # Create second child: first part from p2, second part from p1
    return child1, child2

def mutate(chromosome):
    """Mutate a chromosome by changing a random gene to a valid value"""
    idx = random.randint(0, len(chromosome)-1)  # Select a random position
    max_value = len(chromosome) - idx - 1  # Calculate the maximum valid value for this position
    if(max_value > 0):  # Ensure we can actually mutate
        chromosome[idx] = random.randint(0, max_value)  # Assign a new random valid value
    return chromosome

def tournament_selection(pop, k=3):
    """Select the best chromosome from k random individuals"""
    selected = random.sample(pop, k)  # Select k random individuals from the population
    selected.sort(key=lambda c: path_distance(order_decode(c, cities)))  # Sort by fitness (distance)
    return selected[0]  # Return the best individual (lowest distance)
  
def genetic_algorithm(pop_size=50, generations=100, mutation_rate=0.1):
    """Solve TSP using genetic algorithm"""
    # Initialize population with random chromosomes
    population = [random_chromosome(len(cities)) for _ in range(pop_size)]
    best_solution = None  # Track the best solution found
    best_distance = float('inf')  # Initialize best distance as infinity
    
    for gen in range(generations):  # Loop through generations
        new_population = []  # Initialize next generation's population
        
        for _ in range(pop_size // 2):  # Create pop_size/2 pairs of offspring
            # Select parents using tournament selection
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            
            # Create offspring through crossover
            child1, child2 = crossover(parent1, parent2)
            
            # Apply mutation with some probability
            if random.random() < mutation_rate:
                mutate(child1)
            if random.random() < mutation_rate:
                mutate(child2)
                
            # Add children to new population
            new_population.extend([child1, child2])
            
        population = new_population  # Replace old population with new one
        
        # Evaluate population and update best solution
        for chrom in population:
            path = order_decode(chrom, cities)  # Decode chromosome to path
            dist = path_distance(path)  # Calculate path distance
            if dist < best_distance:  # If better than best so far
                best_distance = dist  # Update best distance
                best_solution = path  # Update best solution
                
        # Print progress every 10 generations
        if(gen % 10 == 0):
            print(f"Generation {gen}: Best Distance = {best_distance}")
            
        return best_solution, best_distance  # Note: this return is inside the loop, which is likely a bug!

# Run the genetic algorithm and get results
best_path, best_distance = genetic_algorithm()
print("Best path found:", best_path)  # Print the best path found
print("Total distance:", best_distance)  # Print the total distance of the best path





