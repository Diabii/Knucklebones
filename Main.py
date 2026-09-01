import random
from collections import Counter


def create_board():
    """Tworzy pustą planszę z trzema kolumnami."""

    return [[None] * 3 for _ in range(3)]


def roll_die():
    """Losuje liczbę oczek od 1 do 6."""

    return random.randint(1, 6)


def calculate_column_score(column):
    """Oblicza wynik jednej kolumny."""

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


def calculate_score(columns):
    """
    Zwraca wyniki każdej kolumny osobno oraz total.
    """

    column_scores = [
        calculate_column_score(column)
        for column in columns
    ]

    return {
        "columns": column_scores,
        "total": sum(column_scores)
    }


def place_die(columns, column_index, pips):
    """
    Umieszcza kostkę na pierwszym wolnym indeksie.

    Index 0 ma inne położenie wizualne dla obu graczy,
    ale mechanicznie nadal jest pierwszym wolnym miejscem.
    """

    column = columns[column_index]

    for index in range(3):
        if column[index] is None:
            column[index] = pips
            return True

    return False


def remove_opponent_dice(
    opponent_columns,
    column_index,
    pips
):
    """
    Usuwa wszystkie identyczne kości przeciwnika
    z odpowiadającej kolumny.

    Pozostałe kości przesuwa w stronę indeksu 0.
    """

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


def make_move(
    player_columns,
    opponent_columns,
    column_index,
    pips
):
    """
    Wykonuje pełny ruch:
    1. umieszcza kostkę,
    2. zbija identyczne kości przeciwnika.

    Zwraca True, jeśli ruch został wykonany.
    Zwraca False, jeśli kolumna była pełna.
    """

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


def full_board(columns):
    """Sprawdza, czy wszystkie miejsca są zajęte."""

    return all(
        value is not None
        for column in columns
        for value in column
    )


def print_board(player, columns):
    """Wyświetla planszę i wyniki gracza w konsoli."""

    print(f"\nBoard of Player {player}:")

    for index, column in enumerate(columns, start=1):
        print(f"Column {index}: {column}")

    score = calculate_score(columns)

    print("Column scores:", score["columns"])
    print("Total:", score["total"])


def print_game_state(player_1_columns, player_2_columns):
    """Wyświetla stan obu plansz i punktację."""

    print_board(1, player_1_columns)
    print_board(2, player_2_columns)