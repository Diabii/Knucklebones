from pathlib import Path
import random

import pygame
import Main as mechanics


# Okno 16:9
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

BACKGROUND_COLOR = (205, 229, 245)

TEXT_COLOR_1 = (176, 129, 77)
TEXT_COLOR_2 = (83, 120, 95)

TEXT_COLOR_1W = (252, 241, 227)
TEXT_COLOR_2W = (211, 242, 222)

MENU_TITLE_Y = 190

MENU_PLAY_Y = 380
MENU_RULES_Y = 500

MENU_LEFT_DICE_X = 125
MENU_RIGHT_DICE_MARGIN = 125

MENU_DICE_Y = (
    150,
    375,
    600
)


# Foldery
BASE_DIR = Path(__file__).resolve().parent
GRAPHICS_DIR = BASE_DIR / "Graphics"


# Ścieżki do grafik
COLUMN_GREEN_PATH = GRAPHICS_DIR / "column_green.png"
COLUMN_ORANGE_PATH = GRAPHICS_DIR / "column_orange.png"
DESK_GREEN_PATH = GRAPHICS_DIR / "desk_green.png"
DESK_ORANGE_PATH = GRAPHICS_DIR / "desk_orange.png"
FONT_PATH = GRAPHICS_DIR / "Pixeled.ttf"
BUTTON_PLAY_PATH = GRAPHICS_DIR / "button_play.png"
BUTTON_RULES_PATH = GRAPHICS_DIR / "button_rules.png"
BUTTON_RETRY_PATH = GRAPHICS_DIR / "button_retry.png"
RULES_BACKGROUND_PATH = GRAPHICS_DIR / "rules_background.png"
CLOSE_BUTTON_PATH = GRAPHICS_DIR / "X.png"

DICE_PATHS = {
    "normal": {
        pips: GRAPHICS_DIR / f"dice_{pips}.png"
        for pips in range(1, 7)
    },
    "yellow": {
        pips: GRAPHICS_DIR / f"dice_{pips}_y.png"
        for pips in range(1, 7)
    },
    "red": {
        pips: GRAPHICS_DIR / f"dice_{pips}_r.png"
        for pips in range(1, 7)
    }
}

BACKGROUND_PATH = GRAPHICS_DIR / "background.png"

# Rozmiar jednej całej kolumny
COLUMN_WIDTH = 130
COLUMN_HEIGHT = 290

# Odległość między kolumnami
COLUMN_GAP = 28

# Rozmiar miejsca do rzucania
DESK_WIDTH = 240
DESK_HEIGHT = 160

# Rozmiar kostki umieszczonej w kolumnie
BOARD_DICE_SIZE = 70

# Rozmiar kostki wyświetlanej na biurku
DESK_DICE_SIZE = 100

MENU_DICE_SIZE = 160

# Czas trwania animacji rzutu w milisekundach
ROLL_DURATION = 1000

# Co ile milisekund zmienia się grafika podczas rzutu
ROLL_FRAME_TIME = 50

# Odległość między planszami
PLAYERS_GAP = 80

# Rozmiary przycisków
BIG_BUTTON_WIDTH = 294   # 49
BIG_BUTTON_HEIGHT = 120   # 20

SMALL_BUTTON_WIDTH = 222   # 37
SMALL_BUTTON_HEIGHT = 84   # 14

# Przyciemnienie menu i ekranu końcowego
OVERLAY_ALPHA = 200

# Okno zasad
RULES_BACKGROUND_WIDTH = 760
RULES_BACKGROUND_HEIGHT = 520

# Przycisk X
CLOSE_BUTTON_SIZE = 48

# Pozycja okna zasad
RULES_WINDOW_X = (
    WINDOW_WIDTH - RULES_BACKGROUND_WIDTH
) // 2

RULES_WINDOW_Y = (
    WINDOW_HEIGHT - RULES_BACKGROUND_HEIGHT
) // 2

# Kolor tekstu zasad, taki jak przycisk RULES
RULES_TEXT_COLOR = (221, 148, 252)


def load_image(path, size):
    """
    Wczytuje grafikę, zachowuje przezroczystość
    i skaluje ją do podanego rozmiaru.
    """

    image = pygame.image.load(
        str(path)
    ).convert_alpha()

    return pygame.transform.smoothscale(
        image,
        size
    )


