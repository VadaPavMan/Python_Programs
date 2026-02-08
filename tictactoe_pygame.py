import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 900, 1000

arr = [[0, 0, 0]
      ,[0, 0, 0], 
       [0, 0, 0]]

# Define Position:
# TOP_LEFT = x(0, 270) y(0, 320)
# TOP_MID = x(271, 630) y(0, 320)
# TOP_RIGHT = x(631, 900) y(0, 320)

# MID_LEFT = x(0, 270) y(320, 680)
# MID_MID = x(271, 630) y(320, 680)
# MID_RIGHT = x(631, 900) y(320, 680)

# DOWN_LEFT = x(0, 270) y(680, 1000)
# DOWN_MID = x(271, 630) y(680, 1000)
# DOWN_RIGHT = x(631, 900) y(680, 1000)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

running = True
while running:

    # Score System
    x = 0
    o = 0
    score = f"X: {x} | O: {o}"
    font = pygame.font.SysFont("Arial", 40)
    text_surface = font.render(score, True, pygame.Color("black"))
    text_rect = text_surface.get_rect()
    text_rect.center = (450, (HEIGHT - 50))

    # Main Game Event Handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH = event.w
            HEIGHT = event.h

            screen = pygame.display.set_mode((WIDTH, HEIGHT))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            print(f"Clicked at: {mouse_pos}")
            
            # Top
            if (mouse_pos[0] > 0 and mouse_pos[0] <= 270) and (mouse_pos[1] > 0 and mouse_pos[1] <= 320):
                print(f'Clicked On Top Left')
                if arr[0][0] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[0][0] = 1
            elif (mouse_pos[0] > 271 and mouse_pos[0] <= 630) and (mouse_pos[1] > 0 and mouse_pos[1] <= 320):
                print(f'Clicked On Top Mid')
                if arr[0][1] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[0][1] = 1
            elif (mouse_pos[0] > 631 and mouse_pos[0] <= 900) and (mouse_pos[1] > 0 and mouse_pos[1] <= 320):
                print(f'Clicked On Top Right')
                if arr[0][2] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[0][2] = 1
            
            # Mid
            if (mouse_pos[0] > 0 and mouse_pos[0] <= 270) and (mouse_pos[1] > 320 and mouse_pos[1] <= 680):
                print(f'Clicked On Mid Left')
                if arr[1][0] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[1][0] = 1
            elif (mouse_pos[0] > 271 and mouse_pos[0] <= 630) and (mouse_pos[1] > 320 and mouse_pos[1] <= 680):
                print(f'Clicked On Mid Mid')
                if arr[1][1] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[1][1] = 1
            elif (mouse_pos[0] > 631 and mouse_pos[0] <= 900) and (mouse_pos[1] > 320 and mouse_pos[1] <= 680):
                print(f'Clicked On Mid Right')
                if arr[1][2] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[1][2] = 1
            
            # Down
            if (mouse_pos[0] > 0 and mouse_pos[0] <= 270) and (mouse_pos[1] > 680 and mouse_pos[1] <= 1000):
                print(f'Clicked On Down Left')
                if arr[2][0] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[2][0] = 1
            elif (mouse_pos[0] > 271 and mouse_pos[0] <= 630) and (mouse_pos[1] > 680 and mouse_pos[1] <= 1000):
                print(f'Clicked On Down Mid')
                if arr[2][1] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[2][1] = 1
            elif (mouse_pos[0] > 631 and mouse_pos[0] <= 900) and (mouse_pos[1] > 680 and mouse_pos[1] <= 1000):
                print(f'Clicked On Down Right')
                if arr[2][2] == 1:
                    print(f'Positon Already Taken')
                    pass
                else:
                    arr[2][2] = 1
                    
    # Draw Screen With Color
    screen.fill(pygame.Color("black"))

    # Draw Linings Horizontal Vertical
    add_space = -180
    for i in range(2):
        
        # Horizontal
        pygame.draw.line(
            screen,
            pygame.Color("white"),
            (0, (HEIGHT // 2) + add_space),
            (WIDTH, (HEIGHT // 2) + add_space),
            5,
        )
        
        # Vertical
        pygame.draw.line(
            screen,
            pygame.Color("white"),
            ((WIDTH // 2) + add_space, 0),
            ((WIDTH // 2) + add_space, HEIGHT),
            5,
        )
        add_space = 180

    # Score Board
    pygame.draw.rect(
        screen,
        pygame.Color("antiquewhite"),
        (300, (HEIGHT - 100), 300, 100),
        0,
        border_radius=22,
    )
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
