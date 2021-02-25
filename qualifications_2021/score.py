from dataparser import *

# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer
def score(inp, out):
    # input 
    ns = parse(inp)
    M = ns.m
    pizzas = ns.pizzas 
    # output 
    deliveries = [line for line in out.split('\n')]
    score = 0

    pizzadict = get_pizza_dict(pizzas)
    visited = [False for i in range(M)]

    for delivery in deliveries[1:]:
        pizza_combo = list(map(int, delivery.split()[1:]))
        for pizza in pizza_combo:
            if visited[pizza]:
                print(f"Error, {pizza} already delivered.")
                return 0
            visited[pizza] = True
        score += pow(get_unique_len(pizza_combo, pizzadict), 2)
    
    return score

def get_unique_len(pizzas, pizzadict):
    ingredients = []
    for pizza in pizzas:
        ingredients += pizzadict[pizza].ingredients 
    return len(set(ingredients))

# return dict of label -> pizza
def get_pizza_dict(pizzas):
    ret = dict()
    for pizza in pizzas:
        ret[pizza.label] = pizza
    return ret 
