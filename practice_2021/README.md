## TODO: 
3. Requirements.txt?


## Solvers

See the [problem statement](problem_statement.pdf).

1. Dummy solver1: assign pizzas in order to teams2, then to teams3 and finally to teams4. 
2. Dummy solver2: assign pizzas in order to teams4, then to teams3 and finally to teams2. 
3. Greedy solver 1: sort pizzas by number of ingredients (heuristic). Assign to [4, 3, 2]. 
4. Greedy solver 2: sort pizzas by number of ingredients (heuristic). Assign to [2, 3, 4]. 
5. Greedy solver 3: sort pizzas by number of ingredients (heuristic). Assign one large from front and 1-3 pizzas from back (last 3 pizzas until finding inflection point (valley) of `waste(current, other)=len(other)-len(set(other)-set(current))`). Assign to [4, 3, 2]. The idea here is to minimize the "waste" of ingredients by evenly spreading the ingredients.
6. Greedy solver 4: same as above but for current pizza_combo, search globally for the other such that `waste(current, other)` is minimum. This will take quite a long runtime (I think). 
7. Random-greedy solver: randomize team assignment (0.33[2], 0.33[3], 0.33[4]). Apply the best greedy solver above. 

## Current high score

See [max.json](max.json). 

459,761,008 points (submitted)

## Contributors

[RoundofThree](https://github.com/RoundofThree) and [xinfan006](https://github.com/xinfan006). 

## Run
```
./runall.sh
```

You need to install pypy3. 