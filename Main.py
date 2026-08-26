import random
from collections import Counter


def calculate_column_score(column):
    """
    Oblicza wynik jednej kolumny.
    """
    numbers = [value for value in column if value is not None]
    counter = Counter(numbers)

    score = 0

    for number, count in counter.items():
        score += number * count * count

    return score


def calculate_score(columns):
    """
    Zwraca wyniki każdej kolumny osobno oraz total.

    Przykładowy wynik:
    {
        "columns": [10, 28, 5],
        "total": 43
    }
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
    Umieszcza kostkę na najniższym wolnym indeksie.

    Zwraca True, jeśli udało się położyć kostkę.
    Zwraca False, jeśli kolumna jest pełna.
    """
    column = columns[column_index]

    for i in range(3):
        if column[i] is None:
            column[i] = pips
            return True

    return False


def remove_opponent_dice(opponent_columns, column_index, pips):
    """
    Usuwa z odpowiedniej kolumny przeciwnika wszystkie kostki
    mające taką samą liczbę oczek jak właśnie położona kostka.

    Pozostałe kostki przesuwa na najniższe indeksy.
    """
    opponent_column = opponent_columns[column_index]

    remaining_dice = [
        value
        for value in opponent_column
        if value is not None and value != pips
    ]

    opponent_columns[column_index] = (
        remaining_dice + [None] * (3 - len(remaining_dice))
    )


def full_board(columns):
    return all(
        value is not None
        for column in columns
        for value in column
    )


def print_board(player, columns):
    print(f"\nBoard of player {player}:")

    for index, column in enumerate(columns, start=1):
        print(f"Column {index}: {column}")

    score = calculate_score(columns)

    print("Column scores:", score["columns"])
    print("Total:", score["total"])


def choose_column(columns):
    """
    Pyta o kolumnę tak długo, aż gracz wybierze poprawną,
    niepełną kolumnę.
    """
    while True:
        try:
            column_index = int(
                input("Where to place the die? (column 1-3): ")
            ) - 1

            if not 0 <= column_index < 3:
                print("Choose a column from 1 to 3.")
                continue

            if None not in columns[column_index]:
                print("This column is full. Choose another one.")
                continue

            return column_index

        except ValueError:
            print("Enter a number from 1 to 3.")


def turn(player, player_columns, opponent_columns):
    print()

    pips = random.randint(1, 6)
    print(f"Player {player} rolled: {pips}")

    column_index = choose_column(player_columns)

    die_placed = place_die(
        player_columns,
        column_index,
        pips
    )

    if die_placed:
        remove_opponent_dice(
            opponent_columns,
            column_index,
            pips
        )

    print_board(player, player_columns)

    opponent = 2 if player == 1 else 1
    print_board(opponent, opponent_columns)


columns_gracz1 = [[None] * 3 for _ in range(3)]
columns_gracz2 = [[None] * 3 for _ in range(3)]


while True:
    turn(
        player=1,
        player_columns=columns_gracz1,
        opponent_columns=columns_gracz2
    )

    if full_board(columns_gracz1):
        break

    turn(
        player=2,
        player_columns=columns_gracz2,
        opponent_columns=columns_gracz1
    )

    if full_board(columns_gracz2):
        break


score1 = calculate_score(columns_gracz1)
score2 = calculate_score(columns_gracz2)

print("\nEnd of the game!")

print(f"Player 1 columns: {score1['columns']}")
print(f"Player 1 total: {score1['total']}")

print(f"Player 2 columns: {score2['columns']}")
print(f"Player 2 total: {score2['total']}")

if score1["total"] > score2["total"]:
    print("Player 1 wins!")
elif score1["total"] < score2["total"]:
    print("Player 2 wins!")
else:
    print("It's a tie!")