def load_graphics():
    """Wczytuje wszystkie grafiki."""

    graphics = {
        "background": load_image(
            BACKGROUND_PATH,
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        ),
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
        ),
        "button_play": load_image(
            BUTTON_PLAY_PATH,
            (BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
        ),
        "button_rules": load_image(
            BUTTON_RULES_PATH,
            (SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)
        ),
        "button_retry": load_image(
            BUTTON_RETRY_PATH,
            (SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)
        ),
        "rules_background": load_image(
            RULES_BACKGROUND_PATH,
            (
                RULES_BACKGROUND_WIDTH,
                RULES_BACKGROUND_HEIGHT
            )
        ),

        "close_button": load_image(
            CLOSE_BUTTON_PATH,
            (
                CLOSE_BUTTON_SIZE,
                CLOSE_BUTTON_SIZE
            )
        ),
        "menu_dice": {},

        # Kostki na planszy w trzech wariantach
        "board_dice": {
            "normal": {},
            "yellow": {},
            "red": {}
        },

        # Kostki na biurku zawsze pozostają zwykłe
        "desk_dice": {}
    }

    for pips in range(1, 7):
        graphics["board_dice"]["normal"][pips] = load_image(
            DICE_PATHS["normal"][pips],
            (BOARD_DICE_SIZE, BOARD_DICE_SIZE)
        )

        graphics["board_dice"]["yellow"][pips] = load_image(
            DICE_PATHS["yellow"][pips],
            (BOARD_DICE_SIZE, BOARD_DICE_SIZE)
        )

        graphics["board_dice"]["red"][pips] = load_image(
            DICE_PATHS["red"][pips],
            (BOARD_DICE_SIZE, BOARD_DICE_SIZE)
        )

        # Animacja rzutu na biurku używa zwykłych białych kostek
        graphics["desk_dice"][pips] = load_image(
            DICE_PATHS["normal"][pips],
            (DESK_DICE_SIZE, DESK_DICE_SIZE)
        )

        graphics["menu_dice"][pips] = load_image(
            DICE_PATHS["normal"][pips],
            (MENU_DICE_SIZE, MENU_DICE_SIZE)
        )

    return graphics

def wrap_text(text, font, max_width):
    """
    Dzieli tekst na linie mieszczące się
    w podanej szerokości.
    """

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = (
            f"{current_line} {word}".strip()
        )

        test_width = font.size(
            test_line
        )[0]

        if test_width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)

            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

def draw_close_button(
    screen,
    close_image,
    center,
    mouse_position,
    mouse_pressed
):
    """
    Rysuje przycisk X z efektem hover i pressed.
    Zwraca jego klikalny prostokąt.
    """

    base_rect = close_image.get_rect(
        center=center
    )

    is_hovered = base_rect.collidepoint(
        mouse_position
    )

    is_pressed = (
        is_hovered
        and mouse_pressed
    )

    scale = 1.08 if is_hovered else 1.0

    width = int(
        close_image.get_width() * scale
    )

    height = int(
        close_image.get_height() * scale
    )

    displayed_image = pygame.transform.smoothscale(
        close_image,
        (width, height)
    )

    displayed_rect = displayed_image.get_rect(
        center=center
    )

    displayed_rect.y -= 3
    displayed_rect.x += 3

    if is_pressed:
        displayed_rect.y += 2

    screen.blit(
        displayed_image,
        displayed_rect
    )

    effect = pygame.Surface(
        displayed_rect.size,
        pygame.SRCALPHA
    )

    if is_pressed:
        effect.fill(
            (0, 0, 0, 80)
        )
    elif is_hovered:
        effect.fill(
            (255, 255, 255, 35)
        )

    screen.blit(
        effect,
        displayed_rect
    )

    return base_rect

