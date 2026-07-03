
# 🏏 Hand Cricket Game

A text-based Hand Cricket game built in Python where you play against the computer. This project was created while learning Python and helped me practice programming fundamentals such as functions, loops, conditionals, and random number generation.

---

## 🎮 How the Game Works

The game follows the basic rules of hand cricket with a toss, two innings, wickets, and a target chase.

### 🪙 Toss

- The player first chooses **Odd** or **Even**.
- The player enters a number between **1 and 6**.
- The computer randomly selects its own number.
- The sum of both numbers determines the toss winner:
  - **Odd** total → Odd wins
  - **Even** total → Even wins
- Whoever wins the toss chooses whether to **bat** or **bowl** first.

---

### 🏏 Match Rules

- Each innings consists of:
  - **10 balls**
  - **3 wickets**
- On every ball:
  - The player enters a number between **1 and 6**.
  - The computer randomly generates a number between **1 and 6**.

#### Batting

- If the player's number and the computer's number are **different**, the batsman scores runs.
- If both numbers are **the same**, the batsman loses a wicket.
- The innings ends when:
  - All **3 wickets** are lost, or
  - All **10 balls** have been played.

---

### 🎯 Target Chase

After the first innings:

- The batting and bowling sides switch.
- The second team must score **more than the first team's total** before:
  - Losing all 3 wickets, or
  - Using all 10 balls.

If the chasing team scores more than the target, they win immediately.

---

## ✨ Features

- 🪙 Odd/Even toss system
- 🏏 Choice to bat or bowl after winning the toss
- 🎲 Random computer moves
- 📊 Live score updates
- 🚪 3-wicket system
- ⏱️ 10-ball innings
- 🎯 Target chase
- 🏆 Automatic winner announcement
- 🤝 Tie detection

---

## 🛠️ Technologies Used

- Python
- Random Module

---

## 📚 Concepts Practiced

- Functions
- Loops (`while`)
- Conditional Statements (`if`, `elif`, `else`)
- User Input Validation
- Variables
- Global Variables
- Random Number Generation
- Game Logic

---

## 🚀 About

## 🚀 About

This is one of my first Python projects, created while I was learning the fundamentals of programming. The goal was to simulate a complete hand cricket match while practicing functions, loops, conditionals, user input validation, and random number generation.

As I'm still new to Python, there is plenty of room for improvement, and I plan to continue updating this project as my skills grow. Constructive feedback, suggestions, and advice are always appreciated. Thank you for taking the time to check out my project!
