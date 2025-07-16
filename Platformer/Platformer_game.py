import sys
import random
from data.engine import generate_chunks, load_animations, Entity
from platformer_constants import *


load_animations('Platformer/data/images/entities/')
player = Entity(50, 70, 5, 13, 'player')


class JumperEntity:
    def __init__(self, loc):
        self.loc = loc

    def render(self, surface, scrol):
        surface.blit(jumper_img, (self.loc[0] - scrol[0], self.loc[1] - scrol[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 8, 9)

    def collision_test(self, rect):
        jumper_rect = self.get_rect()
        return jumper_rect.colliderect(rect)


for i in range(5):
    jumper_objects.append(JumperEntity((random.randint(0, 600) - 300, 50)))


while run:
    display.fill(light_blue)
    if grass_sound_timer > 0:
        grass_sound_timer -= 1

    real_scroll[0] += (player.x - real_scroll[0] - 152)/20
    real_scroll[1] += (player.y - real_scroll[1] - 106)/20
    scroll = real_scroll.copy()
    scroll[0], scroll[1] = int(real_scroll[0]), int(real_scroll[1])

    for background_obj in background_objects:
        obj_rect = pygame.Rect(background_obj[1][0] - scroll[0] * background_obj[0],
                               background_obj[1][1] - scroll[1] * background_obj[0],
                               background_obj[1][2], background_obj[1][3])
        if background_obj[0] == 0.5:
            pygame.draw.rect(display, (14, 222, 150), obj_rect)
        if background_obj[0] == 0.25:
            pygame.draw.rect(display, (9, 91, 85), obj_rect)

    tiles = []
    for chunk_a in range(4):
        for chunk_b in range(5):
            target_x = chunk_a - 1 + int(round(scroll[0]/(chunk_size * 16)))
            target_y = chunk_b - 1 + int(round(scroll[1] / (chunk_size * 16)))
            target_chunk = str(target_x) + ';' + str(target_y)
            if target_chunk not in game_map:
                game_map[target_chunk] = generate_chunks(target_x, target_y)
            for tile in game_map[target_chunk]:
                display.blit(tile_index[tile[1]], (tile[0][0] * tile_size - scroll[0],
                                                   tile[0][1] * tile_size - scroll[1]))
                if tile[1] in [1, 2]:
                    tiles.append(pygame.Rect(tile[0][0] * tile_size, tile[0][1] * tile_size, tile_size, tile_size))

    player.change_frame(1)
    player.display(display, scroll)

    for jumper in jumper_objects:
        jumper.render(display, scroll)
        if jumper.collision_test(player.obj.rect):
            player_y_momentum = -6

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_SPACE:
                if air_timer < 6:
                    player_y_momentum = -5
                    jump_sound.play()
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False

    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += vel
    if moving_left:
        player_movement[0] -= vel

    if player_movement[0] > 0:
        player.set_action('run')
        player.set_flip(False)
    if player_movement[0] == 0:
        player.set_action('idle')
    if player_movement[0] < 0:
        player.set_action('run')
        player.set_flip(True)

    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum = 3

    collision_types = player.move(player_movement, tiles)

    if collision_types['bottom']:
        player_y_momentum = 0
        air_timer = 0
        if player_movement[0] != 0:
            if grass_sound_timer == 0:
                grass_sound_timer = 30
                random.choice(grass_sounds).play()

    else:
        air_timer += 1
    if collision_types['top']:
        player_y_momentum = 0

    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(fps)