def draw_rules_window(
    screen,
    graphics,
    rules_title_font,
    rules_text_font,
    rules_fun_font
):
    """
    Przyciemnia menu i wyświetla okno zasad.

    Zwraca prostokąt przycisku X.
    """

    draw_dark_overlay(screen)

    panel_x = RULES_WINDOW_X
    panel_y = RULES_WINDOW_Y

    screen.blit(
        graphics["rules_background"],
        (panel_x, panel_y)
    )

    # X w prawym górnym rogu panelu
    close_center = (
        panel_x + RULES_BACKGROUND_WIDTH - 38,
        panel_y + 38
    )

    close_rect = draw_close_button(
        screen,
        graphics["close_button"],
        close_center,
        pygame.mouse.get_pos(),
        pygame.mouse.get_pressed()[0]
    )

    # Tytuł RULES
    title_surface = rules_title_font.render(
        "RULES",
        True,
        RULES_TEXT_COLOR
    )

    title_rect = title_surface.get_rect(
        center=(
            panel_x + RULES_BACKGROUND_WIDTH // 2,
            panel_y + 78
        )
    )

    screen.blit(
        title_surface,
        title_rect
    )

    rules_text = (
        "Knucklebones is a two-player turn-based game "
        "in which the player with the highest score wins. "
        "Points are calculated by adding the values of a "
        "player's dice. When identical dice are placed in "
        "the same column, their values are doubled or tripled. "
        "You can destroy an opponent's dice by placing a die "
        "with the same value in the corresponding column. "
        "The game ends when either player's board is completely full."
    )

    text_left = panel_x + 85
    text_width = RULES_BACKGROUND_WIDTH - 170
    text_start_y = panel_y + 120

    lines = wrap_text(
        rules_text,
        rules_text_font,
        text_width
    )

    line_height = rules_text_font.get_linesize() 

    for line_index, line in enumerate(lines):
        line_surface = rules_text_font.render(
            line,
            True,
            RULES_TEXT_COLOR
        )

        line_rect = line_surface.get_rect(
            centerx=panel_x + RULES_BACKGROUND_WIDTH // 2,
            top=text_start_y + line_index * line_height
        )

        screen.blit(
            line_surface,
            line_rect
        )

    # Have fun
    have_fun_surface = rules_fun_font.render(
        "HAVE FUN!",
        True,
        RULES_TEXT_COLOR
    )

    have_fun_rect = have_fun_surface.get_rect(
        center=(
            panel_x + RULES_BACKGROUND_WIDTH // 2,
            panel_y + RULES_BACKGROUND_HEIGHT - 65
        )
    )

    screen.blit(
        have_fun_surface,
        have_fun_rect
    )

    return close_rect


def draw_dark_overlay(screen):
    """Nakłada półprzezroczyste przyciemnienie na ekran."""

    overlay = pygame.Surface(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, OVERLAY_ALPHA)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

def draw_button(
    screen,
    button_image,
    button_font,
    text,
    text_color,
    center,
    mouse_position,
    mouse_pressed
):
    """
    Rysuje dowolny przycisk z efektem hover i pressed.

    Rozmiar jest pobierany bezpośrednio z grafiki,
    więc funkcja działa zarówno dla dużego PLAY,
    jak i małych RULES oraz RETRY.

    Zwraca stały pygame.Rect używany do kliknięcia.
    """

    base_rect = button_image.get_rect(
        center=center
    )

    is_hovered = base_rect.collidepoint(
        mouse_position
    )

    is_pressed = (
        is_hovered
        and mouse_pressed
    )

    # Jednolity hover dla wszystkich rozmiarów
    if is_hovered:
        scale = 1.04
    else:
        scale = 1.0

    current_width = int(
        button_image.get_width() * scale
    )

    current_height = int(
        button_image.get_height() * scale
    )

    displayed_image = pygame.transform.smoothscale(
        button_image,
        (current_width, current_height)
    )

    if is_pressed:
        displayed_image.set_alpha(170)

    elif is_hovered:
        displayed_image.set_alpha(220)

    displayed_rect = displayed_image.get_rect(
        center=center
    )

    # Wciśnięcie przesuwa cały przycisk lekko w dół
    if is_pressed:
        displayed_rect.y += 3

    screen.blit(
        displayed_image,
        displayed_rect
    )

    # Renderujemy wyłącznie napis aktualnego przycisku
    button_text = button_font.render(
        text,
        True,
        text_color
    )

    text_rect = button_text.get_rect(
        center=displayed_rect.center
    )

    text_rect.y -= 5

    screen.blit(
        button_text,
        text_rect
    )

    # Obszar klikalny ma bazowy rozmiar grafiki.
    # Nie zmienia się podczas hover.
    return base_rect

