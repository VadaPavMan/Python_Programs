import pygame
import random
import sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((GRID_WIDTH // 2), (GRID_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.head_color = DARK_GREEN
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + x) % GRID_WIDTH), (cur[1] + y) % GRID_HEIGHT)
        
        if len(self.positions) > 2 and new in self.positions[2:]:
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        return True

    def reset(self):
        self.length = 1
        self.positions = [((GRID_WIDTH // 2), (GRID_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def render(self, surface):
        for i, p in enumerate(self.positions):
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            if i == 0:
                pygame.draw.rect(surface, self.head_color, r)
                pygame.draw.rect(surface, BLACK, r, 1)
            else:
                pygame.draw.rect(surface, self.color, r)
                pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def render(self, surface):
        r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

def draw_grid(surface):
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GRAY, rect, 1)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    
    snake = Snake()
    food = Food()
    
    font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 72)
    
    game_over = False
    
    while True:
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        snake.reset()
                        food.randomize_position()
                        game_over = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            screen.fill(BLACK)
            game_over_text = game_over_font.render('GAME OVER', True, RED)
            score_text = font.render(f'Final Score: {snake.score}', True, WHITE)
            restart_text = font.render('Press ENTER to restart', True, WHITE)
            quit_text = font.render('Press ESC to quit', True, WHITE)
            
            screen.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - 100))
            screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, WINDOW_HEIGHT // 2))
            screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, WINDOW_HEIGHT // 2 + 50))
            screen.blit(quit_text, (WINDOW_WIDTH // 2 - quit_text.get_width() // 2, WINDOW_HEIGHT // 2 + 90))
            
            pygame.display.update()
            continue
        
        snake.handle_keys()
        
        if not snake.update():
            game_over = True
            continue
        
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 10
            food.randomize_position()
            while food.position in snake.positions:
                food.randomize_position()
        
        screen.fill(BLACK)
        draw_grid(screen)
        snake.render(screen)
        food.render(screen)
        
        score_text = font.render(f'Score: {snake.score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        clock.tick(10)  

if __name__ == '__main__':
    main()
