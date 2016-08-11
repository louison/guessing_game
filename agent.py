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
	indexes = [index for index in states_map.index.values if state[0] <= index[0] <= state[1] and state[0] <= index[1] <= state[1]]  
	future_states = states_map.ix[indexes]
	return future_states

def find_best_choice(future_states, state):
	actions_state = future_states.ix[[state]]
	if(actions_state.values.all() == 0):
		best_choice = random.randint(1,10)
		print('random best_choice : ' + str(best_choice))
	else:
		best_choice = actions_state.idxmax(axis = 1)[0] +1
		print('decided best_choice : ' + str(best_choice))
	return best_choice


def give_choice(best_choice, epsilon, future_states, state):
	if(np.random.rand(1)[0] < epsilon):
		choice = random.randint(1,10)
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
	actions_new_state = states_map.ix[[new_state]]
	max_q_new_state = actions_new_state.idxmax(axis = 1)[0] +1

	if(new_state != 'won'):
		states_map.ix[[state], choice-1] += alpha*(neg_r + gamma*max_q_new_state - states_map.ix[[state], choice-1])