def draw_menu(
    screen,
    graphics,
    title_font,
    title_y,
    big_button_font,
    small_button_font,
    footer_font,
    dice_positions_y
):
    """
    Wyświetla ekran startowy.

    Zwraca prostokąty przycisków PLAY i RULES.
    """

    screen.blit(
        graphics["background"],
        (0, 0)
    )

    # Dekoracyjne kostki po lewej: 1, 2, 3
    left_x = 125

    for pips, y in zip(
        (1, 2, 3),
        dice_positions_y
    ):
        die_image = graphics["menu_dice"][pips]

        die_rect = die_image.get_rect(
            center=(left_x, y)
        )

        screen.blit(
            die_image,
            die_rect
        )

    # Dekoracyjne kostki po prawej: 4, 5, 6
    right_x = WINDOW_WIDTH - 125

    for pips, y in zip(
        (4, 5, 6),
        dice_positions_y
    ):
        die_image = graphics["menu_dice"][pips]

        die_rect = die_image.get_rect(
            center=(right_x, y)
        )

        screen.blit(
            die_image,
            die_rect
        )

    # Tytuł
    title = title_font.render(
        "KNUCKLEBONES",
        True,
        (245, 245, 245)
    )

    title_rect = title.get_rect(
        center=(
            WINDOW_WIDTH // 2,
            title_y
        )
    )

    screen.blit(
        title,
        title_rect
    )

    mouse_position = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]

    play_rect = draw_button(
        screen,
        graphics["button_play"],
        big_button_font,
        "PLAY",
        (32, 193, 233),
        center=(
            WINDOW_WIDTH // 2,
            MENU_PLAY_Y
        ),
        mouse_position=mouse_position,
        mouse_pressed=mouse_pressed
    )

    rules_rect = draw_button(
        screen,
        graphics["button_rules"],
        small_button_font,
        "RULES",
        (221, 148, 252),
        center=(
            WINDOW_WIDTH // 2,
            MENU_RULES_Y
        ),
        mouse_position=mouse_position,
        mouse_pressed=mouse_pressed
    )

    # Stopka
    author_text = footer_font.render(
        "Programmed by Diabi",
        True,
        (230, 230, 230)
    )

    author_rect = author_text.get_rect(
        center=(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT - 67
        )
    )

    screen.blit(
        author_text,
        author_rect
    )

    inspiration_text = footer_font.render(
        "Inspired by Knucklebones from Cult of the Lamb",
        True,
        (190, 190, 190)
    )

    inspiration_rect = inspiration_text.get_rect(
        center=(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT - 45
        )
    )

    screen.blit(
        inspiration_text,
        inspiration_rect
    )

    return play_rect, rules_rect

def create_new_game():
    """Tworzy i zwraca początkowy stan nowej gry."""

    start_time = pygame.time.get_ticks()

    return {
        "player_1_columns": mechanics.create_board(),
        "player_2_columns": mechanics.create_board(),
        "current_player": random.choice(
            [1, 2]
        ),
        "current_pips": mechanics.roll_die(),
        "displayed_pips": random.randint(1, 6),
        "rolling": True,
        "roll_start_time": start_time,
        "last_roll_frame_time": start_time,
        "winner_printed": False
    }


def get_board_width():
    """Zwraca szerokość trzech kolumn wraz z przerwami."""

    return (
        3 * COLUMN_WIDTH
        + 2 * COLUMN_GAP
    )


def get_layout():
    """
    Oblicza pozycje plansz oraz biurek.

    Zwraca je w jednym słowniku, żeby rysowanie
    i obsługa kliknięć korzystały z tych samych pozycji.
    """

    board_width = get_board_width()

    board_x = (
        WINDOW_WIDTH - board_width
    ) // 2

    all_boards_height = (
        2 * COLUMN_HEIGHT
        + PLAYERS_GAP
    )

    orange_board_y = (
        WINDOW_HEIGHT - all_boards_height
    ) // 2

    green_board_y = (
        orange_board_y
        + COLUMN_HEIGHT
        + PLAYERS_GAP
    )

    orange_desk_x = (
        WINDOW_WIDTH
        - DESK_WIDTH
        - 45
    )
    orange_desk_y = 90

    green_desk_x = 45
    green_desk_y = (
        WINDOW_HEIGHT
        - DESK_HEIGHT
        - 90
    )

    return {
        "board_x": board_x,
        "orange_board_y": orange_board_y,
        "green_board_y": green_board_y,
        "orange_desk_x": orange_desk_x,
        "orange_desk_y": orange_desk_y,
        "green_desk_x": green_desk_x,
        "green_desk_y": green_desk_y
    }


def get_column_rects(board_x, board_y):
    """
    Tworzy prostokąty klikalne dla trzech kolumn.
    """

    column_rects = []

    for column_index in range(3):
        x = board_x + column_index * (
            COLUMN_WIDTH + COLUMN_GAP
        )

        column_rect = pygame.Rect(
            x,
            board_y,
            COLUMN_WIDTH,
            COLUMN_HEIGHT
        )

        column_rects.append(column_rect)

    return column_rects


