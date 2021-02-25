import argparse
import random
from dataparser import parse, Pizza 

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
    out2, out3, out4 = [], [], []
    
    visited = [False for i in range(M)]  # visited or not based on pizza label 
    pizzas_left = M 

    for i in range(M):
        p = pizzas[i]
        if visited[p.label]:
            continue
        if pizzas_left < 2:
            break 
        visited[i] = True 
        current = set(p.ingredients)
        ok = False
        while not ok:
            team = random.randint(2, 4)
            if team == 4:
                if t4>0 and pizzas_left > 3:
                    ret = [4, p.label]
                    for k in range(3):
                        next = nextBest(current, i, pizzas, visited)
                        current = current.union(set(pizzas[next].ingredients))
                        visited[pizzas[next].label] = True 
                        ret.append(pizzas[next].label)
                    out4.append(ret)
                    pizzas_left -= 4
                    t4 -= 1
                    ok = True
            elif team == 3:
                if t3 > 0 and pizzas_left > 2:
                    ret = [3, p.label] 
                    for k in range(2):
                        next = nextBest(current, i, pizzas, visited)
                        current = current.union(set(pizzas[next].ingredients))
                        visited[pizzas[next].label] = True 
                        ret.append(pizzas[next].label)
                    out3.append(ret)
                    pizzas_left -= 3
                    t3 -= 1
                    ok = True 
            else:
                if t2 > 0:
                    next = nextBest(current, i, pizzas, visited)
                    current = current.union(set(pizzas[next].ingredients))
                    visited[pizzas[next].label] = True 
                    ret = [2, p.label, pizzas[next].label]
                    out2.append(ret)
                    pizzas_left -= 2
                    t2 -= 1
                    ok = True 
    
    print(f"There are {len(out2)} teams 2, {len(out3)} teams 3, {len(out4)} teams4.")
    out = out2 + out3 + out4 
    out = list(map(serialize, out))
    return '\n'.join([str(len(out))] + out) 
    
   
def serialize(integers) -> str:
    strings = [str(x) for x in integers]
    return ' '.join(strings)

# Unique ingredients that set B adds to A. 
def diff(current, added) -> int:
    return len(added-current)

# return best index in pizzas list 
def nextBest(current, start, pizzas, visited) -> int:
    min_waste = 10000000
    for i in range(start+1, len(pizzas)):
        if visited[pizzas[i].label]:
            continue 
        currwaste = waste(current, set(pizzas[i].ingredients))
        if currwaste < min_waste:
            next = i
            min_waste = currwaste
    return next

def waste(current, added) -> int:
    return len(added) - diff(current, added)
