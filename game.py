import numpy as np
import math
import pandas as pd
import csv
import random

n = 100
higher_bound = n
lower_bound = 1

def init_states_map():
	indexes = []
	for i in range(1,n+1):
		for j in range(1,n+1):
			if i <= j: #lower bound can't by higher than higher bound
				indexes.append((i,j))
	states_map = pd.DataFrame(0, index=indexes, columns = np.arange(1, n+1))
	return states_map

def init_game():
	global n 
	global higher_bound
	global lower_bound
	higher_bound = n
	magic_number = random.randint(1,n)
	state = (1,n)
	return state, magic_number

def play(dec, magic_number):
	global n
	global higher_bound
	global lower_bound
	#gérer lower bound & higher bound
	##les passer dans initgame et les mettre en global

    #Higher
	if(dec < magic_number):
		lower_bound = dec+1
		state = (dec+1, higher_bound)

	#Lower
	elif(dec > magic_number):
		higher_bound = dec-1
		state = (lower_bound, dec-1)
	else:
		state = 'won'
		higher_bound = n
		lower_bound = 1
		# print('------------WON-------------')
	return state