def draw_player_info(
    screen,
    label_font,
    score_font,
    player_name,
    total_score,
    desk_x,
    desk_y,
    color,
    info_position
):
    """
    Wyświetla nazwę gracza i total score.

    info_position == "above":
        Player
        Score
        biurko

    info_position == "below":
        biurko
        Score
        Player
    """

    label = label_font.render(
        player_name,
        True,
        color
    )

    score_text = score_font.render(
        f"Score: {total_score}",
        True,
        color
    )

    desk_center_x = desk_x + DESK_WIDTH // 2

    if info_position == "above":
        # Player 2 pozostaje nad biurkiem
        label_rect = label.get_rect(
            centerx=desk_center_x,
            bottom=desk_y - 30
        )

        score_rect = score_text.get_rect(
            centerx=desk_center_x,
            top=label_rect.bottom - 18
        )

    else:
        # Player 1 pod biurkiem:
        # najpierw Score, niżej Player 1
        score_rect = score_text.get_rect(
            centerx=desk_center_x,
            top=desk_y + DESK_HEIGHT - 5
        )

        label_rect = label.get_rect(
            centerx=desk_center_x,
            top=score_rect.bottom - 22
        )

    screen.blit(label, label_rect)
    screen.blit(score_text, score_rect)


def draw_rolled_die(
    screen,
    dice_images,
    pips,
    desk_x,
    desk_y
):
    """
    Wyświetla grafikę aktualnej kostki
    na środku biurka aktywnego gracza.
    """

    die_image = dice_images[pips]

    die_rect = die_image.get_rect(
        center=(
            desk_x + DESK_WIDTH // 2,
            desk_y + DESK_HEIGHT // 2
        )
    )

    screen.blit(
        die_image,
        die_rect
    )


def get_die_center(
    board_x,
    board_y,
    column_index,
    data_index,
    player
):
    """
    Zwraca środek konkretnego pola w kolumnie.

    Player 1:
    index 0 znajduje się na dole.

    Player 2:
    index 0 znajduje się na górze.
    """

    x = (
        board_x
        + column_index * (
            COLUMN_WIDTH + COLUMN_GAP
        )
        + COLUMN_WIDTH // 2
    )

    if player == 1:
        visual_row = 2 - data_index
    else:
        visual_row = data_index

    slot_height = COLUMN_HEIGHT / 3

    y = int(
        board_y
        + visual_row * slot_height
        + slot_height / 2
    )

    return x, y


def draw_dice(
    screen,
    dice_images,
    columns,
    board_x,
    board_y,
    player
):
    """
    Wyświetla grafiki postawionych kostek.

    Jeśli dana wartość występuje w kolumnie:
    - 1 raz: kostka biała,
    - 2 razy: obie kostki żółte,
    - 3 razy: wszystkie trzy kostki czerwone.
    """

    for column_index, column in enumerate(columns):

        for data_index, pips in enumerate(column):

            if pips is None:
                continue

            # Liczymy wystąpienia tylko w aktualnej kolumnie
            pips_count = column.count(pips)

            if pips_count == 3:
                dice_variant = "red"

            elif pips_count == 2:
                dice_variant = "yellow"

            else:
                dice_variant = "normal"

            die_image = dice_images[dice_variant][pips]

            x, y = get_die_center(
                board_x,
                board_y,
                column_index,
                data_index,
                player
            )

            die_rect = die_image.get_rect(
                center=(x, y)
            )

            screen.blit(
                die_image,
                die_rect
            )


def draw_column_scores(
    screen,
    font,
    column_scores,
    board_x,
    board_y,
    player,
    color
):
    """
    Wyświetla wynik każdej kolumny.

    Player 1: wyniki pod planszą.
    Player 2: wyniki nad planszą.
    """

    for column_index, column_score in enumerate(column_scores):

        column_center_x = (
            board_x
            + column_index * (
                COLUMN_WIDTH + COLUMN_GAP
            )
            + COLUMN_WIDTH // 2
        )

        score_text = font.render(
            str(column_score),
            True,
            color
        )

        if player == 1:
            score_rect = score_text.get_rect(
                centerx=column_center_x,
                top=board_y + COLUMN_HEIGHT - 8
            )
        else:
            score_rect = score_text.get_rect(
                centerx=column_center_x,
                bottom=board_y
            )

        screen.blit(score_text, score_rect)


def draw_board(
    screen,
    column_image,
    dice_images,
    columns,
    start_x,
    start_y,
    player
):
    """
    Wyświetla grafiki trzech kolumn
    oraz umieszczone w nich kostki.
    """

    for column_index in range(3):
        x = start_x + column_index * (
            COLUMN_WIDTH + COLUMN_GAP
        )

        screen.blit(
            column_image,
            (x, start_y)
        )

    draw_dice(
        screen,
        dice_images,
        columns,
        start_x,
        start_y,
        player
    )


