import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 900, 1000
current_player = "X"
arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
winner = ""
game_over = False
x_score = 0
o_score = 0

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


def checkWin(arr):
    # Check rows
    for row in range(3):
        if arr[row][0] != 0 and arr[row][0] == arr[row][1] == arr[row][2]:
            return arr[row][0]
    
    # Check columns
    for col in range(3):
        if arr[0][col] != 0 and arr[0][col] == arr[1][col] == arr[2][col]:
            return arr[0][col]
    
    # Check diagonals
    if arr[0][0] != 0 and arr[0][0] == arr[1][1] == arr[2][2]:
        return arr[0][0]
    if arr[0][2] != 0 and arr[0][2] == arr[1][1] == arr[2][0]:
        return arr[0][2]
    
    return None


def checkDraw(arr):
    for row in range(3):
        for col in range(3):
            if arr[row][col] == 0:
                return False
    return True


def resetGame():
    global arr, current_player, winner, game_over
    arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = "X"
    winner = ""
    game_over = False


running = True
while running:

    # Draw Screen With Color
    screen.fill(pygame.Color("black"))

    # Score System
    score = f"X: {x_score} | O: {o_score}"
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
            elif event.key == pygame.K_r:
                resetGame()
                
        elif event.type == pygame.VIDEORESIZE:
            WIDTH = event.w
            HEIGHT = event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = event.pos
            print(f"Clicked at: {mouse_pos}")
            
            row, col = -1, -1

            # Top row
            if mouse_pos[1] > 0 and mouse_pos[1] <= 320:
                row = 0
                if mouse_pos[0] > 0 and mouse_pos[0] <= 270:
                    col = 0
                    print("Clicked On Top Left")
                elif mouse_pos[0] > 271 and mouse_pos[0] <= 630:
                    col = 1
                    print("Clicked On Top Mid")
                elif mouse_pos[0] > 631 and mouse_pos[0] <= 900:
                    col = 2
                    print("Clicked On Top Right")
            
            # Middle row
            elif mouse_pos[1] > 320 and mouse_pos[1] <= 680:
                row = 1
                if mouse_pos[0] > 0 and mouse_pos[0] <= 270:
                    col = 0
                    print("Clicked On Mid Left")
                elif mouse_pos[0] > 271 and mouse_pos[0] <= 630:
                    col = 1
                    print("Clicked On Mid Mid")
                elif mouse_pos[0] > 631 and mouse_pos[0] <= 900:
                    col = 2
                    print("Clicked On Mid Right")
            
            # Bottom row
            elif mouse_pos[1] > 680 and mouse_pos[1] <= 1000:
                row = 2
                if mouse_pos[0] > 0 and mouse_pos[0] <= 270:
                    col = 0
                    print("Clicked On Down Left")
                elif mouse_pos[0] > 271 and mouse_pos[0] <= 630:
                    col = 1
                    print("Clicked On Down Mid")
                elif mouse_pos[0] > 631 and mouse_pos[0] <= 900:
                    col = 2
                    print("Clicked On Down Right")
            
            if row != -1 and col != -1:
                if arr[row][col] == 0:
                    arr[row][col] = current_player
                    
                    winner = checkWin(arr)
                    if winner:
                        game_over = True
                        if winner == "X":
                            x_score += 1
                            print(f"X Wins! Score: X-{x_score} O-{o_score}")
                        else:
                            o_score += 1
                            print(f"O Wins! Score: X-{x_score} O-{o_score}")
                    elif checkDraw(arr):
                        game_over = True
                        winner = "Draw"
                        print("It's a Draw!")
                    else:
                        current_player = "O" if current_player == "X" else "X"
                else:
                    print("Position Already Taken")

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

    # Draw X's and O's
    cell_centers = [
        [(135, 160), (450, 160), (765, 160)],
        [(135, 500), (450, 500), (765, 500)],
        [(135, 840), (450, 840), (765, 840)],
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

    # Display winner or draw message
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        win_font = pygame.font.SysFont("sansserif", 80)
        instruction_font = pygame.font.SysFont("sansserif", 40)
        
        if winner == "Draw":
            win_text = win_font.render("It's a Draw!", True, pygame.Color("yellow"))
        else:
            win_color = pygame.Color("red") if winner == "X" else pygame.Color("blue")
            win_text = win_font.render(f"{winner} Wins!", True, win_color)
        
        win_rect = win_text.get_rect()
        win_rect.center = (WIDTH // 2, HEIGHT // 2 - 50)
        screen.blit(win_text, win_rect)
        
        instruction_text = instruction_font.render("Press R to play again", True, pygame.Color("white"))
        instruction_rect = instruction_text.get_rect()
        instruction_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)
        screen.blit(instruction_text, instruction_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
