import numpy as np
import math
import pandas as pd
import csv
import random

def find_future_states(state, states_map):
	future_states = states_map.loc[:, state[0] <= states_map.columns]
	future_states = future_states.loc[:, state[1] >= future_states.columns]
	# indexes = [index for index in states_map.index.values if state[0] <= index[0] <= state[1] and state[0] <= index[1] <= state[1]]  
	# columns = [columns for columns in states_map.columns if state[0] <= columns <= state[1]]
	# future_states = states_map.ix[indexes, columns]
	return future_states

def find_best_choice(state, future_states):
	actions_state = future_states.ix[[state]]
	if(actions_state.values.all() == 0):
		best_choice = random.randint(state[0],state[1])
		# print('random best_choice : ' + str(best_choice))
	else:
		best_choice = actions_state.idxmax(axis = 1)[0]
		# print('decided best_choice : ' + str(best_choice))
	return best_choice


def give_choice(best_choice, epsilon, state):
	if(np.random.rand(1)[0] < epsilon):
		choice = random.randint(state[0],state[1])
	else:
		choice = best_choice
	return choice


def update_q_values(states_map, future_states ,state, choice, new_state, alpha, gamma, neg_r, pos_r):
	if(new_state != 'won'):
		future_new_states = find_future_states(new_state, future_states)
		actions_new_state = future_new_states.ix[[new_state]]
		#columns = [column for column in actions_new_state.columns if new_state[0] <= column <= new_state[1]]
		#max_q_new_state = max(actions_new_state[columns])
		max_q_new_state = actions_new_state.values.max()
		states_map.ix[[state], choice] += alpha*(neg_r + gamma*max_q_new_state - states_map.ix[[state], choice])