def draw_game(
    screen,
    graphics,
    label_font,
    score_font,
    player_1_columns,
    player_2_columns,
    current_player,
    displayed_pips
):
    """Wyświetla aktualny stan gry wraz z punktacją."""

    layout = get_layout()

    board_x = layout["board_x"]

    orange_board_y = layout["orange_board_y"]
    green_board_y = layout["green_board_y"]

    orange_desk_x = layout["orange_desk_x"]
    orange_desk_y = layout["orange_desk_y"]

    green_desk_x = layout["green_desk_x"]
    green_desk_y = layout["green_desk_y"]

    # Pobranie aktualnych wyników z backendu
    player_1_score = mechanics.calculate_score(
        player_1_columns
    )

    player_2_score = mechanics.calculate_score(
        player_2_columns
    )

    # Player 1, pomarańczowy, u góry
    draw_board(
        screen,
        graphics["column_orange"],
        graphics["board_dice"],
        player_1_columns,
        board_x,
        orange_board_y,
        player=1
    )

    # Player 2, zielony, na dole
    draw_board(
        screen,
        graphics["column_green"],
        graphics["board_dice"],
        player_2_columns,
        board_x,
        green_board_y,
        player=2
    )

    # Wyniki kolumn Player 1, pod planszą
    draw_column_scores(
        screen,
        score_font,
        player_1_score["columns"],
        board_x,
        orange_board_y,
        player=1,
        color=TEXT_COLOR_1W
    )

    # Wyniki kolumn Player 2, nad planszą
    draw_column_scores(
        screen,
        score_font,
        player_2_score["columns"],
        board_x,
        green_board_y,
        player=2,
        color=TEXT_COLOR_2W
    )

    # Biurko Player 1
    screen.blit(
        graphics["desk_orange"],
        (orange_desk_x, orange_desk_y)
    )

    # Biurko Player 2
    screen.blit(
        graphics["desk_green"],
        (green_desk_x, green_desk_y)
    )

    # Nazwa i total Player 1
    draw_player_info(
        screen,
        label_font,
        score_font,
        "Player 1",
        player_1_score["total"],
        orange_desk_x,
        orange_desk_y,
        TEXT_COLOR_1W,
        info_position="below"
    )

    # Nazwa i total Player 2
    draw_player_info(
        screen,
        label_font,
        score_font,
        "Player 2",
        player_2_score["total"],
        green_desk_x,
        green_desk_y,
        TEXT_COLOR_2W,
        info_position="above"
    )

    # Wylosowana liczba na biurku aktywnego gracza
    if current_player == 1:
        draw_rolled_die(
            screen,
            graphics["desk_dice"],
            displayed_pips,
            orange_desk_x,
            orange_desk_y
        )
    else:
        draw_rolled_die(
            screen,
            graphics["desk_dice"],
            displayed_pips,
            green_desk_x,
            green_desk_y
        )


def get_clicked_column(
    mouse_position,
    current_player
):
    """
    Sprawdza, czy kliknięto kolumnę aktywnego gracza.

    Zwraca indeks 0, 1 lub 2.
    Zwraca None, jeśli nie kliknięto kolumny.
    """

    layout = get_layout()

    if current_player == 1:
        board_y = layout["orange_board_y"]
    else:
        board_y = layout["green_board_y"]

    column_rects = get_column_rects(
        layout["board_x"],
        board_y
    )

    for column_index, column_rect in enumerate(column_rects):
        if column_rect.collidepoint(mouse_position):
            return column_index

    return None


def get_keyboard_column(key):
    """
    Zamienia klawisz 1, 2 lub 3
    na indeks kolumny 0, 1 lub 2.
    """

    key_to_column = {
        pygame.K_1: 0,
        pygame.K_2: 1,
        pygame.K_3: 2,
        pygame.K_KP1: 0,
        pygame.K_KP2: 1,
        pygame.K_KP3: 2
    }

    return key_to_column.get(key)


