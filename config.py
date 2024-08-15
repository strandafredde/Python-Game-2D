import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to assets
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
GUI_DIR = os.path.join(ASSETS_DIR, 'gui')
SCENES_DIR = os.path.join(BASE_DIR, 'scenes')
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
BASE_MAP_DIR = os.path.join(SCENES_DIR, 'base_map')
MAIN_MAP_PATH = os.path.join(BASE_MAP_DIR, 'main_map.tmx')
NPC_DIR = os.path.join(ASSETS_DIR, 'npc')

# File paths
TEXT_BOX_PATH = os.path.join(GUI_DIR, 'text_box.png')
START_IMG_PATH = os.path.join(SCENES_DIR, 'start_screen2.png')
CONTROLS_IMG_PATH = os.path.join(SCENES_DIR, 'controls_screen.png')
CONTROL_IMG_PAUSE_PATH = os.path.join('assets', 'gui', 'control_pause.png')
SCOREBOARD_FILE_PATH = os.path.join(ASSETS_DIR, 'scoreboard.txt')
FONT_PATH = os.path.join(FONTS_DIR, 'PressStart2P.ttf')
FLY_DYING_SOUND = os.path.join(SOUNDS_DIR, 'fly_dying.wav')
HURT_SOUND = os.path.join(SOUNDS_DIR, 'hurt.wav')
ARTHUR_IMAGE = os.path.join(NPC_DIR, 'arthur.png')
TEXT_BOX_IMAGE = os.path.join(GUI_DIR, 'text_box.png')
TEXT_BOX_IMAGE = os.path.join(GUI_DIR, 'text_box.png')
SHOP_MENU_IMAGE = os.path.join(GUI_DIR, 'shop_menu2.png')
MERCHANT_IMAGE = os.path.join(NPC_DIR, 'merchant.png')
WALTER_IMAGE = os.path.join(NPC_DIR, 'walter.png')
TEXT_BOX_IMAGE = os.path.join(GUI_DIR, 'text_box.png')
FLY_SPRITESHEET = os.path.join(NPC_DIR, 'fly.png')
# Player sprite paths
MAIN_CHAR_DEFAULT_PATH = os.path.join(ASSETS_DIR, 'player', 'main_char_default.png')
SWORD_WALK_PATH = os.path.join(ASSETS_DIR, 'player', 'sword', 'main_character_sword_walk.png')
SWORD_IDLE_PATH = os.path.join(ASSETS_DIR, 'player', 'sword', 'main_character_sword_idle.png')
SWORD_SLASH_PATH = os.path.join(ASSETS_DIR, 'player', 'sword', 'main_character_sword_slash.png')
COIN_IMAGE_PATH = os.path.join(ASSETS_DIR, 'items', 'coin.png')

# Sound paths
DOOR_OPEN_SOUND = os.path.join(SOUNDS_DIR, 'door_open.wav')
TOWN_MUSIC = os.path.join(SOUNDS_DIR, 'town-2.wav')
SWORD_SWING_SOUND = os.path.join(SOUNDS_DIR, 'sword_swing.wav')
COIN_PICKUP_SOUND = os.path.join(SOUNDS_DIR, 'coin_pickup.wav')
TALK_SOUND = os.path.join(SOUNDS_DIR, 'talk.wav')
PICK_UP_SOUND = os.path.join(SOUNDS_DIR, 'pick_up.wav')
SCROLL_SOUND = os.path.join(SOUNDS_DIR, 'scroll.wav')
SELECT_SOUND = os.path.join(SOUNDS_DIR, 'select2.wav')
START_SCREEN_MUSIC = os.path.join(SOUNDS_DIR, 'start_screen_music.wav')
TALK_SOUND = os.path.join(SOUNDS_DIR, 'talk.wav')
SELECT_SOUND = os.path.join(SOUNDS_DIR, 'select.wav')
BUYING_SOUND = os.path.join(SOUNDS_DIR, 'buying_sound.wav')
TALK_SOUND = os.path.join(SOUNDS_DIR, 'talk.wav')
HIT_HURT_FLY_PATH = os.path.join(SOUNDS_DIR, 'hit_hurt_fly.wav')
POTION_SOUND_PATH = os.path.join(SOUNDS_DIR, 'potion_sound.wav')

# Prices
TACO_PRICE = 10
FLOUR_PRICE = 5
GAS_MASK_PRICE = 10
HP_POTION_PRICE = 2

# Button sizes
BUTTON_WIDTH = 560
BUTTON_HEIGHT = 50

TEXT_BOX_WIDTH_RATIO = 3 / 5
TEXT_BOX_HEIGHT = 100

