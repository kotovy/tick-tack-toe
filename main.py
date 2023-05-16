import pygame
pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('tic-tac-toe')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CELL_SIZE = 100
GRID_SIZE = 3

EMPTY = 0
CROSS = 1
NOUGHT = 2

board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

current_player = CROSS

game_over = False


def draw_grid():
    for x in range(GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, GRID_SIZE * CELL_SIZE))
        pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), (GRID_SIZE * CELL_SIZE, x * CELL_SIZE))

def draw_shape(row, col):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2

    if board[row][col] == CROSS:
        pygame.draw.line(screen, BLACK, (x - 30, y - 30), (x + 30, y + 30), 3)
        pygame.draw.line(screen, BLACK, (x + 30, y - 30), (x - 30, y + 30), 3)
    elif board[row][col] == NOUGHT:
        pygame.draw.circle(screen, BLACK, (x, y), 30, 3)

def update_game_state(row, col):
    if board[row][col] == EMPTY:
        board[row][col] = current_player
        check_winner()
        switch_players()

def check_winner():
    global game_over

    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            game_over = True

    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            game_over = True

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        game_over = True

def switch_players():
    global current_player
    if current_player == CROSS:
        current_player = NOUGHT
    else:
        current_player = CROSS
        
def display_result(player):
    if player == CROSS:
        message = "Crosses won!"
    else:
        message = "Toe wins!"

    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(150, 150))
    screen.blit(text, text_rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            clicked_row = mouse_pos[1] // CELL_SIZE
            clicked_col = mouse_pos[0] // CELL_SIZE
            update_game_state(clicked_row, clicked_col)

    screen.fill(WHITE)
    draw_grid()

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            draw_shape(row, col)

    if game_over:
        screen.fill(WHITE)  
        display_result(current_player)

    pygame.display.flip()


pygame.quit()



