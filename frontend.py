from pathlib import Path

import pygame


# Okno 16:9
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

BACKGROUND_COLOR = (205, 229, 245)
TEXT_COLOR_1 = (176, 129, 77)
TEXT_COLOR_2 = (83, 120, 95)

# Folder, w którym znajduje się frontend.py
BASE_DIR = Path(__file__).resolve().parent

# Folder z grafikami
GRAPHICS_DIR = BASE_DIR / "Graphics"

# Ścieżki do grafik
COLUMN_GREEN_PATH = GRAPHICS_DIR / "column_green.png"
COLUMN_ORANGE_PATH = GRAPHICS_DIR / "column_orange.png"
DESK_GREEN_PATH = GRAPHICS_DIR / "desk_green.png"
DESK_ORANGE_PATH = GRAPHICS_DIR / "desk_orange.png"
FONT_PATH = GRAPHICS_DIR / "pixel.ttf"

# Rozmiar jednej całej kolumny, czyli 3 miejsca pionowo
COLUMN_WIDTH = 100
COLUMN_HEIGHT = 290

# Przerwa między gotowymi grafikami kolumn
COLUMN_GAP = 28

# Rozmiar miejsca do rzucania kostką
DESK_WIDTH = 240
DESK_HEIGHT = 160

# Odległość między planszami graczy
PLAYERS_GAP = 80


def load_image(path, size):
    """
    Wczytuje grafikę, zachowuje przezroczystość
    i skaluje ją do podanego rozmiaru.
    """

    image = pygame.image.load(str(path)).convert_alpha()

    return pygame.transform.smoothscale(
        image,
        size
    )


def load_graphics():
    """Wczytuje wszystkie grafiki potrzebne do frontendu."""

    return {
        "column_green": load_image(
            COLUMN_GREEN_PATH,
            (COLUMN_WIDTH, COLUMN_HEIGHT)
        ),
        "column_orange": load_image(
            COLUMN_ORANGE_PATH,
            (COLUMN_WIDTH, COLUMN_HEIGHT)
        ),
        "desk_green": load_image(
            DESK_GREEN_PATH,
            (DESK_WIDTH, DESK_HEIGHT)
        ),
        "desk_orange": load_image(
            DESK_ORANGE_PATH,
            (DESK_WIDTH, DESK_HEIGHT)
        )
    }


def get_board_width():
    """Zwraca szerokość trzech kolumn wraz z przerwami."""

    return (
        3 * COLUMN_WIDTH
        + 2 * COLUMN_GAP
    )


def draw_board(screen, column_image, start_x, start_y):
    """
    Wyświetla trzy gotowe grafiki kolumn obok siebie.
    Każda grafika zawiera już trzy miejsca pionowo.
    """

    for column_index in range(3):
        x = start_x + column_index * (
            COLUMN_WIDTH + COLUMN_GAP
        )

        screen.blit(
            column_image,
            (x, start_y)
        )


def draw_player_label(screen, font, text, desk_x, desk_y, color):
    """Wyświetla nazwę gracza nad jego miejscem do rzucania."""

    label = font.render(
        text,
        True,
        color
    )

    label_rect = label.get_rect(
        centerx=desk_x + DESK_WIDTH // 2,
        bottom=desk_y - 10
    )

    screen.blit(label, label_rect)


def draw_game(screen, graphics, font):
    """Wyświetla statyczny układ obu graczy."""

    board_width = get_board_width()

    # Plansze są wyśrodkowane w poziomie
    board_x = (
        WINDOW_WIDTH - board_width
    ) // 2

    all_boards_height = (
        2 * COLUMN_HEIGHT
        + PLAYERS_GAP
    )

    # Plansza pomarańczowego gracza u góry
    orange_board_y = (
        WINDOW_HEIGHT - all_boards_height
    ) // 2

    # Plansza zielonego gracza na dole
    green_board_y = (
        orange_board_y
        + COLUMN_HEIGHT
        + PLAYERS_GAP
    )

    # Gracz 1, pomarańczowy, u góry
    draw_board(
        screen,
        graphics["column_orange"],
        board_x,
        orange_board_y
    )

    # Gracz 2, zielony, na dole
    draw_board(
        screen,
        graphics["column_green"],
        board_x,
        green_board_y
    )

    # Pomarańczowe miejsce do rzucania, prawy górny róg
    orange_desk_x = WINDOW_WIDTH - DESK_WIDTH - 45
    orange_desk_y = 65

    screen.blit(
        graphics["desk_orange"],
        (orange_desk_x, orange_desk_y)
    )

    # Zielone miejsce do rzucania, lewy dolny róg
    green_desk_x = 45
    green_desk_y = WINDOW_HEIGHT - DESK_HEIGHT - 45

    screen.blit(
        graphics["desk_green"],
        (green_desk_x, green_desk_y)
    )

    draw_player_label(
        screen,
        font,
        "Player 1",
        orange_desk_x,
        orange_desk_y,
        TEXT_COLOR_1
    )
    
    draw_player_label(
        screen,
        font,
        "Player 2",
        green_desk_x,
        green_desk_y,
        TEXT_COLOR_2
    )


def run_frontend():
    """Uruchamia statyczny frontend bez mechaniki gry."""

    pygame.init()

    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )

    pygame.display.set_caption("Knucklebones")

    # Zwykła domyślna czcionka pygame
    font = pygame.font.Font(str(FONT_PATH), 24)

    graphics = load_graphics()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        draw_game(
            screen,
            graphics,
            font
        )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run_frontend()