# 🐍 Snake Game — Python OOP Project

A fully functional classic Snake Game built with **Python** and **Pygame**, designed to demonstrate Object-Oriented Programming concepts including Abstract Classes, Inheritance, Polymorphism, and Properties.

---

## 👩‍💻 Project By

**Warda Zaheer**
BS Artificial Intelligence — 4th Semester
University of Haripur | Roll No: F24-1630 | Section D

---

## 📋 Project Overview

This Snake Game was built as an OOP course project. The player controls a snake that moves around a 600×600 grid, eats food to grow longer, and tries to avoid hitting walls or its own body. Speed increases as score goes up, making the game progressively harder.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3 | Main programming language |
| Pygame | Game window, drawing, keyboard input, FPS control |
| ABC Module | Abstract Base Class creation |
| Random Module | Random food position generation |

---

## 🧱 OOP Concepts Used

| Concept | Implementation |
|---------|---------------|
| **Abstract Class** | `GameObject` — base class with abstract `draw()` method |
| **Inheritance** | `Segment` and `Food` both inherit from `GameObject` |
| **Polymorphism** | `draw()` behaves differently in `Segment` (green) vs `Food` (red) |
| **Properties** | `rect` property in `GameObject` returns a `pygame.Rect` object |
| **Encapsulation** | All game logic is contained inside the `SnakeGame` class |

---

## 📁 Project Structure

```
snake-game/
│
├── Snake_Game.py            # Main game source code
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── docs/
    └── SnakeGame_Presentation.pptx   # Project presentation slides
```

---

## 🚀 How to Run

**Step 1** — Install the required library:
```
pip install pygame
```

**Step 2** — Run the game:
```
python Snake_Game.py
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| ↑ Arrow | Move Up |
| ↓ Arrow | Move Down |
| ← Arrow | Move Left |
| → Arrow | Move Right |
| R | Restart after Game Over |

---

## ✨ Features

- Classic snake gameplay on a 600×600 grid
- Live score display on screen
- Speed increases as score goes up (FPS: 10 → max 20)
- Game Over screen with instant restart option
- Food never spawns on the snake's body
- Reverse direction protection (can't go into yourself)

---

## 📊 Speed Progression

| Score | Speed |
|-------|-------|
| 0 | 10 FPS (Start) |
| 50 | 11 FPS |
| 100 | 12 FPS |
| 200 | 14 FPS |
| 300 | 16 FPS |
| 500+ | 20 FPS (Max) |

---

## 📂 Docs

The `docs/` folder contains the full project presentation (20 slides) covering:
- Game design and logic
- OOP class structure
- Code walkthrough
- Challenges faced and lessons learned

---

## 📄 License

This project was made for academic purposes at the University of Haripur.
