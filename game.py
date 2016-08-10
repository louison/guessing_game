import numpy as np
import math
import pandas as pd
import csv
import random


higher_bound = 0
lower_bound = 1
n = 10


def init_game():
	global higher_bound
	global lower_bound
	global n 
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
	#

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
		print('------------WON-------------')
	return state



