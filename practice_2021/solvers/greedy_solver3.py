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
    # output 
    out2 = [] # [int]
    out3 = []
    out4 = []
    # sort the pizzas 
    pizzas.sort(key=lambda x: len(x.ingredients))
    # [Boolean] representing if pizza visited
    visited = [False for i in range(M)]
    pizzas_left = M 
    currpizza = 0
    # main loop, while pizzas_left > 1 && t2 > 0 || pizzas_left > 2 && t3>0 || pizzas_left>3 && t4>0
    while pizzas_left>1 and t2>0 or pizzas_left>2 and t3>0 or pizzas_left>3 and t4>0:
        current = set(pizzas[currpizza].ingredients)
        visited[currpizza] = True 
        pizzas_left -= 1
        inflection = M-1
        lowest_waste = 1000000
        # find inflection point (valley)
        while inflection > currpizza:
            if visited[inflection]:
                inflection -= 1
                continue
            currwaste = waste(current, set(pizzas[inflection].ingredients))
            if currwaste > lowest_waste:
                inflection -= 1
                break # lowest_waste is the valley
            lowest_waste = currwaste
            inflection -= 1
        
        if t4>0 and inflection>currpizza+1 and inflection<M-1 and not visited[inflection-1] and not visited[inflection+1]:
            out4.append([4, pizzas[currpizza].label, pizzas[inflection].label, pizzas[inflection-1].label, pizzas[inflection+1].label])
            pizzas_left -= 3
            t4 -= 1
        elif t3>0 and (inflection>currpizza+1 and not visited[inflection-1] or inflection<M-1 and not visited[inflection+1]):
            waste_left = 1000000
            if inflection>currpizza+1:
                waste_left = waste(current | set(pizzas[inflection].ingredients), set(pizzas[inflection-1].ingredients))
            waste_right = 1000000
            if inflection<M-1:
                waste_right = waste(current | set(pizzas[inflection].ingredients), set(pizzas[inflection+1].ingredients))
            if waste_left < waste_right:
                out3.append([3, pizzas[currpizza].label, pizzas[inflection].label, pizzas[inflection-1].label])
            else:
                out3.append([3, pizzas[currpizza].label, pizzas[inflection].label, pizzas[inflection+1].label])
            pizzas_left -= 2
            t3 -= 1
        else:
            out2.append([2, pizzas[currpizza].label, pizzas[inflection].label])
            pizzas_left -= 1
            t2 -= 1

        while visited[currpizza]:
            currpizza += 1


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

def waste(current, added) -> int:
    return len(added) - diff(current, added)
