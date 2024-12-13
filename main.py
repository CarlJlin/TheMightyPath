from player import *
from knight import Knight
from mage import Mage
from rogue import Rogue
import pygame
from config import *
import base64
from math import sqrt

class Particle:
    def __init__(self, x, y, dx, dy, size, image, lifespan):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.image = pygame.transform.scale(image, (size, size))
        self.lifespan = lifespan

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifespan -= 1

    def draw(self, surface, camera_x, camera_y):
        if self.lifespan > 0:
            surface.blit(self.image, (self.x - camera_x, self.y - camera_y))

def get_input(prompt):
    input_box = pygame.Rect(300, 200, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_active
    active = True
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.blit(background_image, (0, 0))  # Draw background image
        draw_text(prompt, font, BLACK, screen, 300, 150)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

    return text

def choose_option(prompt, options):
    selected = 0
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)

        screen.blit(background_image, (0, 0))  # Draw background image
        draw_text(prompt, font, BLACK, screen, 300, 150)
        for i, option in enumerate(options):
            color = BLACK if i == selected else pygame.Color('gray')
            draw_text(option, font, color, screen, 300, 200 + i * 40)
        pygame.display.flip()

    return options[selected]

def main_menu():
    options = ["Start Game", "Load Game", "Options", "Quit"]
    selected = 0
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if options[selected] == "Start Game":
                        game()
                    elif options[selected] == "Load Game":
                        player1 = load_game()
                        if player1:
                            game(player1)
                    elif options[selected] == "Options":
                        print('options')
                    elif options[selected] == "Quit":
                        pygame.quit()
                        exit()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        draw_text("Main Menu", font, WHITE, screen, 300, 100)
        for i, option in enumerate(options):
            color = WHITE if i == selected else pygame.Color('BLACK')
            draw_text(option, font, color, screen, 300, 200 + i * 40)
        pygame.display.flip()

def game(player1=None):
    if not player1:
        player_name = get_input("Enter your name:")
        player_surname = get_input("Enter your surname:")
        player_class = choose_option("Choose your class:", ["Knight", "Mage", "Rogue"])
        difficulty = choose_option("Choose difficulty:", ["1 (Easy)", "2 (Medium)", "3 (Hard)"])

        player1 = Player(player_name, player_surname)
        if player_class.lower() == 'knight':
            player1.character = Knight(player_name, player_surname)
        elif player_class.lower() == 'mage':
            player1.character = Mage(player_name, player_surname)
        elif player_class.lower() == 'rogue':
            player1.character = Rogue(player_name, player_surname)

        if difficulty.startswith("1"):
            player1.difficulty = DifficultyLevel.EASY
        elif difficulty.startswith("2"):
            player1.difficulty = DifficultyLevel.MEDIUM
        elif difficulty.startswith("3"):
            player1.difficulty = DifficultyLevel.HARD

    particle = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1
        if keys[pygame.K_ESCAPE]:
            escape_menu(player1)

        if dx != 0 and dy != 0:
            dx *= 1/sqrt(2)
            dy *= 1/sqrt(2)

        player_rect.x += dx
        player_rect.y += dy

        camera_x = player_rect.x - SCREEN_WIDTH // 2
        camera_y = player_rect.y - SCREEN_HEIGHT // 2

        if (dx != 0 or dy != 0) and (particle is None or particle.lifespan <= 0):
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                particle = Particle(
                    player_rect.x - player_rect.width // 2,
                    player_rect.y + player_rect.height // 2,
                    -dx * 2, -dy * 2,
                    player_rect.width // 2,
                    particle_image,
                    20
                )
            elif keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_a]:
                particle = Particle(
                    player_rect.x + player_rect.width,
                    player_rect.y + player_rect.height // 2,
                    -dx * 2, -dy * 2,
                    player_rect.width // 2,
                    particle_image,
                    20
                )
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                particle = Particle(
                    player_rect.x + player_rect.width // 2,
                    player_rect.y - player_rect.height // 2,
                    -dx * 2, -dy * 2,
                    player_rect.width // 2,
                    particle_image,
                    20
                )
            elif keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_w]:
                particle = Particle(
                    player_rect.x + player_rect.width // 2,
                    player_rect.y + player_rect.height,
                    -dx * 2, -dy * 2,
                    player_rect.width // 2,
                    particle_image,
                    20
                )

        screen.fill(WHITE)

        screen.blit(game_background, (-camera_x, -camera_y))

        if particle:
            particle.update()
            particle.draw(screen, camera_x, camera_y)

        screen.blit(player_image, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()

    pygame.quit()


def save_game(player1):
    data = f"{player1.name},{player1.surname},{player1.character.__class__.__name__},{player1.difficulty.name},{player_rect.x},{player_rect.y}\n"
    encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    with open('save', 'w') as f:
        f.write(encoded_data)


def load_game():
    try:
        with open('save', 'r') as f:
            encoded_data = f.read()
            data = base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')
            name, surname, character_class, difficulty, x, y = data.strip().split(',')
            player1 = Player(name, surname)
            if character_class.lower() == 'knight':
                player1.character = Knight(name, surname)
            elif character_class.lower() == 'mage':
                player1.character = Mage(name, surname)
            elif character_class.lower() == 'rogue':
                player1.character = Rogue(name, surname)
            if difficulty.lower() == 'easy':
                player1.difficulty = DifficultyLevel.EASY
            elif difficulty.lower() == 'medium':
                player1.difficulty = DifficultyLevel.MEDIUM
            elif difficulty.lower() == 'hard':
                player1.difficulty = DifficultyLevel.HARD
            player_rect.x = int(x)
            player_rect.y = int(y)
            return player1
    except FileNotFoundError:
        print("No saved game found")
    except Exception as e:
        print(f"Failed to load game: {e}")
    return None


def escape_menu(player1):
    options = ["Resume", "Save Game", "Main Menu", "Quit"]
    selected = 0
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if options[selected] == "Resume":
                        done = True
                    elif options[selected] == "Save Game":
                        save_game(player1)
                        done = True
                    elif options[selected] == "Main Menu":
                        main_menu()
                        done = True
                    elif options[selected] == "Quit":
                        pygame.quit()
                        exit()
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)

        screen.fill(WHITE)
        draw_text("Pause Menu", font, BLACK, screen, 300, 100)
        for i, option in enumerate(options):
            color = BLACK if i == selected else pygame.Color('gray')
            draw_text(option, font, color, screen, 300, 200 + i * 40)
        pygame.display.flip()

main_menu()