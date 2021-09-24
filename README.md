# RJKTQ™
RJK'S Trivia Quiz Game ™

The project is a trivia quiz game that consists of matches where random questions are asked related to current affairs and answers can be input by the user/player as 
keywords related to the answer. It is developed using Python 3.x and the questions, answers, information about every player who has played the game and every admin 
who monitors player activity and information to be displayed in the leaderboard are stored in the back-end of the program, viz. the text, binary and CSV* files.

Python is a general purpose, dynamic, high level and interpreted language. It supports an OOP** approach to developing applications. It is simple and easy to 
learn and provides a lot of high-level data structures. Therefore this language was apt for the coding of the program.

The key elements of the program are: “Profile”, “Leaderboard”, “Settings” and “Quick Play”. Players or admins have to create an account or log into an existing 
one when the game is being run, by creating a username and password. Players get to see their rank by selecting “Leaderboard” in the menu among the several others who played the game. Ranking will be based on highest scores earned in “Quick Play”, level, and no. of achievements earned by the player. Selecting “Play” in the game menu opens a 1-round match which rewards EXP*** for levelling up. The game is played by answering a set of 20 questions, randomly selected. There are 3 lifelines provided that can be used during each attempt. By doing a special set of tasks, players receive achievements that can enhance their profile. By selecting “Settings” in the menu, the admins have access to manipulating stored data, such as data related to questions, answers, leaderboard and accounts. The admins do not have access to the “Quick Play” feature while the players do not have access to the game’s settings. Other features include “Achievements”, “Help” and “Quit”. 

The menu-driven program wherein the user can enter simple keywords in order to utilize the game’s various features consists of user-defined functions catered to the 
functioning of each element of the game. Sensitive information stored in the back end is pseudo-encrypted in the form of binary data. Confirmation requests are also 
added into the code to prevent errors from the user wherever possible. The program and every menu option can be run multiple times for as long as the user 
wishes and any update in the player’s performance can be seen immediately.

*CSV – Comma Separated Values, **OOP – Object Oriented Programming, ***EXP – Experience Points

Requirements
1. Python 3
2. Python module tabulate
