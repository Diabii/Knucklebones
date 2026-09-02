import random
from collections import Counter


# Creates a 3x3 board with None values
def create_board():
    return [[None] * 3 for _ in range(3)]


# Rolls a die and returns a number between 1 and 6
def roll_die():
    return random.randint(1, 6)


# Calculates the score for a single column based on the rules of Knucklebones
def calculate_column_score(column):
    numbers = [
        value
        for value in column
        if value is not None
    ]

    counter = Counter(numbers)

    score = 0

    for number, count in counter.items():
        score += number * count * count

    return score


# Calculates the total score for all columns and returns a dictionary with individual column scores and the total score
def calculate_score(columns):
    column_scores = [
        calculate_column_score(column)
        for column in columns
    ]

    return {
        "columns": column_scores,
        "total": sum(column_scores)
    }


# Places a die in the first available index of the specified column. Returns True if successful, False if the column is full.
def place_die(columns, column_index, pips):
    column = columns[column_index]

    for index in range(3):
        if column[index] is None:
            column[index] = pips
            return True

    return False


# Removes all identical dice from the opponent's corresponding column and shifts the remaining dice towards index 0.
def remove_opponent_dice(
    opponent_columns,
    column_index,
    pips
):
    opponent_column = opponent_columns[column_index]

    remaining_dice = [
        value
        for value in opponent_column
        if value is not None and value != pips
    ]

    opponent_columns[column_index] = (
        remaining_dice
        + [None] * (3 - len(remaining_dice))
    )


# Executes a full move: places a die and removes identical dice from the opponent's column. Returns True if the move was successful, False if the column was full.
def make_move(
    player_columns,
    opponent_columns,
    column_index,
    pips
):
    die_placed = place_die(
        player_columns,
        column_index,
        pips
    )

    if not die_placed:
        return False

    remove_opponent_dice(
        opponent_columns,
        column_index,
        pips
    )

    return True


# Checks if all positions on the board are occupied. Returns True if the board is full, False otherwise.
def full_board(columns):
    return all(
        value is not None
        for column in columns
        for value in column
    )


# Prints the current state of the board and the player's scores in the console.
def print_board(player, columns):
    print(f"\nBoard of Player {player}:")

    for index, column in enumerate(columns, start=1):
        print(f"Column {index}: {column}")

    score = calculate_score(columns)

    print("Column scores:", score["columns"])
    print("Total:", score["total"])


# Prints the state of both players' boards and their scores in the console.
def print_game_state(player_1_columns, player_2_columns):
    print_board(1, player_1_columns)
    print_board(2, player_2_columns)