import pygame, sys, time, math

pygame.init()

screen = pygame.display.set_mode((500,600))
pygame.display.set_caption('Đồng hồ đếm ngược!')

GREY = (120,120,120)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

font = pygame.font.SysFont('consolas',30)
textSurface0 = font.render('Start!',True,BLACK)
textSurface1 = font.render('+',True,BLACK)
textSurface2 = font.render('-',True,BLACK)
textSurface3 = font.render('Reset!',True,BLACK)

total_secs = 0
start = False
restart = False

while True:
    screen.fill(GREY)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    pygame.draw.rect(screen, WHITE, (50,50,50,50))
    pygame.draw.rect(screen, WHITE, (50,200,50,50))
    pygame.draw.rect(screen, WHITE, (150,50,50,50))
    pygame.draw.rect(screen, WHITE, (150,200,50,50))
    pygame.draw.rect(screen, WHITE, (320,50,150,50))
    pygame.draw.rect(screen, WHITE, (320,150,150,50))

    pygame.draw.rect(screen, WHITE, (100,500,300,50))
    pygame.draw.rect(screen, BLACK, (100,500,300,50), 5)

    pygame.draw.circle(screen, WHITE, (250,400), 50)
    pygame.draw.circle(screen, BLACK, (250,400), 50, 3)
    pygame.draw.circle(screen, BLACK, (250,400), 2)

    screen.blit(textSurface0, (345,60))
    screen.blit(textSurface1, (67,60))
    screen.blit(textSurface1, (167,60))
    screen.blit(textSurface2, (67,210))
    screen.blit(textSurface2, (167,210))
    screen.blit(textSurface3, (345,160))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (50 < mouse_x < 100) and (50 < mouse_y < 100):
                    total_secs += 60
                if (150 < mouse_x < 200) and (50 < mouse_y < 100):
                    total_secs += 1
                if (50 < mouse_x < 100) and (200 < mouse_y < 250):
                    total_secs -= 60
                if (150 < mouse_x < 200) and (200 < mouse_y < 250):
                    total_secs -= 1
                if (320 < mouse_x < 470) and (50 < mouse_y < 100):
                    start = True
                if (320 < mouse_x < 470) and (150 < mouse_y < 200):
                    total_secs = 0

    if start:
        total_secs -= 1        
        if total_secs == 0:
            start = False           
        time.sleep(1)

    if total_secs < 0:
        total_secs = 0

    if restart:
        total_secs = 0
        start = False

    mins = int(total_secs/60)
    secs = total_secs - mins*60

    text_time1 = font.render(str(mins),True,BLACK)
    text_time2 = font.render(str(secs),True,BLACK)
    text_time3 = font.render(':',True,BLACK)

    screen.blit(text_time1, (67,140))
    screen.blit(text_time2, (167,140))
    screen.blit(text_time3, (117,140))

    extra_x1 = math.sin(6*secs*math.pi/180)*50
    extra_y1 = math.cos(6*secs*math.pi/180)*50
    extra_x2 = math.sin(6*mins*math.pi/180)*50
    extra_y2 = math.cos(6*mins*math.pi/180)*50

    pygame.draw.line(screen, BLACK, (250,400), (250+extra_x1,400-extra_y1))
    pygame.draw.line(screen, RED, (250,400), (250+extra_x2,425-extra_y2))
    if total_secs != 0:
        pygame.draw.rect(screen, RED, (100,500,300-300/total_secs,50))

    pygame.display.flip()