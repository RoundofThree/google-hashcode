import argparse
import json
from collections import *
from pathlib import Path

# next integer 
def ni(itr):
    return int(next(itr))

# next line
# parses the next string of itr as a list of integers
def nl(itr):
    return [int(v) for v in next(itr).split()]

# could have used a namedtuple 
class Pizza:
    def __init__(self, label, ingredients):
        self.ingredients = ingredients
        self.label = label

# parser logic 
def parse(inp):
    # TODO: fill ns
    lines = inp.split('\n')
    M, T2, T3, T4 = map(int, lines[0].split())
    # pizza: {label: int, flavours: [int]}
    # dict: string -> int
    p = []
    curring = 0
    ingredients = dict()
    for num, line in enumerate(lines[1:]):
        curringlist = []
        # build the ingredients list 
        for ing in line.split()[1:]:
            # place to dict or retrive 
            if ing in ingredients:
                ingint = ingredients[ing]
            else:
                ingredients[ing] = curring
                ingint = curring
                curring += 1
            curringlist.append(ingint)
        p.append(Pizza(num, curringlist))
    
    # p contains labeled pizzas, with ingredients as a list of numbers (int comparison is faster than str comparison)
    return argparse.Namespace(m=M, t2=T2, t3=T3, t4=T4, pizzas=p)

class FlexibleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, argparse.Namespace):
            return vars(obj)
        return json.JSONEncoder.default(self, obj)

def parse2json(inp):
    ns = parse(inp)
    return json.dumps(ns, cls=FlexibleEncoder)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('inp', nargs='?')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.inp:
        file_list = [args.inp]
    else:
        file_list = Path('in').glob('*.in')

    for inp in file_list:
        data = parse2json(inp.read_text())
        with inp.with_suffix('.json').open('w') as f:
            f.write(data)
