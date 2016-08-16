import numpy as np
import math
import pandas as pd
import csv
import random

def find_future_states(state, states_map):
	indexes = [index for index in states_map.index.values if state[0] <= index[0] <= state[1] and state[0] <= index[1] <= state[1]]  
	columns = [columns for columns in states_map.columns if state[0] <= columns <= state[1]]
	# future_states = states_map.ix[indexes, columns]
	return indexes, columns

def find_best_choice(state, states_map, columns):
	actions_state = states_map.ix[[state]]
	if(actions_state.values.all() == 0):
		best_choice = random.randint(state[0],state[1])
		# print('random best_choice : ' + str(best_choice))
	else:
		best_choice = actions_state[columns].idxmax(axis = 1)[0]
		# print('decided best_choice : ' + str(best_choice))
	return best_choice


def give_choice(best_choice, epsilon, state):
	if(np.random.rand(1)[0] < epsilon):
		choice = random.randint(state[0],state[1])
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



def update_q_values(states_map, state, choice, new_state, alpha, gamma, neg_r, pos_r):
	if(new_state != 'won'):
		actions_new_state = states_map.ix[[new_state]]
		# test = actions_new_state.values[actions_new_state.columns.all() >= new_state[0] and actions_new_state.columns <= new_state[1]]
		# print(test)
		columns = [column for column in actions_new_state.columns if new_state[0] <= column <= new_state[1]]
		max_q_new_state = max(actions_new_state[columns])
		states_map.ix[[state], choice] += alpha*(neg_r + gamma*max_q_new_state - states_map.ix[[state], choice])
	else:
		states_map.ix[[state], choice] += alpha*(pos_r + gamma*0 - states_map.ix[[state], choice])
