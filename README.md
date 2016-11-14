## Overview

This project is an experiment about bringing reinforcement learing and **Q-learning** to a basic guessing game.

**The game :**
A *leader* thinks of a secret number between 1 and 100 inclusive. The *guesser* then makes guesses at the secret number. After each guess, the *leader* tells the *guesser* if their guess was correct, in which case the game ends, too high, or too low.

In the project, a simple computed programm (see *game.py*) is the *leader* and an Q-learning agent is the *guesser* (see *agent.py*).

On a simulation like this, a perfect trained agent would be able to guess the number in **5.8** guess on average. In my experiment, it only succeed to reach **7.2**.


## How to run ?

1. Clone the project : 
```
git clone https://github.com/LouisonGitzinger/guessing_game.git
```
2. Run
```
python main.py
```

## References

http://personal.denison.edu/~kretchmar/pubs/WASP03.pdf

Richard S. Sutton and Andrew G. Barto. *Reinforcement Learning: An Introduction*. The MIT Press, 1998.

