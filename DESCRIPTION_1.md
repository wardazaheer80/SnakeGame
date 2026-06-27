# 🐍 Snake Game — Project Description & OOP Usage Guide

**Project:** Classic Snake Game  
**Language:** Python 3  
**Library:** Pygame  
**Concepts:** Object-Oriented Programming (OOP)  
**Developer:** Warda Zaheer | Roll No: F24-1630 | Section D | University of Haripur

---

## 🎮 What is This Game?

Snake Game is a classic arcade game originally from the 1970s. In this project, it is rebuilt using Python and Pygame with a full Object-Oriented Programming structure.

The player controls a snake moving on a 600×600 pixel grid. The snake eats red food to grow longer and score points. The game ends if the snake hits a wall or its own body. As the score increases, the snake moves faster — making the game progressively harder.

---

## 🏗️ Class Structure & Design

The entire game is built using 4 classes. Here is how they are connected:

```
           GameObject  (Abstract Base Class)
           /        \
      Segment        Food
      (Green)        (Red)
           \        /
           SnakeGame  (Main Game Controller)
```

| Class | Type | Role |
|-------|------|------|
| `GameObject` | Abstract Class | Base template for all game objects |
| `Segment` | Child Class | Represents one piece of the snake body |
| `Food` | Child Class | Represents the food item on the grid |
| `SnakeGame` | Controller Class | Controls the entire game logic |

---

## 🧱 OOP Concepts — How Each One is Used

### 1️⃣ Abstract Class — `GameObject`

**What it is:** A class that cannot be used directly to create objects. It acts as a blueprint or template that forces all child classes to follow a specific structure.

**How it is used in the game:**

```python
from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    @abstractmethod
    def draw(self, surf):
        pass  # Every child class MUST implement this
```

- `GameObject` cannot be created directly — you cannot write `obj = GameObject()`
- It forces `Segment` and `Food` to both have a `draw()` method
- This ensures every game object knows how to draw itself

---

### 2️⃣ Inheritance — `Segment` and `Food`

**What it is:** A child class automatically gets all the properties and methods of the parent class, plus it can add its own.

**How it is used in the game:**

```python
class Segment(GameObject):       # Segment inherits from GameObject
    def draw(self, surf):
        pygame.draw.rect(surf, GREEN, self.rect)
        pygame.draw.rect(surf, DARK_GREEN, self.rect, 2)

class Food(GameObject):          # Food inherits from GameObject
    def draw(self, surf):
        pygame.draw.rect(surf, RED, self.rect)
```

| What is Inherited | From `GameObject` |
|-------------------|-------------------|
| `self.x` | x position on grid |
| `self.y` | y position on grid |
| `self.size` | size of the object |
| `rect` property | returns `pygame.Rect` object |

Both `Segment` and `Food` did NOT need to write position or size code again — they inherited it directly from `GameObject`. This saves code and avoids repetition.

---

### 3️⃣ Polymorphism — `draw()` Method

**What it is:** Same method name, but different behavior depending on which class calls it.

**How it is used in the game:**

```python
# One loop, two different behaviors
for seg in self.snake:
    seg.draw(screen)    # Draws GREEN rectangle (Segment)

self.food.draw(screen)  # Draws RED rectangle (Food)
```

- `Segment.draw()` → draws a **green** rectangle (snake body)
- `Food.draw()` → draws a **red** rectangle (food item)

Both use the exact same method name `draw()` but the output is completely different. Python automatically knows which `draw()` to call based on the object type. This is Polymorphism.

---

### 4️⃣ Properties — `@property` Decorator

**What it is:** A method that works like a variable — you access it without using brackets.

**How it is used in the game:**

```python
class GameObject(ABC):

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

# Using it — no brackets needed!
seg.rect      # Returns pygame.Rect object automatically
food.rect     # Same thing, fresh Rect every time
```

- Pygame needs a `Rect` object for drawing and collision detection
- Instead of creating a new Rect manually every time, `rect` is made a `@property`
- Every time `obj.rect` is accessed, it automatically gives a fresh updated Rect

---

### 5️⃣ Encapsulation — `SnakeGame` Class

**What it is:** Keeping all related data and logic inside one class, protected and organized.

**How it is used in the game:**

```python
class SnakeGame:
    def __init__(self):
        self.snake = []           # Snake body segments
        self.direction = (1, 0)   # Current movement direction
        self.food = None          # Current food object
        self.score = 0            # Player score
        self.game_over = False    # Game state flag
```

All game logic — movement, collision detection, food spawning, score tracking — is fully contained inside `SnakeGame`. Nothing leaks outside. This makes the code clean, organized, and easy to manage.

---

## ⚙️ Game Features & How They Work

### Snake Movement
- Snake is a list of `Segment` objects
- Every frame: new head is added at the front, tail is removed from the back
- This creates the illusion of smooth movement
- If food is eaten: tail is NOT removed — snake grows by 1 segment

### Collision Detection
- **Wall collision:** checks if new head position goes outside 600×600 window
- **Self collision:** checks if new head matches any existing segment position
- **Food collision:** checks if new head matches food position → score +10

### Food Spawning
- Food spawns at a random grid cell (30×30 grid)
- A `while` loop keeps trying new positions until one is found that is NOT on the snake body
- This guarantees food never appears inside the snake

### Score & Speed System
```
FPS = min(20, 10 + score // 50)
```

| Score | Speed |
|-------|-------|
| 0 | 10 FPS |
| 50 | 11 FPS |
| 100 | 12 FPS |
| 200 | 14 FPS |
| 300 | 16 FPS |
| 500+ | 20 FPS (Maximum) |

### Reverse Direction Protection
- A dictionary stores the opposite of each direction
- If player presses the opposite key, the input is ignored
- This prevents the snake from instantly running into itself

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| ↑ Arrow | Move Up — direction = (0, -1) |
| ↓ Arrow | Move Down — direction = (0, +1) |
| ← Arrow | Move Left — direction = (-1, 0) |
| → Arrow | Move Right — direction = (+1, 0) |
| R | Restart after Game Over |

---

## 📚 Libraries Used

| Library | Type | Purpose |
|---------|------|---------|
| `pygame` | Install required | Game window, drawing, keyboard input, FPS |
| `abc` | Python built-in | Abstract Base Class and `@abstractmethod` |
| `random` | Python built-in | Random food position generation |

> **Note:** Only `pygame` needs to be installed. `abc` and `random` come with Python automatically.

---

## 🚀 How to Run

```bash
pip install pygame
python Snake_Game.py
```

---

*Project by Warda Zaheer — BS Artificial Intelligence, 4th Semester, University of Haripur*
