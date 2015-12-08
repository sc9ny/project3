#!/usr/bin/python



import random
import sys


def hangman (beep):
	if (beep == 1):
		print """-----
|   
|   
|    
|   
|	
--------"""
	if (beep == 2):
		print """-----
|   |
|   
|    
|   
|	
--------"""
	if (beep == 3):
		print """-----
|   |
|   0
|    
|   
|	
--------"""
	if (beep == 4):
		print """-----
|   |
|   0
|  /  
|  
|	
--------"""
	if (beep == 5):
		print """-----
|   |
|   0
|  /|  
|    
|	
--------"""
	if (beep == 6):
		print """-----
|   |
|   0
|  /|\  
|   
|	
--------"""
	if (beep == 7):
		print """-----
|   |
|   0
|  /|\  
|  /  
|	
--------"""
	if (beep == 8):
		print """-----
|   |
|   0
|  /|\  
|  / \ 
|	
--------"""


	     	
rand = random.randint(0, 47)

f=open('wordbank.txt', 'r')
lines = f.readlines()
#48


key = lines[rand].rstrip()
#print key

print 'There are ' + str(len(key)) + ' characters in this word.'

chance = 8
history = [' ']*8
guess = 0
index = 0 
ans = ['_'] * len(key)
beep = 0
print 'You get ' + str(chance) + ' chances to guess.\nYou can either guess an alphabet or a word.\nCategory is: Mammal.'
print 'Shall we start?'
while (guess < chance):
	ending = ['st', 'nd', 'rd']
	
	if (guess >= 3):
		print ''
		print str(guess+1) + 'th' + ' attempt'
	else:	
		print ''
		print str(guess+1) + ending[guess] + ' attempt'
	
	
	my_guess = raw_input('Enter your guess: ')
	if (my_guess == ''):
		my_guess = raw_input('Please enter something: ')
	history[index] = my_guess
	
	
	index += 1
	print 'Input history: '
	print history
	if (len(my_guess) > 1):
		if (my_guess == key):
			for q in range(0, len(key)):
				print key[q],
			print ''
			print 'You got it!!! Congratulations, you saved hangman'
			exit()
		else: 
			print 'Try again'
			beep += 1
			hangman(beep)
			for m in range(0, len(ans)):
				print ans[m],
			print ''
			guess += 1
			
	else: 
		inCount = key.count(my_guess)
		flag = 0
		for j in range(0, inCount):
			for ind in range(0, len(key)):
				
				if (my_guess == key[ind]):
					if (ans[ind] == '_'):
						ans[ind] = my_guess
														
		guess += 1
		if (inCount > 0):
			hangman(beep)
			print 'Found ' + str(inCount) + ' character(s)!'
		
		if (inCount == 0):
			beep += 1
			hangman(beep)
			print 'Not found'
	
			
		for k in range(0, len(ans)):
			print ans[k],
		print ''
	#checking process
	match = 0
	for check in range(0, len(key)):
		if (ans[check] == key[check]):
			match += 1
		
	#print match
	if (match == len(key)):
		for p in range(0, len(ans)):
			print ans[p],
		print ''
		print 'You got it! Congratulations, you saved hangman'
		exit()
if (match != len(key)):
	hangman(8)
	print 'Hangman has been executed'
	print 'You just killed poor hangman :('
	print 'Answer was: '
	for o in range(0, len(key)):
		print key[o],
	print ''