def try_move(
    current_player,
    current_pips,
    column_index,
    player_1_columns,
    player_2_columns
):
    """
    Próbuje wykonać ruch aktywnego gracza.

    Zwraca True, jeśli kostka została umieszczona.
    """

    if current_player == 1:
        player_columns = player_1_columns
        opponent_columns = player_2_columns
    else:
        player_columns = player_2_columns
        opponent_columns = player_1_columns

    move_successful = mechanics.make_move(
        player_columns,
        opponent_columns,
        column_index,
        current_pips
    )

    if not move_successful:
        print(
            f"Player {current_player}: "
            f"column {column_index + 1} is full."
        )

        return False

    print(
        f"\nPlayer {current_player} placed "
        f"{current_pips} in column {column_index + 1}."
    )

    mechanics.print_game_state(
        player_1_columns,
        player_2_columns
    )

    return True


def print_winner(
    player_1_columns,
    player_2_columns
):
    """Wyświetla końcowy wynik w konsoli."""

    score_1 = mechanics.calculate_score(
        player_1_columns
    )

    score_2 = mechanics.calculate_score(
        player_2_columns
    )

    print("\nEnd of the game!")

    print(
        f"Player 1 columns: {score_1['columns']}"
    )
    print(
        f"Player 1 total: {score_1['total']}"
    )

    print(
        f"Player 2 columns: {score_2['columns']}"
    )
    print(
        f"Player 2 total: {score_2['total']}"
    )

    if score_1["total"] > score_2["total"]:
        print("Player 1 wins!")
    elif score_2["total"] > score_1["total"]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

def draw_game_over_overlay(
    screen,
    graphics,
    winner_font,
    final_score_font,
    small_button_font,
    player_1_columns,
    player_2_columns
):
    """
    Przyciemnia ekran, wyświetla wynik
    i rysuje przycisk powrotu do menu.
    """

    score_1 = mechanics.calculate_score(
        player_1_columns
    )["total"]

    score_2 = mechanics.calculate_score(
        player_2_columns
    )["total"]

    draw_dark_overlay(screen)

    if score_1 > score_2:
        winner_text = "PLAYER 1 WINS!"
        winner_color = TEXT_COLOR_1W
        score_color = TEXT_COLOR_2W

    elif score_2 > score_1:
        winner_text = "PLAYER 2 WINS!"
        winner_color = TEXT_COLOR_2W
        score_color = TEXT_COLOR_1W

    else:
        winner_text = "IT'S A TIE!"
        winner_color = (245, 245, 245)
        score_color = (210, 210, 210)

    winner_surface = winner_font.render(
        winner_text,
        True,
        winner_color
    )

    winner_rect = winner_surface.get_rect(
        center=(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 - 100
        )
    )

    screen.blit(
        winner_surface,
        winner_rect
    )

    final_score_surface = final_score_font.render(
        f"{score_1} POINTS VS {score_2} POINTS",
        True,
        score_color
    )

    final_score_rect = final_score_surface.get_rect(
        center=(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 - 30
        )
    )

    screen.blit(
        final_score_surface,
        final_score_rect
    )

    retry_rect = draw_button(
        screen,
        graphics["button_retry"],
        small_button_font,
        "RETRY",
        (32, 193, 233),
        center=(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 + 100
        ),
        mouse_position=pygame.mouse.get_pos(),
        mouse_pressed=pygame.mouse.get_pressed()[0]
    )

    return retry_rect


