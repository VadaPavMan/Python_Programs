import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 900, 1000
current_player = "X" 
arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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

    # Draw Screen With Color
    screen.fill(pygame.Color("black"))

    # Score System
    x = 0
    o = 0
    score = f"X: {x} | O: {o}"
    X_text = "X"
    O_text = "O"
    X_font = pygame.font.SysFont("sansserif", 130)
    O_font = pygame.font.SysFont("sansserif", 130)
    font = pygame.font.SysFont("sansserif", 60)
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
            if (mouse_pos[0] > 0 and mouse_pos[0] <= 270) and (
                mouse_pos[1] > 0 and mouse_pos[1] <= 320
            ):
                print(f"Clicked On Top Left")
                if arr[0][0] == 0:
                    arr[0][0] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")
                    
            elif (mouse_pos[0] > 271 and mouse_pos[0] <= 630) and (
                mouse_pos[1] > 0 and mouse_pos[1] <= 320
            ):
                print(f"Clicked On Top Mid")
                if arr[0][1] == 0:
                    arr[0][1] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")
                    
            elif (mouse_pos[0] > 631 and mouse_pos[0] <= 900) and (
                mouse_pos[1] > 0 and mouse_pos[1] <= 320
            ):
                print(f"Clicked On Top Right")
                if arr[0][2] == 0:
                    arr[0][2] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")

            # Mid
            if (mouse_pos[0] > 0 and mouse_pos[0] <= 270) and (
                mouse_pos[1] > 320 and mouse_pos[1] <= 680
            ):
                print(f"Clicked On Mid Left")
                if arr[1][0] == 0:
                    arr[1][0] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")
                    
            elif (mouse_pos[0] > 271 and mouse_pos[0] <= 630) and (
                mouse_pos[1] > 320 and mouse_pos[1] <= 680
            ):
                print(f"Clicked On Mid Mid")
                if arr[1][1] == 0:
                    arr[1][1] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")
                    
            elif (mouse_pos[0] > 631 and mouse_pos[0] <= 900) and (
                mouse_pos[1] > 320 and mouse_pos[1] <= 680
            ):
                print(f"Clicked On Mid Right")
                if arr[1][2] == 0:
                    arr[1][2] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")

            # Down
            if (mouse_pos[0] > 0 and mouse_pos[0] <= 270) and (
                mouse_pos[1] > 680 and mouse_pos[1] <= 1000
            ):
                print(f"Clicked On Down Left")
                if arr[2][0] == 0:
                    arr[2][0] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")
                    
            elif (mouse_pos[0] > 271 and mouse_pos[0] <= 630) and (
                mouse_pos[1] > 680 and mouse_pos[1] <= 1000
            ):
                print(f"Clicked On Down Mid")
                if arr[2][1] == 0:
                    arr[2][1] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")
                    
            elif (mouse_pos[0] > 631 and mouse_pos[0] <= 900) and (
                mouse_pos[1] > 680 and mouse_pos[1] <= 1000
            ):
                print(f"Clicked On Down Right")
                if arr[2][2] == 0:
                    arr[2][2] = current_player
                    current_player = "O" if current_player == "X" else "X"
                else:
                    print(f"Position Already Taken")

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

    cell_centers = [
        [(135, 160), (450, 160), (765, 160)],      
        [(135, 500), (450, 500), (765, 500)],      
        [(135, 840), (450, 840), (765, 840)]       
    ]
    
    for row in range(3):
        for col in range(3):
            if arr[row][col] == "X":
                X_surface = X_font.render("X", True, pygame.Color("red"))
                X_rect = X_surface.get_rect()
                X_rect.center = cell_centers[row][col]
                screen.blit(X_surface, X_rect)
            elif arr[row][col] == "O":
                O_surface = O_font.render("O", True, pygame.Color("blue"))
                O_rect = O_surface.get_rect()
                O_rect.center = cell_centers[row][col]
                screen.blit(O_surface, O_rect)

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
