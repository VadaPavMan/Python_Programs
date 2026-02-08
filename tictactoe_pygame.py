import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 900, 1000

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

    # Draw Screen With Color
    screen.fill(pygame.Color("black"))

    # Draw Linings Horizontal Vertical
    add_space = -180
    for i in range(2):
        pygame.draw.line(
            screen,
            pygame.Color("white"),
            (0, (HEIGHT // 2) + add_space),
            (WIDTH, (HEIGHT // 2) + add_space),
            5,
        )

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
