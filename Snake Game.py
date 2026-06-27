"""
CLASSIC SNAKE GAME
OOP: Classes, Inheritance, Polymorphism, Properties
"""

import pygame
import random
from abc import ABC, abstractmethod

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
FPS = 10

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (255,0,0)
DARK_GREEN = (0,150,0)

# ========== ABSTRACT CLASS ==========
class GameObject(ABC):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    @abstractmethod
    def draw(self, surf): pass
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

# ========== SNAKE SEGMENT ==========
class Segment(GameObject):
    def draw(self, surf):
        pygame.draw.rect(surf, GREEN, self.rect)
        pygame.draw.rect(surf, DARK_GREEN, self.rect, 2)

# ========== FOOD ==========
class Food(GameObject):
    def draw(self, surf):
        pygame.draw.rect(surf, RED, self.rect)

# ========== GAME ==========
class SnakeGame:
    def __init__(self):
        self.cell_size = 20
        self.width_cells = WIDTH // self.cell_size
        self.height_cells = HEIGHT // self.cell_size
        self.snake = []
        self.direction = (1, 0)  # right
        self.food = None
        self.score = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        self.reset_game()
    
    def reset_game(self):
        # Snake starts with 3 segments
        start_x = self.width_cells // 2
        start_y = self.height_cells // 2
        self.snake = [
            Segment(start_x * self.cell_size, start_y * self.cell_size, self.cell_size),
            Segment((start_x-1) * self.cell_size, start_y * self.cell_size, self.cell_size),
            Segment((start_x-2) * self.cell_size, start_y * self.cell_size, self.cell_size)
        ]
        self.direction = (1, 0)
        self.score = 0
        self.game_over = False
        self.spawn_food()
    
    def spawn_food(self):
        while True:
            fx = random.randint(0, self.width_cells-1) * self.cell_size
            fy = random.randint(0, self.height_cells-1) * self.cell_size
            # Check if food not on snake
            collision = False
            for seg in self.snake:
                if seg.x == fx and seg.y == fy:
                    collision = True
                    break
            if not collision:
                self.food = Food(fx, fy, self.cell_size)
                break
    
    def move(self):
        if self.game_over:
            return
        head = self.snake[0]
        new_x = head.x + self.direction[0] * self.cell_size
        new_y = head.y + self.direction[1] * self.cell_size
        
        # Check wall collision
        if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:
            self.game_over = True
            return
        
        # Check self collision
        for seg in self.snake:
            if seg.x == new_x and seg.y == new_y:
                self.game_over = True
                return
        
        # Add new head
        new_head = Segment(new_x, new_y, self.cell_size)
        self.snake.insert(0, new_head)
        
        # Check food collision
        if new_head.x == self.food.x and new_head.y == self.food.y:
            self.score += 10
            self.spawn_food()
            # Increase speed slightly
            global FPS
            FPS = min(20, 10 + self.score // 50)
        else:
            self.snake.pop()
    
    def change_direction(self, new_dir):
        # Prevent moving back into itself
        opposite = { (1,0): (-1,0), (-1,0): (1,0), (0,1): (0,-1), (0,-1): (0,1) }
        if new_dir != opposite.get(self.direction):
            self.direction = new_dir
    
    def draw(self):
        screen.fill(BLACK)
        for seg in self.snake:
            seg.draw(screen)
        if self.food:
            self.food.draw(screen)
        
        # UI
        score_txt = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_txt, (10,10))
        
        if self.game_over:
            go = self.big_font.render("GAME OVER", True, RED)
            restart = self.font.render("Press R to Restart", True, WHITE)
            screen.blit(go, (WIDTH//2 - 130, HEIGHT//2 - 50))
            screen.blit(restart, (WIDTH//2 - 110, HEIGHT//2 + 20))
        
        pygame.display.flip()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                if not self.game_over:
                    if event.key == pygame.K_UP:
                        self.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.change_direction((1, 0))
        return True
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.move()
            self.draw()
            clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()