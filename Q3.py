import math

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

def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]



for state in greedy_descent(4, neighbours, cost):
    print(state)
#print("4\n3\n2\n1\n0")

for state in greedy_descent(-6.75, neighbours, cost):
    print(state)
#print('-6.75\n-5.75\n-4.75\n-3.75\n-2.75\n-1.75\n-0.75\n0.25')




def cost(x):
     return -x**2

def neighbours(x):
     return [x - 1, x + 1] if abs(x) < 5 else []

for state in greedy_descent(0, neighbours, cost):
     print(state)
