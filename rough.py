import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
LIGHT_BLACK = (100, 100, 100)
RED = (255, 0, 0)
# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
pygame.display.flip()