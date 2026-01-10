# 🎮 Tic Tac Toe — Console Edition

A clean and simple Tic Tac Toe game built in Python, played directly in the terminal.

The project focuses on clear object-oriented design and readable, well-structured code.

---

## ✨ Features

- Two-player mode (X vs O)
- Console-based game board
- Input validation
- Automatic win & draw detection
- Modular, object-oriented architecture

---

## 📁 Project Structure

```
Tic-Tac-Toe/
├── main.py
└── classes/
    ├── Game.py
    ├── Grid.py
    ├── Player.py
    ├── RandomPlayer.py
    └── StrategyPlayer.py
```

---

## ▶️ Running the Game

Make sure Python 3 is installed.

From the project folder, run:

```bash
python main.py
```

---

## 🕹 How to Play

Players take turns entering a set of numbers from **1 to 3** indicating the grid position
to place their symbol on the board.

The grid positions are:

```
(1,1) | (1,2) | (1,3)
----------------------
(2,1) | (2,2) | (2,3)
----------------------
(3,1) | (3,2) | (3,3)
```

- Player 1 uses **X**
- Player 2 uses **O**
- The first player to align three symbols wins
- If the board fills up, the game ends in a draw

---

## 🛠 Tech

- Python 3.x
- Object-oriented programming
- Console input/output
