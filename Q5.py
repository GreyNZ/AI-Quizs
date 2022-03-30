def roulette_wheel_select(population, fitness, r):
    fitness_pool = 0
    for individual in population:
        fitness_pool += fitness(individual)
    remaining_pool = 0
    for individual in population:
        if r * fitness_pool < remaining_pool + fitness(individual):
            return individual
        remaining_pool += fitness(individual)




population = [0, 1, 2]

def fitness(x):
    return x

for r in [0, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))
