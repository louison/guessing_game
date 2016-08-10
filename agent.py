import numpy as np
import math
import pandas as pd
import csv
import random

def init_states_map(n):
	indexes = []
	for i in range(1,n+1):
		for j in range(1,n+1):
			if i <= j: #lower bound can't by higher than higher bound
				indexes.append((i,j))
	states_map = pd.DataFrame(0, index=indexes, columns = np.arange(n))
	return states_map


def find_future_states(state, states_map):
	print(states_map)
	state = (2,6)
	indexes = [index for index in states_map.index.values if 2 <= index[0] <= 6 and 2 <= index[1] <= 6 and index != state]  
	print(indexes)
	future_states = states_map.ix[indexes]
	print(future_states)
	exit()
	return future_states

def find_best_choice(future_states, state):
	# print(future_states)
	# max_q = future_states[state]
	# print(max_q)
	return best_choice


def give_choice(best_choice, epsilon, future_states, state):
	if(np.random.rand(1)[0] < epsilon):
		for i in future_states:
			if(future_states[i][0] == state):
				choice = random.choice(list(future_states[i][1].keys()))
	else:
		choice = best_choice
	return choice

def find_state(states_map, state):
	for i in states_map:
		if(states_map[i][0] == state):
			return i

def find_q_value(states_map, state, choice):
	for i in states_map:
		if(states_map[i][0] == state):
			return states_map[i][1][choice]

def find_best_q_value(state, states_map):
	best_q_value = 0
	for i in states_map:
		if(states_map[i][0] == state):
			for key in states_map[i][1]:
				if(states_map[i][1][key] >= best_q_value):
					best_q_value = states_map[i][1][key]
	return best_q_value



def update_q_values(states_map, state, choice, new_state, alpha, gamma, neg_r):
	index = -1
	for i in states_map:
			if(states_map[i][0] == new_state):
				index = i
	max_q_plus_un = find_best_q_value(new_state, states_map)

	if(new_state != 'won'):
		states_map[index][1][choice] += alpha*(neg_r + gamma*max_q_plus_un - states_map[index][1][choice])
