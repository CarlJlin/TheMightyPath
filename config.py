import pygame

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Game")

# Load and scale player sprite
player_image = pygame.image.load('assets/characters/hero/hero_face_unnarmed.png')
player_image = pygame.transform.scale(player_image, (50, 50))  # Resize to 50x50 pixels
player_rect = player_image.get_rect()
player_rect.topleft = (100, 100)

# Load background image
background_image = pygame.image.load('assets/scenes/battleback1.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load particle image
particle_image = pygame.image.load('assets/elements/Nuage.png')
particle_image = pygame.transform.scale(particle_image, (10, 10))  # Resize to 10x10 pixels

# Font
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)