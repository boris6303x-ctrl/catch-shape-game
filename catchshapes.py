import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("CatchShapes")

BASKET_POS = [200, 350]
WHITE = "#ffffff"
BROWN = "#946f53"
score = 0
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
                elif event.key == pygame.K_ESCAPE:
                    engine = False

        
        screen.fill(WHITE)
        # print(colour)
        
        if shapetype == 1:
            pygame.draw.rect(screen, colour, [x, y, 20, 20])
        if shapetype == 2:
            pygame.draw.circle(screen, colour, [x, y], 10)
        if shapetype == 3:
            pygame.draw.rect(screen, colour, [x, y, 20, 10])
        if shapetype == 4:
            pygame.draw.polygon(screen, colour, [(0+x, 20+y), (10+x, 0+y), (20+x, 20+y)])

        pygame.draw.rect(screen, BROWN, [BASKET_POS[0], BASKET_POS[1], 100, 50])
        y += 1
        if y >= 400 or (y == BASKET_POS[1] and x == BASKET_POS[0]):
            if y == BASKET_POS[1] and x == BASKET_POS[0]:
                score += 1
            x = random.randint(0, 400)
            y = 0
            break
        pygame.display.flip()
        clock.tick(60)


pygame.quit()
sys.exit()