def run_frontend():
    """Uruchamia menu i główną pętlę gry."""

    pygame.init()

    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )

    pygame.display.set_caption(
        "Knucklebones"
    )

    label_font = pygame.font.Font(
        str(FONT_PATH),
        24
    )

    score_font = pygame.font.Font(
        str(FONT_PATH),
        16
    )

    winner_font = pygame.font.Font(
        str(FONT_PATH),
        48
    )

    final_score_font = pygame.font.Font(
        str(FONT_PATH),
        20
    )

    title_font = pygame.font.Font(
        str(FONT_PATH),
        60
    )

    small_button_font = pygame.font.Font(
        str(FONT_PATH),
        22
    )

    big_button_font = pygame.font.Font(
        str(FONT_PATH),
        36
    )

    footer_font = pygame.font.Font(
        str(FONT_PATH),
        11
    )

    rules_title_font = pygame.font.Font(
        str(FONT_PATH),
        34
    )

    rules_text_font = pygame.font.Font(
        str(FONT_PATH),
        13
    )

    rules_fun_font = pygame.font.Font(
        str(FONT_PATH),
        20
    )

    graphics = load_graphics()

    # Dostępne stany:
    # "menu", "game", "game_over"
    game_state = "menu"

    game = create_new_game()

    play_rect = None
    rules_rect = None
    retry_rect = None
    close_rules_rect = None

    clock = pygame.time.Clock()
    running = True

    while running:
        current_time = pygame.time.get_ticks()

        # Animacja kostki działa wyłącznie podczas gry
        if (
            game_state == "game"
            and game["rolling"]
        ):
            if (
                current_time
                - game["last_roll_frame_time"]
                >= ROLL_FRAME_TIME
            ):
                game["displayed_pips"] = random.randint(
                    1,
                    6
                )

                game["last_roll_frame_time"] = current_time

            if (
                current_time
                - game["roll_start_time"]
                >= ROLL_DURATION
            ):
                game["rolling"] = False

                game["displayed_pips"] = game[
                    "current_pips"
                ]

                print(
                    f"Player {game['current_player']} rolled: "
                    f"{game['current_pips']}"
                )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                continue

            # RULES
            if game_state == "rules":

                if (
                    event.type == pygame.MOUSEBUTTONUP
                    and event.button == 1
                    and close_rules_rect is not None
                    and close_rules_rect.collidepoint(event.pos)
                ):
                    game_state = "menu"

                # Opcjonalnie ESC również zamyka zasady
                elif (
                    event.type == pygame.KEYDOWN
                    and event.key == pygame.K_ESCAPE
                ):
                    game_state = "menu"

                continue

        
            # MENU
            if game_state == "menu":

                if (
                    event.type == pygame.MOUSEBUTTONUP
                    and event.button == 1
                ):

                    if (
                        play_rect is not None
                        and play_rect.collidepoint(event.pos)
                    ):
                        game = create_new_game()
                        game_state = "game"

                    elif (
                        rules_rect is not None
                        and rules_rect.collidepoint(event.pos)
                    ):
                        game_state = "rules"

                continue


            # GAME OVER
            if game_state == "game_over":

                if (
                    event.type == pygame.MOUSEBUTTONUP
                    and event.button == 1
                    and retry_rect is not None
                    and retry_rect.collidepoint(event.pos)
                ):
                    # Czyszczenie całego stanu gry
                    game = create_new_game()

                    # RETRY zgodnie z ustaleniem
                    # wraca do menu głównego
                    game_state = "menu"

                continue

            # W trakcie animacji nie można stawiać kostki
            if game["rolling"]:
                continue

            selected_column = None

            if event.type == pygame.KEYDOWN:
                selected_column = get_keyboard_column(
                    event.key
                )

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    selected_column = get_clicked_column(
                        event.pos,
                        game["current_player"]
                    )

            if selected_column is None:
                continue

            move_successful = try_move(
                game["current_player"],
                game["current_pips"],
                selected_column,
                game["player_1_columns"],
                game["player_2_columns"]
            )

            if not move_successful:
                continue

            if game["current_player"] == 1:
                current_board = game["player_1_columns"]
            else:
                current_board = game["player_2_columns"]

            if mechanics.full_board(current_board):

                if not game["winner_printed"]:
                    print_winner(
                        game["player_1_columns"],
                        game["player_2_columns"]
                    )

                    game["winner_printed"] = True

                game_state = "game_over"
                continue

            # Zmiana aktywnego gracza
            if game["current_player"] == 1:
                game["current_player"] = 2
            else:
                game["current_player"] = 1

            game["current_pips"] = mechanics.roll_die()
            game["displayed_pips"] = random.randint(1, 6)

            game["rolling"] = True

            game["roll_start_time"] = (
                pygame.time.get_ticks()
            )

            game["last_roll_frame_time"] = game[
                "roll_start_time"
            ]

        # RYSOWANIE MENU
        if game_state in ("menu", "rules"):

            play_rect, rules_rect = draw_menu(
                screen,
                graphics,
                title_font,
                MENU_TITLE_Y,
                big_button_font,
                small_button_font,
                footer_font,
                MENU_DICE_Y
            )

            if game_state == "rules":
                close_rules_rect = draw_rules_window(
                    screen,
                    graphics,
                    rules_title_font,
                    rules_text_font,
                    rules_fun_font
                )

        # RYSOWANIE GRY ORAZ GAME OVER
        else:
            screen.blit(
                graphics["background"],
                (0, 0)
            )

            draw_game(
                screen,
                graphics,
                label_font,
                score_font,
                game["player_1_columns"],
                game["player_2_columns"],
                game["current_player"],
                game["displayed_pips"]
            )

            if game_state == "game_over":
                retry_rect = draw_game_over_overlay(
                    screen,
                    graphics,
                    winner_font,
                    final_score_font,
                    small_button_font,
                    game["player_1_columns"],
                    game["player_2_columns"]
                )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run_frontend()