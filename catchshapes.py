import pygame
import random
import sys


pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("CatchShapes")

BASKET_POS = [200, 350]
WHITE = "#ffffff"
BROWN = "#946f53"
RED = "#ff0000"
BLACK = "#000000"
score = 0
shapes_on_ground = 0
game_over = False
speed_increment = 1
monospace = pygame.font.SysFont("Consolas", 20)
monospace_bold = pygame.font.SysFont("Consolas", 24, bold=True)
monospace_small = pygame.font.SysFont("Consolas", 16)
x1 = random.randint(0, 400)
x2 = random.randint(0, 400)
x3 = random.randint(0, 400)
y1 = 0
y2 = 0
y3 = 0

shape2_appeared = random.choice([True, False])
shape3_appeared = random.choice([True, False]) if shape2_appeared else False

def count_shapes():
    shape_amount = 1
    if shape2_appeared:
        shape_amount += 1
    if shape3_appeared:
        shape_amount += 1
    return shape_amount

engine = True
clock = pygame.time.Clock()

while engine:
    shapetype1 = random.randint(1, 4)
    shapetype2 = random.randint(1, 4)
    shapetype3 = random.randint(1, 4)
    colour = list(str(hex(random.randint(0x000000, 0xffffff))).replace("0x", "#"))
    if len(colour) < 7:
        colour.insert(1, "0"*(7-len(colour)))
    colour = ''.join(colour)
    shape_amount = count_shapes()
    
    while engine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    BASKET_POS[0] -= 20
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_e:
                    BASKET_POS[0] += 20
                elif (event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS) and speed_increment != 20:
                    while True:
                        speed_increment += 1
                        if 200 % speed_increment == 0:
                            break
                elif (event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE) and speed_increment != 1:
                    while True:
                        speed_increment -= 1
                        if 200 % speed_increment == 0:
                            break
                elif event.key == pygame.K_SPACE and game_over == True:
                    score = 0
                    shapes_on_ground = 0
                    speed_increment = 1
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    engine = False

        
        screen.fill(WHITE)
        # print(colour)
        
        if game_over:
            screen.blit(monospace_bold.render("GAME OVER", True, RED), (135, 100))
            screen.blit(monospace.render(f"Score: {score}", True, BLACK), (135, 150))
            screen.blit(monospace_small.render("Press SPACE to try again\nOr press ESCAPE or close the window to quit", True, BLACK))
        else:
            if shapetype1 == 1:
                pygame.draw.rect(screen, colour, [x1, y1, 20, 20])
            if shapetype1 == 2:
                pygame.draw.circle(screen, colour, [x1, y1], 10)
            if shapetype1 == 3:
                pygame.draw.rect(screen, colour, [x1, y1, 20, 10])
            if shapetype1 == 4:
                pygame.draw.polygon(screen, colour, [(0+x1, 20+y1), (10+x1, 0+y1), (20+x1, 20+y1)])
            if shape_amount == 2:
                if shapetype2 == 1:
                    pygame.draw.rect(screen, colour, [x2, y2, 20, 20])
                if shapetype2 == 2:
                    pygame.draw.circle(screen, colour, [x2, y2], 10)
                if shapetype2 == 3:
                    pygame.draw.rect(screen, colour, [x2, y2, 20, 10])
                if shapetype2 == 4:
                    pygame.draw.polygon(screen, colour, [(0+x2, 20+y2), (10+x2, 0+y2), (20+x2, 20+y2)])
            if shape_amount == 3:
                if shapetype2 == 1:
                    pygame.draw.rect(screen, colour, [x2, y2, 20, 20])
                if shapetype2 == 2:
                    pygame.draw.circle(screen, colour, [x2, y2], 10)
                if shapetype2 == 3:
                    pygame.draw.rect(screen, colour, [x2, y2, 20, 10])
                if shapetype2 == 4:
                    pygame.draw.polygon(screen, colour, [(0+x2, 20+y2), (10+x2, 0+y2), (20+x2, 20+y2)])
                
                if shapetype3 == 1:
                    pygame.draw.rect(screen, colour, [x3, y3, 20, 20])
                if shapetype3 == 2:
                    pygame.draw.circle(screen, colour, [x3, y3], 10)
                if shapetype3 == 3:
                    pygame.draw.rect(screen, colour, [x3, y3, 20, 10])
                if shapetype3 == 4:
                    pygame.draw.polygon(screen, colour, [(0+x3, 20+y3), (10+x3, 0+y3), (20+x3, 20+y3)])

            pygame.draw.rect(screen, BROWN, [BASKET_POS[0], BASKET_POS[1], 100, 50])
            
            y1 += speed_increment
            if shape_amount == 2:
                y2 += speed_increment
            if shape_amount == 3:
                y2 += speed_increment
                y3 += speed_increment
            
            if y1 >= 400 or ((y1 == BASKET_POS[1]) and (BASKET_POS[0]-50 <= x1 <= BASKET_POS[0]+50)):
                if (y1 == BASKET_POS[1]) and (BASKET_POS[0]-50 <= x1 <= BASKET_POS[0]+50):
                    score += 1
                else:
                    shapes_on_ground += 1
                
                x1 = random.randint(0, 400)
                x2 = random.randint(0, 400)
                x3 = random.randint(0, 400)
                y1 = 0
                y2 = 0
                y3 = 0
                if shape_amount == 1:
                    break
                else:
                    shape_amount -= 1

            screen.blit(monospace_small.render(f"Score: {score}\nSpeed: {speed_increment}", True, BLACK))
        
        pygame.display.flip()
        clock.tick(60)
        if shapes_on_ground == 5:
            game_over = True

pygame.quit()
sys.exit()