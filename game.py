import sys
import random
import pygame

pygame.init()

width = 800
height = 600
# colors
RED = (229, 22, 12)
BLUE = (12, 12, 255)
YELLOW = (120, 23, 62)
# background color
BG_col = (11, 238, 207)
# player size
player_size = 50
# player position
player_pos = (width / 2, height - 2 * player_size)
# enemy size
enemy_size = 50
# enemy position
enemy_pos = [random.randint(0, width - enemy_size), 0]
enemy_list = [enemy_pos]
# speed
speed = 10
# Score
score = 0

screen = pygame.display.set_mode((width, height))

game_over = False

clock = pygame.time.Clock()

# print the score on screen
myFont = pygame.font.SysFont("monospace", 35)


# Set level
def set_level(scr,spd):
    speed = scr/5+5
    return spd


# Draw enemy
def draw_enemies(enemy_list1):
    for enemy_pos1 in enemy_list1:
        pygame.draw.rect(screen, BLUE, (enemy_pos1[0], enemy_pos1[1], enemy_size, enemy_size))


# Drop Enemy
def drop_enemy(enemy_list1):
    delay = random.random()
    if len(enemy_list1) < 10 and delay < 0.2:
        x_pos = random.randint(0, width - enemy_size)
        y_pos = 0
        enemy_list1.append([x_pos, y_pos])


# Update enemy position
def update_enemy_position(enemy_list1, score=0):
    for idx, enemy_pos1 in enumerate(enemy_list1):
        # Update the enemy position
        if 0 <= enemy_pos1[1] < height:
            enemy_pos1[1] += speed
        else:
            enemy_list1.pop(idx)
            score += 1
    return score


# Collision check
def collision_check(enemy_list1, player_pos1):
    for enemy_pos1 in enemy_list1:
        if detect_collision(player_pos1, enemy_pos1):
            return True
    return False


# function to detect collision
def detect_collision(player_pos1, enemy_pos1):
    p_x = player_pos1[0]
    p_y = player_pos1[1]

    e_x = enemy_pos1[0]
    e_y = enemy_pos1[1]

    if p_x <= e_x < (p_x + player_size) or e_x <= p_x < (e_x + enemy_size):
        if p_y <= e_y < (p_y + player_size) or e_y <= p_y < (e_y + enemy_size):
            return True
    return False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # using movements of left and right key
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x, y]

    screen.fill(BG_col)

    # Drop enemies
    drop_enemy(enemy_list)
    score = update_enemy_position(enemy_list, score)

    speed = set_level(score, speed)

    text = "Score" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (width - 200, height - 40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    # Draw enemy and player
    draw_enemies(enemy_list)
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(20)

    pygame.display.update()

print("Game Over")
print("Your final score is: "+ str(score))