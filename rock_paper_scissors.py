#!/usr/bin/env python2
#de juiste versie van het systeem ophalen. hiermee kan het gedraaid worden in de terminal


#Rock, Paper, Scissors: The Video Game

#modules importeren 'random' om te kijken welke zet de computer zal doen maakt een getal tussen 1 en 3(regel28)
#time is een counter om script te vertragen of dateTime kan er ook mee ingeladen worden. 

import random
import time

#variabelen aanmaken voor rock paper en scissors. zodat gebruiker nummers invullen ipv woorden
rock = 1
paper = 2
scissors = 3

#hier zetten we de tekstuele weergave van de variabelen zodat om het de gebruiker makkelijker te laten lezen.
names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
# de regels worden hier geplaatst
rules = { rock: scissors, paper: rock, scissors: paper }

#hier worden de score van iedere speler bijgehouden
player_score = 0
computer_score = 0

#starten het spel met een welkomstekst. dit blijft herhalen dankzij de while statement
#while stopt wanneer gebruiker het spel wilt beeindigen en voert dan de score functie uit.
def start():
	print "Let's play a game of Rock, Paper, Scissors."
	while game():
		pass
	scores()

# bepaald eerst de zet van de gebruiker verder te lezen in move(), wanneer deze gezet is, word de actie van de computer uitgevoerd. ->
# de functie van de computer is de random functie die eerder is ingevoerd en kiest een hele getal tussen 1 en 3
# Het resultaat van beide acties worden doorgegeven in de result functie. om uit te rekenen wie gewonnen heeft.
def game():
	player = move()
	computer = random.randint(1, 3)
	result(player, computer)
	return play_again()

# dit is de keuze van de gebruiker. raw_input vraagt wat de gebruiker in wil voeren zo niet dan verschijnt er een error tekst
def move():
	while True:
		print
		player = raw_input("rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
		try:
			player = int(player)
			if player in (1,2,3):
				return player
		except valueError:
			pass
		print "Oops! I didn't understand that. please enter 1, 2 or 3."

# hier wordt de time functie gebruikt die eerder is ingeladen.  met een pauze van 1 sec.
# 
def result(player, computer):
	print "1..."
	time.sleep(1)
	print "2..."
	time.sleep(1)
	print "3..."
	time.sleep(0.5)
	print "Computer threw {0}!".format(names[computer])
	global player_score, computer_score
	if player == computer:
		print "Tie game"
	else:
		if rules[player] == computer:
			print "Your victory has been assured."
			player_score += 1
		else:
			print "The computer laughs as you realise you have been defeated."
			computer_score += 1

def play_again():
	answer = raw_input("Would you like to play again? y/n: ")
	if answer in ("y", "Y", "yes", "Yes", "of course!"):
		return answer
	else:
		print "Thank you very much for playing our game. See you next time!"

def scores():
	global player_score, computer_score
	print "HIGH SCORES"
	print "Player: ", player_score
	print "Computer: ", computer_score

#dit maakt het mogelijk het script op 2 manieren te gebruiken. ten eerste kunnen we het vanaf de commandline uitvoeren.
#de 2e kan het importeerd worden in een ander python script de code wordt op deze manier niet uitgevoerd worden zodra het geimporteerd worden.
if __name__ == '__main__':
	start()
