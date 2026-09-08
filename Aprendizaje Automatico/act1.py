import random

# Parameters of the genetic algorithm
POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 5
GENERATIONS = 10
MUTATION_RATE = 0.1


# Create one random binary chromosome
def create_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]


# this function creates the initial population of chromosomes
def create_population():
    return [create_chromosome() for _ in range(POPULATION_SIZE)]


# Convert a binary chromosome to a decimal number
def binary_to_decimal(chromosome):
    return int("".join(map(str, chromosome)), 2)


# Calculate the fitness using the objective function
def fitness(chromosome):
    x = binary_to_decimal(chromosome)
    return x ** 2


# Select two parents using tournament selection
def selection(population):
    parents = []

    # Select two parents
    for _ in range(2):
        candidates = random.sample(population, 2)

        # Choose the chromosome with the best fitness
        winner = max(candidates, key=fitness)
        parents.append(winner)

    return parents


# Create two children by crossing the parents
def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)

    # Combine the first part of one parent with the second part of the other
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


# Mutate bits randomly
def mutation(chromosome):

    # Check every bit in the chromosome
    for i in range(len(chromosome)):

        # Mutate the bit according to the mutation rate
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]

    return chromosome


# Create the initial population
population = create_population()


# Repeat the genetic algorithm for several generations
for generation in range(GENERATIONS):

    new_population = []

    # Create new individuals until the population is complete
    while len(new_population) < POPULATION_SIZE:

        # Select two parents
        parent1, parent2 = selection(population)

        # Create two children through crossover
        child1, child2 = crossover(parent1, parent2)

        # Apply mutation to both children
        child1 = mutation(child1)
        child2 = mutation(child2)

        # Add the children to the new population
        new_population.append(child1)
        new_population.append(child2)

    # Keep only the required population size
    population = new_population[:POPULATION_SIZE]

    # Find the best chromosome of the current generation
    best = max(population, key=fitness)

    print(
        "Generation:", generation + 1,
        "Best:", best,
        "x =", binary_to_decimal(best),
        "Fitness =", fitness(best)
    )


# Show the final solution
best = max(population, key=fitness)

print("\nFinal solution:")
print("Chromosome:", best)
print("x:", binary_to_decimal(best))
print("Fitness:", fitness(best))