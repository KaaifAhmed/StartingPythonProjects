import pygame as pg
import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import sys
import random

pg.font.init()

'''Constants'''


# IMAGES
RED_SPACESHIP_IMAGE = pg.image.load(os.path.join('Assets', 'spaceship_red.png'))
YELLOW_SPACESHIP_IMAGE = pg.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
BACKGROUND = pg.image.load(os.path.join('Assets', 'space.png'))
SPACE = pg.transform.scale(pg.image.load(os.path.join('Assets', 'space.png')), (900, 500))

# User Events
YELLOW_HIT = pg.USEREVENT + 1
RED_HIT = pg.USEREVENT + 2

# Width, Height
WIDTH, HEIGHT = 900, 500
SS_WIDTH, SS_HEIGHT = 55, 40
FPS = 60

# Fonts
HEALTH_FONT = pg.font.SysFont('consolas', 30)
WINNER_FONT = pg.font.SysFont('consolas', 100)

# Displays
BORDER = pg.Rect(WIDTH//2 - 4, 0, 8, HEIGHT)
WIN = pg.display.set_mode((WIDTH, HEIGHT))

# Velocities
VEL = 5
BULLET_VEL = 10
NUM_BULLETS = 3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# SpaceShips
YELLOW_SPACESHIP = pg.transform.rotate(
    pg.transform.scale(YELLOW_SPACESHIP_IMAGE, (SS_WIDTH, SS_HEIGHT)), 90)
RED_SPACESHIP = pg.transform.rotate(
    pg.transform.scale(RED_SPACESHIP_IMAGE, (SS_WIDTH, SS_HEIGHT)), 270)

# Hand Detection
detector = HandDetector(detectionCon=0.7, maxHands=1)
capture = cv2.VideoCapture(0)

fire_bullet = False

'''Functions'''


# Updating the display
def update():
    pg.display.update()


# Handling movements of yellow spaceship
def yellow_movement(direct, yellow):
     yellow.x = direct[0]
     yellow.y = direct[1]

    # if k_prs[pg.K_a] and yellow.x - VEL > 0:  # LEFT
    #     yellow.x -= VEL
    # if k_prs[pg.K_d] and yellow.x + VEL < BORDER.x - yellow.width + 14:  # RIGHT
    #     yellow.x += VEL
    # if k_prs[pg.K_w] and yellow.y - VEL > 0:  # UP
    #     yellow.y -= VEL
    # if k_prs[pg.K_s] and yellow.y + VEL < HEIGHT - SS_HEIGHT - 15:  # DOWN
    #     yellow.y += VEL


# Handling movements of the bullet
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pg.event.post(pg.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pg.event.post(pg.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


# Displaying winner text
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, True, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    update()
    pg.time.delay(3000)


# Displaying the main window and all of its components
def draw_window(red, yellow, yellow_bullets, red_bullets, r_health, y_health):
    WIN.blit(SPACE, (0, 0))
    pg.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render("Health : " + str(r_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health : " + str(y_health), True, WHITE)
    WIN.blit(red_health_text, ((WIDTH - red_health_text.get_width() - 10), 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pg.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pg.draw.rect(WIN, YELLOW, bullet)
    update()


def computer_movement(yellow, red, bullets):
    global fire_bullet
    if random.randint(1, 2) == 2:
        if yellow.y < red.y:
            red.y -= VEL
        if yellow.y > red.y:
            red.y += VEL

    for bullet in bullets:
        if red.x == bullet.x + 20:
            if bullet.y in range(red.y, red.height):
                if random.randint(0, 2) == 1:
                    red.y -= VEL

    if random.randint(0, 2) == 1:
        fire_bullet = True
    else:
        fire_bullet = False


def direction(hand):
    if hand:
        return hand[0]['center']
    else:
        return [100, 100]


# Main game loop
def main():

    red = pg.Rect(750, 250, SS_WIDTH, SS_HEIGHT)
    yellow = pg.Rect(100, 100, SS_WIDTH, SS_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pg.time.Clock()
    run = True

    comp_fire = False

    while run:
        success, image = capture.read()
        hands = detector.findHands(image, draw=False)

        if hands:
            hand_pos = detector.fingersUp(hands[0])
            if hand_pos == [0, 0, 0, 0, 0] and len(yellow_bullets) < NUM_BULLETS:
                bullet = pg.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 3, 10, 5)
                yellow_bullets.append(bullet)
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit(0)

            if fire_bullet is True and len(red_bullets) < NUM_BULLETS:
                bullet = pg.Rect(red.x - red.width, red.y + red.height//2 + 3, 10, 5)
                red_bullets.append(bullet)

            if comp_fire and len(red_bullets) < NUM_BULLETS:
                bullet = pg.Rect(red.x, red.y + red.height//2 + 3, 10, 5)
                red_bullets.append(bullet)

            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins!"
        if yellow_health <= 0:
            winner_text = "Red wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        directions = direction(hands)
        yellow_movement(directions, yellow)
        computer_movement(yellow, red, yellow_bullets)
        # red_movement(directions, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, yellow_bullets, red_bullets, red_health, yellow_health)

        # cv2.imshow('Hand Detection', image)
        # cv2.waitKey(1)

    main()


# Checking if the file is opened directly
if __name__ == "__main__":
    main()
