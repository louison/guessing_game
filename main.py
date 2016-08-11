import numpy as np
import math
import pandas as pd
import csv
import random
import agent
import game


game_number = 20
n = 10
epsilon = 0.3
alpha = 0.5
gamma = 0.9
neg_r = -1

#Inititiating all states for range n
states_map = agent.init_states_map(n)

# Number of games the agent will play
for i in range(game_number):
	#New Game
	state, magic_number = game.init_game()
	# print(states_map)

	#Game is won when agent find the state [magic_number, magic_number]
	while state != 'won':
		
		future_states_map = agent.find_future_states(state, states_map)
		best_choice = agent.find_best_choice(future_states_map, state)
		choice = agent.give_choice(best_choice, epsilon, future_states_map, state)
		new_state = game.play(choice, magic_number)
		agent.update_q_values(states_map, state, choice, new_state, alpha, gamma, neg_r)
		state = new_state
