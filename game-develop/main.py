# Section 01: Pre-Game Setup
import pygame

pygame.init()

monitor_display = (800,600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_tank_svg = pygame.image.load("tank.svg")

game_tank_sprite = pygame.transform.scale(game_tank_svg, (75,75))

# Section 02: Game Properties
game_properties ={
    "sky": {
        "color": (135, 205, 235)
    },
    "grass": {
        "color" : (0, 255, 0),
        "position": {
            "y": 0.8 * monitor_display[1]
        }
    },
    "player":{
        "name": "Player",
        "position": {
            "x": 0.2 * monitor_display[0]
        },
        "hp": 1
    },
    "computer": {
        "name": "CPU",
        "position": {
            "x": 0.8 * monitor_display[0] - game_tank_sprite.get_width()
        },
        "hp": 1
    }
}

# Section 03: Health bar logic
def display_hp(tank_property, offset_left):
    offset = {
        "left": offset_left * monitor_display[0],
        "top": 0.05 * monitor_display[1]
    }
    
    size = {
        "width": 0.5 * monitor_display[0],
        "height": 25
    }
    
    
    pygame.draw.rect(game_display, (127, 127, 127), pygame.Rect(offset["left"]+0.1 * size ["width"], offset["top"], 0.8 * size ["width"], size["height"]))

    name_text_surface = pygame.font.SysFont("arial", 20).render(tank_property["name"], True, (255, 255, 255))
    
    name_text_rect = name_text_surface.get_rect(topleft = (offset["left"] + 0.1 * size ["width"], offset["top"]))
    
    game_display.blit(name_text_surface, name_text_rect)
    
    pygame.draw.rect(game_display, (255, 255, 255), pygame.Rect(offset["left"] + 0.25 * size["width"], offset["top"] + 0.2 * size["height"], 0.5 * size["width"] * tank_property["hp"], 0.6 * size["height"]))
    
    hp_percentage = round(tank_property["hp"] * 100)
    
    hp_text_surface = pygame.font.SysFont("arial", 20).render(f"{hp_percentage}%", True, (255, 255, 255))
    
    hp_text_rect = hp_text_surface.get_rect(topleft = (offset["left"] + 0.75 * size ["width"], offset["top"]))
    
    game_display.blit(hp_text_surface, hp_text_rect)

# Section 04: Projectile shooting logic

# Section 05: Computer controls logic

# Section 06: Game Logic:
game_running_flag = True

while game_running_flag:
    # Section 06A: Stopping the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running_flag = False

    if not game_running_flag:
        pygame.quit()

        break
    
    # Section 06B: Detecting key presses and movements
    key_pressed = pygame.key.get_pressed()

    position_delta = 0

    if key_pressed[pygame.K_LEFT]:
        position_delta = -1
    elif key_pressed[pygame.K_RIGHT]:
        position_delta = 1 

    if 0 <= game_properties["player"]["position"]["x"] + position_delta and game_properties["player"]["position"]["x"] + position_delta + game_tank_sprite.get_width() <= game_properties["computer"]["position"]["x"]:
        game_properties["player"]["position"]["x"] += position_delta

    # Section 06C: Background graphics rendering
    game_display.fill(game_properties["sky"]["color"])

    pygame.draw.rect(game_display, game_properties["grass"]["color"], pygame.Rect(0, game_properties["grass"]["position"]["y"], monitor_display[0], monitor_display[1] - game_properties["grass"]["position"]["y"]))
# Section 06D: Player graphics rendering
    game_tank_sprite_player = game_tank_sprite

    game_display.blit(game_tank_sprite_player, (game_properties["player"]["position"]["x"], game_properties["grass"]["position"]["y"] - game_tank_sprite.get_height()))

# Section 06E: Computer graphics rendering 
    game_tank_sprite_computer = pygame.transform.flip(game_tank_sprite, True, False)

    game_display.blit(game_tank_sprite_computer, (game_properties["computer"]["position"]["x"], game_properties["grass"]["position"]["y"] - game_tank_sprite.get_height()))

    # Section 06D: Player graphics rendering
    game_tank_sprite_player = game_tank_sprite

    game_display.blit(game_tank_sprite_player, (game_properties["player"]["position"]["x"], game_properties["grass"]["position"]["y"] - game_tank_sprite.get_height()))

    # Section 06E: Computer graphics rendering
    game_tank_sprite_computer = pygame.transform.flip(game_tank_sprite, True, False)

    game_display.blit(game_tank_sprite_computer, (game_properties["computer"]["position"]["x"], game_properties["grass"]["position"]["y"] - game_tank_sprite.get_height()))

    # Section 06F: Health bar rendering
    display_hp(game_properties["player"],0)
    display_hp(game_properties["computer"],0.5)
    # Section 06G: Refreshing game graphics
    pygame.display.update()

    system_clock.tick(30)