import argparse
import random
from dataparser import parse, Pizza 

# inp is an input file as a single string
# return your output as a string
def solve(inp, args):
    # TODO: Solve the problem
    random.seed(args['seed'])
    ns = parse(inp)
    # ns.m, t2, t3, t4, pizzas
    # [[2, p, p], [2, p, p]]
    M = ns.m
    pizzas = ns.pizzas
    t2 = ns.t2
    t3 = ns.t3
    t4 = ns.t4
    currpizza = 0

    out2 = [] # [int]
    out3 = []
    out4 = []
    # very very dumb solver 
    while currpizza < M-1 and t2 > 0:
        out2.append([2, pizzas[currpizza].label, pizzas[currpizza+1].label])
        currpizza += 2
        t2 -= 1
    while currpizza < M-2 and t3 > 0:
        out3.append([3, pizzas[currpizza].label, pizzas[currpizza+1].label, pizzas[currpizza+2].label])
        currpizza += 3
        t3 -= 1
    while currpizza < M-3 and t4 > 0:
        out4.append([4, pizzas[currpizza].label, pizzas[currpizza+1].label, pizzas[currpizza+2].label, pizzas[currpizza+3].label])
        currpizza += 4
        t4 -= 1

    out = out2 + out3 + out4 
    out = list(map(serialize, out))
    return '\n'.join([str(len(out))] + out)

def serialize(integers) -> str:
    strings = [str(x) for x in integers]
    return ' '.join(strings)

# Order matters. b will be sorted according to its score in the queue of a. 
def diff(a: Pizza, b: Pizza) -> int:
    ingsA = a.ingredients
    ingsB = b.ingredients
    return len(set(ingsB) - set(ingsA))  # order matters 
