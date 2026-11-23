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
x = random.randint(0, 400)
y = 0

engine = True
clock = pygame.time.Clock()

while engine:
    shapetype = random.randint(1, 4)
    colour = list(str(hex(random.randint(0x000000, 0xffffff))).replace("0x", "#"))
    if len(colour) < 7:
        colour.insert(1, "0"*(7-len(colour)))
    colour = ''.join(colour)
    
    while engine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    BASKET_POS[0] -= 10
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_e:
                    BASKET_POS[0] += 10
                elif (event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS) and speed_increment != 20:
                    while True:
                        speed_increment += 1
                        if 400 % speed_increment == 0:
                            break
                elif (event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE) and speed_increment != 1:
                    while True:
                        speed_increment -= 1
                        if 400 % speed_increment == 0:
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
            if shapetype == 1:
                pygame.draw.rect(screen, colour, [x, y, 20, 20])
            if shapetype == 2:
                pygame.draw.circle(screen, colour, [x, y], 10)
            if shapetype == 3:
                pygame.draw.rect(screen, colour, [x, y, 20, 10])
            if shapetype == 4:
                pygame.draw.polygon(screen, colour, [(0+x, 20+y), (10+x, 0+y), (20+x, 20+y)])

            pygame.draw.rect(screen, BROWN, [BASKET_POS[0], BASKET_POS[1], 100, 50])
            
            y += speed_increment
            if y >= 400 or ((y == BASKET_POS[1]) and (BASKET_POS[0]-50 <= x <= BASKET_POS[0]+50)):
                if (y == BASKET_POS[1]) and (BASKET_POS[0]-50 <= x <= BASKET_POS[0]+50):
                    score += 1
                else:
                    shapes_on_ground += 1
                
                x = random.randint(0, 400)
                y = 0
                break

            screen.blit(monospace_small.render(f"Score: {score}\nSpeed: {speed_increment}", True, BLACK))
        
        pygame.display.flip()
        clock.tick(60)
        if shapes_on_ground == 5:
            game_over = True

pygame.quit()
sys.exit()