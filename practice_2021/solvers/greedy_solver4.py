import argparse
import random
from dataparser import parse, Pizza 

def solve(inp, arg):
    random.seed(args['seed']) 
    ns = parse(inp)
    # input 
    M = ns.m # number of pizzas
    pizzas = ns.pizzas # pizza has fields label and ingredients 
    t2 = ns.t2 # number of teams 
    t3 = ns.t3
    t4 = ns.t4
    # TODO
    