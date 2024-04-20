import pygame
import sys
import win32gui
import win32con


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def draw_board(screen, n):
    block_size = SCREEN_WIDTH // n
    for row in range(n):
        for col in range(n):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, [col * block_size, row * block_size, block_size, block_size])

def draw_queens(screen, queens, n):
    block_size = SCREEN_WIDTH // n
    for row, col in enumerate(queens):
        pygame.draw.circle(screen, RED, (col * block_size + block_size // 2, row * block_size + block_size // 2), block_size // 3)

def visualize_backtracking(screen, n, queens, row):
    draw_board(screen, n)
    for r in range(row):
        pygame.draw.circle(screen, RED, (queens[r] * (SCREEN_WIDTH // n) + (SCREEN_WIDTH // (2 * n)), r * (SCREEN_HEIGHT // n) + (SCREEN_HEIGHT // (2 * n))), (SCREEN_WIDTH // (2 * n)))
    draw_queens(screen, queens, n)
    pygame.display.flip()
    pygame.time.delay(200)  

def place_queens(screen, n, queens, row):
    if row == n:
        return True

    for col in range(n):
        queens[row] = col
        visualize_backtracking(screen, n, queens, row + 1)
        if is_safe(queens, row):
            if place_queens(screen, n, queens, row + 1):
                return True
        queens[row] = -1
    return False

def is_safe(queens, row):
    for i in range(row):
        if queens[i] == queens[row] or abs(queens[i] - queens[row]) == abs(i - row):
            return False
    return True

def visualize_n_queens(n):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(f"{n}-Queens Backtracking Visualization")

    hwnd = win32gui.GetForegroundWindow()

    queens = [-1] * n  

    pygame.display.flip()  

    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    if place_queens(screen, n, queens, 0):
        draw_board(screen, n)
        draw_queens(screen, queens, n)
        pygame.display.flip()
    else:
        print("No solution exists for the given board size.")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
if __name__ == "__main__":
    n = int(input("Enter the size of the board (N x N): "))
    visualize_n_queens(n)
