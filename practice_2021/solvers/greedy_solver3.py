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
    while (pizzas_left>1 and t2>0) or (pizzas_left>2 and t3>0) or (pizzas_left>3 and t4>0):
        while currpizza<M and visited[pizzas[currpizza].label]:
            currpizza += 1
        # ending condition 
        if currpizza == M:
            break 

        current = set(pizzas[currpizza].ingredients)
        visited[pizzas[currpizza].label] = True 
        pizzas_left -= 1
        inflection = M-1
        curr_index = M-1
        lowest_waste = 100000000000000
        # find inflection point (valley)
        while curr_index > currpizza:
            if visited[pizzas[curr_index].label]:
                curr_index -= 1
                continue
            currwaste = waste(current, set(pizzas[curr_index].ingredients))
            if currwaste > lowest_waste:
                break # lowest_waste is the valley
            lowest_waste = currwaste
            inflection = curr_index
            curr_index -= 1
        # invalid 
        if visited[pizzas[inflection].label]:
            break 
        # assign to teams [4, 3, 2]
        if (pizzas_left>2 and t4>0) and (inflection>currpizza+1) and (inflection<M-1) and (visited[pizzas[inflection-1].label] is False) and (visited[pizzas[inflection+1].label] is False):
            out4.append([4, pizzas[currpizza].label, pizzas[inflection].label, pizzas[inflection-1].label, pizzas[inflection+1].label])
            visited[pizzas[inflection].label] = True
            visited[pizzas[inflection+1].label] = True 
            visited[pizzas[inflection-1].label] = True 
            pizzas_left -= 3
            t4 -= 1
        elif (pizzas_left>1 and t3>0) and ((inflection>currpizza+1 and (visited[pizzas[inflection-1].label] is False)) or (inflection<M-1 and (visited[pizzas[inflection+1].label] is False))):
            waste_left = 1000000
            if inflection>currpizza+1 and (visited[pizzas[inflection-1].label] is False):
                waste_left = waste(current | set(pizzas[inflection].ingredients), set(pizzas[inflection-1].ingredients))
            waste_right = 1000000
            if inflection<M-1 and (visited[pizzas[inflection+1].label] is False):
                waste_right = waste(current | set(pizzas[inflection].ingredients), set(pizzas[inflection+1].ingredients))
            # decide which to include: left or right neighbour 
            if waste_left < waste_right:
                out3.append([3, pizzas[currpizza].label, pizzas[inflection].label, pizzas[inflection-1].label])
                visited[pizzas[inflection-1].label] = True  
            else:
                out3.append([3, pizzas[currpizza].label, pizzas[inflection].label, pizzas[inflection+1].label])
                visited[pizzas[inflection+1].label] = True 
            visited[pizzas[inflection].label] = True 
            pizzas_left -= 2
            t3 -= 1
        elif (pizzas_left>0 and t2>0):
            out2.append([2, pizzas[currpizza].label, pizzas[inflection].label])
            visited[pizzas[inflection].label] = True 
            pizzas_left -= 1
            t2 -= 1
    
    print(f"There are {len(out2)} teams2, {len(out3)} teams 3, {len(out4)} teams4.")
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
