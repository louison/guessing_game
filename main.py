import numpy as np
import math
import pandas as pd
import csv
import random
import agent
import game
import stats
import time
import sys


game_number = 10000
epsilon = 0.1
alpha = 0.5
gamma = 0.9
neg_r = -1
pos_r = 5
game_counter = 0
total_elapsed_time = 0
total_number_guess = 0


#Inititiating all states for range n
states_map = game.init_states_map()

# Number of games the agent will play
for i in range(game_number):
	guesses = 0
	#New Game
	state, magic_number = game.init_game()
	# print(states_map)
	
	#Game is won when agent find the state [magic_number, magic_number]
	while state != 'won':
		guesses = guesses + 1
		future_states = agent.find_future_states(state, states_map)
		best_choice = agent.find_best_choice(state, future_states)
		choice = agent.give_choice(best_choice, epsilon, state)
		new_state = game.play(choice, magic_number)
		agent.update_q_values(states_map, future_states, state, choice, new_state, alpha, gamma, neg_r, pos_r)
		state = new_state
	total_number_guess = total_number_guess + guesses
	game_counter = game_counter + 1
	print(round(total_number_guess/game_counter, 2))
	print(game_number - game_counter)

print (states_map)
states_map.to_csv("states_map.csv")