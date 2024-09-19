# RJKTQ - RJK's Trivia Quest

<p align="center">
  <img src="https://github.com/rishn/RJKTQ/blob/main/RJKTQ/Banner.png?raw=true" alt="Banner" />
</p>

**RJKTQ** is an interactive trivia quiz game developed in **Python 3.x**. The game is designed to challenge players with a variety of questions related to current affairs. Players can enter keywords as answers and track their performance through an integrated ranking system. The game also features administrator functionality to monitor and manage players, questions, and game data.

## Table of Contents

1. [RJKTQ - RJK's Trivia Quest](#rjktq---rjks-trivia-quest)
2. [Features](#features)
3. [File Storage Structure](#file-storage-structure)
4. [Requirements](#requirements)
5. [How to Run the Game](#how-to-run-the-game)
6. [Game Flow](#game-flow)

## Features

### 1. **Player and Admin Accounts**
   - Players and admins must create an account or log in to access the game. Admin accounts are granted special privileges.
   - User data such as usernames, passwords, player statistics (rank, level, high score, matches, and wins), and admin information are securely stored in binary and CSV files.
   
### 2. **Game Modes**
   - **Quick Play:** Players can engage in a single round of 20 randomly selected questions. Performance in Quick Play is rewarded with experience points (EXP), which are essential for leveling up.
   - **Lifelines:** Players have access to 3 lifelines during each round of Quick Play, which include options like Expert, Friend, and Magic 8 Ball to assist in answering questions.

### 3. **Leaderboards and Rankings**
   - The game features a **Leaderboard** that ranks players based on their highest scores, levels, and achievements.
   - Achievements are awarded based on special in-game tasks and contribute to a player’s ranking.

### 4. **Admin Functionality**
   - Admins can manage questions, answers, and leaderboard data via the **Settings** menu.
   - Special privileges include adding and clearing stored game data, modifying admin clearance keys, and adjusting the buffer text displayed during the game.
   - Admin accounts have restricted access to gameplay but can fully manage game settings and player data.

### 5. **Achievements**
   - Players can earn various achievements by completing specific tasks or reaching milestones such as obtaining high scores or leveling up.
   - Achievements are displayed on the player profile and can be used to unlock additional avatars.

### 6. **Profile and Customization**
   - Players can view their profiles, including statistics, avatar, and achievements. Custom avatars can be selected based on achievements earned.
   - Admin profiles display their admin rank (primary or subordinate).

### 7. **Security and Data Management**
   - Player and admin account data is pseudo-encrypted and stored securely in binary files.
   - The system includes confirmation prompts to minimize user errors and maintain data integrity.
   - Sensitive admin actions, such as modifying stored data, are protected by an admin clearance key.

## File Storage Structure
   - **Player data** is stored in `2.dat`, and **admin data** in `3.dat`.
   - **Leaderboard data** is stored in `4.csv`, while **questions** and their corresponding **answers** are saved in `5.dat` and `6.dat` respectively.
   - **Buffer text** used in various parts of the game is stored in `7.txt` and `8.txt`.
   - Admin clearance key is stored in `1.dat`.

## Requirements

1. **Python 3.x**: The game is developed using Python and relies on its built-in libraries, along with specific third-party modules.
2. **Python module**: `tabulate` is required to display data in a well-formatted table.
3. All files from the **RJKTQ folder** are essential for running the game, including the `.dat` and `.csv` files for storing game data.

To install the required module, run:
  ```bash
  pip install tabulate
  ```

## How to Run the Game

1. Ensure all necessary data files are located in the `data` folder within the working directory.
2. Launch the game by running the `start.py` script:

    ```bash
    python start.py
    ```
3. The game will prompt you to either create a player or admin account or log into an existing one.
4. Once logged in, players can access the Quick Play mode, view the leaderboard, or check their profile. Admins can access the settings to manage the game’s data.

## Game Flow

- **Player login/creation**: Players are guided through creating a username and password, which is validated against predefined criteria.
- **Game start**: Players answer 20 random questions, and their scores are calculated at the end of the match.
- **Lifelines**: Lifelines can be used to assist with answering difficult questions.
- **Leaderboard**: The leaderboard is updated based on player performance, ranking users by score, level, and achievements.
- **Achievements**: Various achievements are unlocked through gameplay and are displayed on the player’s profile.
