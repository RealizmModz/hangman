import sys, random, time
from time import sleep
import colorama
from colorama import Fore
from cfonts import render, say
import os
username = os.environ['REPL_OWNER']

def write(sentence, duration=0.01, color = Fore.WHITE):
	for char in sentence:
	    sleep(duration)
	    sys.stdout.write(color + char)
	    sys.stdout.flush()


output = render('HangMan', colors=['red', 'yellow'], align='center')
print(output)



write("Hello there ", 0.06, Fore.WHITE)
write('@' + username, 0.06, Fore.BLUE)
write(', Welcome to ', 0.06, Fore.WHITE)
write('Hang Man', 0.06, Fore.RED)
print()
print()
write('Please do read the the instructions before playing the game', 0.01, Fore.RED)
print()
print()
write('How many letter word do you want (5 or 8)', 0.01, Fore.WHITE)
print()
num_of_letters = 0
print()
choice = int(input('Answer : '))
# with open('plays.txt', 'r') as plays:
# 	five_plays = int(plays.read().split(',')[0])
# 	eight_plays = int(plays.read().split(',')[1])
# 	total_plays = five_plays+ eight_plays
# 	print(five_plays, eight_plays)
if choice != 5 and choice != 8:
	print()
	write('Please input a valid option, restart the game to play again', 0.01, Fore.RED)
	print()
	exit()
else:
	num_of_letters = choice
print()
if choice == 5:
	write('Looks like we have a beginner here !!!', 0.01, Fore.GREEN)
else:
	write('Guess you directly jump into the difficult ones !!!', 0.01, Fore.GREEN)
print()
print()
tries = num_of_letters + (num_of_letters) + 3
write(f'How many tries do you want in to be[default({tries}) OR Custom]', 0.01, Fore.WHITE)
print()
print()
write('NOTE : Your score will be affected depending on the number of tries you make and choose, more tries lesser the score', 0.01, Fore.RED)
write('.', 0.01, Fore.WHITE)
print()
print()
choice = input('Answer : ')
if choice.lower() == 'custom':
	tries = int(input('Number of tries : '))
	print()
	write('Ok set MAX tries to ' + str(tries), 0.01, Fore.GREEN)
else:
	print()
	write('Ok set tries to default', 0.01, Fore.GREEN)
print()
print()
with open('words.txt', 'r') as words:
	words_list = words.read().split('\n')
	desired_word_list = []
	for word in words_list:
		if len(word) == num_of_letters:
			desired_word_list.append(word)
print()
write('Picking a random word from ', 0.01, Fore.WHITE)
write(str(len(desired_word_list)) + ' ', 0.01, Fore.RED)
write('words', 0.01, Fore.WHITE)
print()
print()
write('Word Picked !!!', 0.01, Fore.WHITE)
print()
print()
word = random.choice(desired_word_list)
word_list_empty = ['_' for i in list(word)]
start = time.time()
for i in range(tries):
	write('Word you have guessed till now ' + ' '.join(word_list_empty), 0.01, Fore.WHITE)
	print()
	print()
	write('Letter guessed till now ', 0.01, Fore.WHITE)
	write(str(len(word_list_empty) - word_list_empty.count('_')), 0.01, Fore.RED)
	write(' of ', 0.01, Fore.WHITE)
	write(str(len(word_list_empty)), 0.01, Fore.RED)
	write('(' + str(((len(word_list_empty) - word_list_empty.count('_')) / len(word_list_empty)) *100) + '%)', 0.01, Fore.GREEN)
	print()
	print()
	guess = input(f'Guess {i+1}, {tries-(i+1)} guesses remaining : ')
	print()
	if len(guess) > 1:
		write('Only a letter can be entered !!!', 0.01, Fore.RED)
		print()
		exit()
	if list(word).count(guess) > 0:
		write(f'Yay, letter ', 0.01, Fore.GREEN)
		write(guess, 0.01, Fore.RED)
		write(f' was found ', 0.01, Fore.GREEN)			
		write(str(list(word).count(guess)), 0.01, Fore.RED)
		write(f' times.', 0.01, Fore.GREEN)
		for l in range(len(list(word))):

			if list(word)[l] == guess.lower():
				word_list_empty[l] = guess.upper()
		if '_' not in word_list_empty:
			print()
			print()
			write('YOU WIN. THE WORD WAS ', 0.2, Fore.GREEN)
			write(word, 0.1, Fore.RED)
			write(' !!!!', 0.1, Fore.GREEN)
			print()
			print()
			end = time.time()
			time_taken = end - start
			score = round(((num_of_letters/ i+1) * 20000)/time_taken)
			write('Your Score is ', 0.1, Fore.GREEN)
			write(str(score), 0.1, Fore.RED)
			write(' points', 0.1, Fore.GREEN)
			print()
			print()
			write('Do you want to view the leaderboard and the place you have secured ???', 0.05, Fore.WHITE)
			print()
			print()
			choice = input('Yes or No : ')
			if choice.lower() == 'yes':
				with open('plays.txt', 'r') as player_file:
					player_f = player_file.read()
					players = player_f.split('\n')
					player_and_score = {}
					for player in players:
						p = player.split(',')[0]
						s = int(player.split(',')[1])
						player_and_score[p] = s

				with open('plays.txt', 'w') as player_file_edit:
					if username in list(player_and_score.keys()):
						
						if player_and_score[username] >= score:
							write('You have got a lesser score than your highest score', 0.01, Fore.WHITE)
							score = player_and_score[username]
	
					player_and_score[username] = score
					player_and_score= sorted(player_and_score.items(), key=lambda x : 100 - x[1])
					player_and_score = dict(player_and_score)
					s = ''
					index = 0
					for key, value in player_and_score.items():
						if index != 0:
							s += '\n' + key + ',' + str(value)
						else:
							s += key + ',' + str(value)
						index += 1
					player_file_edit.truncate(0)
					player_file_edit.write(s)
				with open('plays.txt', 'r') as leaderboard:
					color_pattern = [Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
					print()
					write('LEADERBOARD', 0.01, Fore.WHITE)
					print()
					print()
					players = leaderboard.read().split('\n')
					for p in players:
						player = p.split(',')[0]
						score = int(p.split(',')[1])
						if player == username:
							print(f'Your rank is #{str(players.index(p) + 1)} with a score of {str(score)}p')
							print()
					for p in players:
						player = p.split(',')[0]
						score = int(p.split(',')[1])
						if (players.index(p) + 1) < 4:
							print(color_pattern[players.index(p)] + f'#{str(players.index(p) + 1)} {player} with a score of {str(score)}p')
						else:
							print(Fore.GREEN + f'#{str(players.index(p) + 1)} {player} with a score of {str(score)}p')
			else:
				exit()

						
			break
		print()
		print()
	else:
		write(f'No letter {guess.upper()} found in the word', 0.01, Fore.RED)
		print()
		print()
else:
	write('The Word was ' + word, 0.01, Fore.WHITE)