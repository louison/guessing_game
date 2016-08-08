import numpy as np
import math
import pandas as pd
import csv
import random

#Initiate all states possible from spaces [1-n]
def init_states_map(n):
	states_map = {}
	key = 0
	for i in range(1,n+1):
		for j in range(1,n+1):
			if i <= j: #lower bound can't by higher than higher bound
				key += 1
				states_map[key] = [[i,j], 0]
	return states_map


def find_future_states(state, states_map):
	future_states = {}
	for i in range(1, len(states_map) +1):
		if(states_map[i][0][0] >= state[0] and states_map[i][0][1] <= state[1]):
			future_states[i] = states_map[i]
	return future_states


def find_best_choice(future_states, n):
	best_q_value = 0
	best_state = [1,n]
	for i in future_states:
		if(future_states[i][1] > best_q_value):
			best_q_value = future_states[i][1]
			best_state = future_states[i][0]
	return best_state


def give_choice(best_state, epsilon, future_states):
	if(np.random.rand(1)[0] < epsilon):
		print(future_states)
		choice_index = random.choice(list(future_states.keys()))
		choice = future_states[choice_index][0]
	else:
		choice = best_state
	return choice

def find_state(states_map, state):
	for i in states_map:
		if(states_map[i][0] == state):
			return i

def find_q_value(states_map, state):
	for i in states_map:
		if(states_map[i][0] == state):
			return states_map[i][1]


def update_q_values(states_map, state, new_state, alpha, gamma, pos_r, neg_r):
	states_map_index = find_state(states_map, state)
	new_state_q_value = find_q_value(states_map, new_state)
	old_state_q_value = find_q_value(states_map, state)
	print(state, new_state, old_state_q_value, new_state_q_value)
	if(new_state == 'won'):
		states_map[states_map_index][1] += alpha*(pos_r + gamma*new_state_q_value - old_state_q_value)
	else:
		states_map[states_map_index][1] += alpha*(neg_r + gamma*new_state_q_value - old_state_q_value)








