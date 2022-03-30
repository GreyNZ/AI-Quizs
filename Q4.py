import itertools
import random

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def n_queens_neighbours(state):
    results = []
    for i in range(len(state)-1):
        results.append(tuple(swapPositions(list(state), i, i + 1)))
        for j in range(len(state)-1):
            results.append(tuple(swapPositions(list(state), i, j + 1)))
    results = list(dict.fromkeys(results))
    if state in results:
        results.remove(state)
    return sorted(list(results))


def n_queens_cost(state):
    colisions = 0
    for i in (list(itertools.combinations(state,2))):
        if (abs(i[0] - i[1]) == abs(state.index(i[0]) - state.index(i[1]))):
            colisions += 1
    return colisions

def greedy_descent(initial_state, neighbours, cost):
    state_list = [initial_state]
    flag = True
    last_added = float('inf')
    while flag:
        current_cost = cost(state_list[-1])
        current_state = state_list[-1]
        neighbour_list = neighbours(state_list[-1])
        if len(neighbour_list) == 0:
            break
        lowest_state = min(neighbour_list, key=lambda x:cost(x))
        flag = False
        if round(current_cost,6) > round(cost(lowest_state),6) and lowest_state not in state_list:
            state_list.append(lowest_state)
            flag = True
    return state_list

def greedy_descent_with_random_restart(random_state, neighbours, cost):
    seed = random_state()
    final = True
    while final:
        previous = float('inf')
        soloutions = greedy_descent(seed,neighbours,cost)
        final = cost(soloutions[-1])
        for soloution in soloutions:
            current_cost = cost(soloution)
            if not(current_cost > previous):
                print(soloution)
            if current_cost == 0:
                final = False
            previous = current_cost
        if final:
            print("RESTART")
            seed = random_state()




N = 6
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)



N = 8
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)
