# project3

# project3

This is program coded by Seunglee Choi for project3 of ECE2524

This program replicates the game "Hangman"
test.py program is executable on terminal by typing:
./test.py

To start a game, program will select a random word from wordbank.txt which contains number of names of animals in the world and set it as the answer key.

Player is given 8 attempts, and player may guess an alphabet or a whole word.
For example, if player enters 'a', program will do search to find alpha bet a(s) in the answer key. If alphabet is found, program will show in which locations the alphabet matches with the answer key on the screen.
If there is no match, program will start drawing hangman as a penalty.

If player guesses by a word, for example 'koala', program will check if it matches with the answer key, and if the player guesses right, program will end, and the user wins. If not, user gets to try again (if there is any more attempt left) and hangman is drawn on screen.


# project3
