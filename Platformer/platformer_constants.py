import pygame

pygame.mixer.pre_init(44100, -16, 2, 1)
pygame.init()
pygame.mixer.set_num_channels(64)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
light_blue = (173, 216, 230)
pink = (150, 0, 0)

vel = 2
fps = 60
tile_size = 16

window_size = (600, 400)
screen = pygame.display.set_mode(window_size)
display = pygame.Surface((300, 200))
pygame.display.set_caption('Platformer')

grass_img = pygame.image.load('data/images/grass.png')
dirt_img = pygame.image.load('data/images/dirt.png')
plant_img = pygame.image.load('data/images/plant.png').convert()
plant_img.set_colorkey(white)

tile_index = {1: grass_img, 2: dirt_img, 3: plant_img}

jumper_img = pygame.image.load('data/images/jumper.png').convert()
jumper_img.set_colorkey(white)

jump_sound = pygame.mixer.Sound('data/audio/jump.wav')
grass_sounds = [pygame.mixer.Sound('data/audio/grass_0.wav'),
                pygame.mixer.Sound('data/audio/grass_1.wav')]
grass_sounds[0].set_volume(0.2)
grass_sounds[1].set_volume(0.2)

pygame.mixer.music.load('data/audio/music.wav')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

grass_sound_timer = 0

background_objects = [[0.25, [120, 10, 70, 400]], [0.25, [280, 30, 40, 400]],
                      [0.5, [30, 40, 40, 400]], [0.5, [130, 90, 100, 400]], [0.5, [300, 80, 120, 400]]]

chunk_size = 8

real_scroll = [0, 0]
player_y_momentum = 0
air_timer = 0

moving_right = False
moving_left = False
jump = False

run = True
clock = pygame.time.Clock()
game_map = {}

jumper_objects = []
