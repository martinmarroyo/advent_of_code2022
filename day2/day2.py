"""Solution to day 2 of Advent of Code 2022"""
from pathlib import Path

def calculate_score(player1: str, player2: str, scoring: dict) -> int:
    """ Determines score for part 1 of problem

    Args:
        player1: The choice of rock/paper/scissor for player 1
        player2: The choice of rock/paper/scissor for player 2
        scoring: A map of choices to scores
    Returns:
        The total score for player 2 for a given game based on outcome
    """
    p1_choice = scoring[player1]
    p2_choice = scoring[player2]
    if p1_choice == p2_choice: #draw
        return p2_choice + 3
    elif p1_choice == 1: #rock
        return (
            p2_choice + 6 if p2_choice == 2 
            else p2_choice
        )
    elif p1_choice == 2: #paper
        return (
            p2_choice + 6 if p2_choice == 3 
            else p2_choice
        )
    elif p1_choice == 3: #scissors
        return (
            p2_choice + 6 if p2_choice == 1 
            else p2_choice
        )
    # If we get here, something went wrong
    return -1


def determine_outcome(p1: str, p2: str, choice_map: dict, outcome_map: dict) -> int:
    """ Determines the score for part 2 of the problem

    Here we are told that the column we assumed was a choice previously is rather
    what the outcome of the game should be. Using an outcome mapping and a choice mapping,
    this function determines what player 2's score should be based on the outcome of the game
    and player 1's choice.

    Args:
        p1:          Player 1's choice
        p2:          Outcome for player 2
        choice_map:  A mapping of choices for player one (rock/paper/scissors)
        outcome_map: The predetermined outcome for player 2 in the given game (win/lose/draw)
    Returns:
        The total score for player 2 based on the intended outcome and player 1's choice

    """
    p1_choice = choice_map[p1]
    outcome = outcome_map[p2]
    if outcome == 3: # draw
        return p1_choice + outcome
    elif outcome == 0: # lose
        if p1_choice == 1: return 3
        if p1_choice == 2: return 1
        return 2
    else: # win
        if p1_choice == 1: return 2 + outcome
        if p1_choice == 2: return 3 + outcome
        return 1 + outcome


with open(Path.cwd()/'day2/input.txt', 'r') as f:
    games = f.read().strip().split('\n')

# Part 1
game_map = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}
games = [game.split(' ') for game in games]
pt1_scores = map(lambda game: calculate_score(game[0], game[1], game_map), games)
pt1_total_score = sum(pt1_scores)
print(f'The total score for player 2 in part 1 is {pt1_total_score}')
# Part 2
outcome_map = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
choice_map = {
    'A': 1,
    'B': 2,
    'C': 3
}

new_outcomes = map(
    lambda game: determine_outcome(game[0], game[1], choice_map, outcome_map), 
    games
)
pt2_total = sum(new_outcomes)
print(f'The total score for player 2 in part 2 is {pt2_total}')