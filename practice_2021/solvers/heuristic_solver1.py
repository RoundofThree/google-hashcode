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
    