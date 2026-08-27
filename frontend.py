import pygame


# Rozdzielczość 16:9
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Kolory
BACKGROUND_COLOR = (43, 23, 3)
SLOT_COLOR = (148, 127, 91)
SLOT_BORDER_COLOR = (69, 59, 42)

# Rozmiary pól
SLOT_SIZE = 90

# Przerwa między polami w tej samej kolumnie
ROW_GAP = 8

# Większa przerwa między kolumnami
COLUMN_GAP = 28

# Odległość między planszami graczy
PLAYERS_GAP = 100


def draw_slot(screen, x, y):
    """Rysuje jedno kwadratowe miejsce na kostkę."""

    slot_rect = pygame.Rect(
        x,
        y,
        SLOT_SIZE,
        SLOT_SIZE
    )

    pygame.draw.rect(
        screen,
        SLOT_COLOR,
        slot_rect,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        SLOT_BORDER_COLOR,
        slot_rect,
        width=3,
        border_radius=10
    )


def get_board_size():
    """Zwraca szerokość i wysokość jednej planszy 3x3."""

    board_width = (
        3 * SLOT_SIZE
        + 2 * COLUMN_GAP
    )

    board_height = (
        3 * SLOT_SIZE
        + 2 * ROW_GAP
    )

    return board_width, board_height


def draw_board(screen, start_x, start_y):
    """
    Rysuje planszę 3 kolumny na 3 miejsca.

    Większa przerwa jest między kolumnami,
    mniejsza między miejscami w kolumnie.
    """

    for column_index in range(3):
        x = start_x + column_index * (
            SLOT_SIZE + COLUMN_GAP
        )

        for row_index in range(3):
            y = start_y + row_index * (
                SLOT_SIZE + ROW_GAP
            )

            draw_slot(screen, x, y)


def draw_game(screen):
    """Rysuje obie plansze graczy."""

    board_width, board_height = get_board_size()

    # Wyśrodkowanie plansz w poziomie
    board_x = (
        WINDOW_WIDTH - board_width
    ) // 2

    # Łączna wysokość obu plansz i przerwy między nimi
    all_boards_height = (
        board_height * 2
        + PLAYERS_GAP
    )

    # Wyśrodkowanie całego układu w pionie
    opponent_board_y = (
        WINDOW_HEIGHT - all_boards_height
    ) // 2

    player_board_y = (
        opponent_board_y
        + board_height
        + PLAYERS_GAP
    )

    # Przeciwnik u góry
    draw_board(
        screen,
        board_x,
        opponent_board_y
    )

    # Gracz na dole
    draw_board(
        screen,
        board_x,
        player_board_y
    )


def run_frontend():
    """Uruchamia samo okno gry, bez mechaniki."""

    pygame.init()

    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )

    pygame.display.set_caption("Knucklebones")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        draw_game(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run_frontend()