import argparse
import random
from dataparser import parse, Pizza 

# inp is an input file as a single string
# return your output as a string
def solve(inp, args):
    random.seed(args['seed']) 
    ns = parse(inp)
    # input 
    M = ns.m # number of pizzas
    pizzas = ns.pizzas # pizza has fields label and ingredients 
    t2 = ns.t2 # number of teams 
    t3 = ns.t3
    t4 = ns.t4
    currpizza = 0

    out2 = [] # [int]
    out3 = []
    out4 = []
    # assign to teams 2, then to teams 3, and then to teams 4
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

# Convert List[List[Int]] to List[String]
def serialize(integers) -> str:
    strings = [str(x) for x in integers]
    return ' '.join(strings)

# Unique ingredients that set B adds to A. 
def diff(current, added) -> int:
    return len(added-current)
