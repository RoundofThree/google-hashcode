from dataparser import *

# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer
def score(inp, out):
    # input 
    ns = parse(inp)
    pizzas = ns.pizzas 
    # output 
    deliveries = [line for line in out.split('\n')]
    score = 0

    pizzadict = get_pizza_dict(pizzas)

    for delivery in deliveries[1:]:
        pizza_combo = list(map(int, delivery.split()[1:]))
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
