import pygame

def load_spritesheet(path, sprite_width, sprite_height, row=0, scale=1):
    sprites = []  # List to hold the individual sprites

    try:
        spritesheet = pygame.image.load(path).convert_alpha()  # Load the spritesheet

        for x in range(spritesheet.get_width() // sprite_width):
            rect = pygame.Rect(x * sprite_width, row * sprite_height, sprite_width, sprite_height)  # Create a rect for the current sprite
            sprite = spritesheet.subsurface(rect)  # Get the sprite from the spritesheet
            sprite = pygame.transform.scale(sprite, (sprite_width * scale, sprite_height * scale))  # Scale the sprite
            sprites.append(sprite)  # Add the sprite to the list

    except pygame.error as e:
        print(f"Error loading spritesheet: {e}")

    return sprites