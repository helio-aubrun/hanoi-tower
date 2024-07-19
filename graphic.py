import pygame
import time
from solve import hanoi

# Initialize Pygame
pygame.init()

# Set up window
window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Hanoi Tower")

# Define colors
white = (220, 220, 220)
back = (52, 188, 176)
disc_colors = [(185, 185, 190), (148, 148, 152), (111, 111, 114), (74, 74, 76), (55, 55, 60)]

# Peg and disc properties
leg_width, leg_height = 20, 250
gap = 150
disc_height = 20

# Calculate peg positions
left_leg_x = window_width / 2 - gap - leg_width
middle_leg_x = left_leg_x + gap + leg_width
right_leg_x = middle_leg_x + gap + leg_width
leg_y = window_height - leg_height - 200

# Initial game state
num_discs = 5
pegs = [list(range(num_discs, 0, -1)), [], []]

def draw_scene():
    screen.fill(back)
    # Draw pegs
    for x in (left_leg_x, middle_leg_x, right_leg_x):
        pygame.draw.rect(screen, white, (x, leg_y, leg_width, leg_height))
    pygame.draw.rect(screen, white, (0, leg_y + leg_height, window_width, leg_width))
    # Draw discs
    for peg_index, peg in enumerate(pegs):
        for disc_index, disc_size in enumerate(peg):
            disc_width = disc_size * 30
            peg_x = [left_leg_x, middle_leg_x, right_leg_x][peg_index]
            disc_x = peg_x + leg_width // 2 - disc_width // 2
            disc_y = leg_y + leg_height - (disc_index + 1) * disc_height
            pygame.draw.rect(screen, disc_colors[disc_size - 1], (disc_x, disc_y, disc_width, disc_height))
    pygame.display.flip()

def move_disc(from_peg, to_peg):
    pegs[to_peg - 1].append(pegs[from_peg - 1].pop())
    draw_scene()
    time.sleep(0.5)

def play_moves(moves):
    for move in moves:
        move_disc(*move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    solve =hanoi()
    solve.main(num_discs)
    moves = solve.path

    draw_scene()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time.sleep(1)
        play_moves(moves)
        running = False  # Stop after playing moves

    pygame.quit()
