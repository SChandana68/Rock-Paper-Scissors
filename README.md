# Rock-Paper-Scissors
# 🎮 Rock–Paper–Scissors Console Game

A visually engaging, console-based Rock–Paper–Scissors game in Python featuring **best-of-N rounds**, ASCII art, colorized output, and clear score tracking.

---

## 📌 Highlights

- Play a **best-of-N match** (you select number of rounds)  
- **ASCII art** visual representation of each move  
- **Colored terminal output** via `colorama`  
- **Flexible input**: accepts `r`/`p`/`s`, case-insensitive, and `q` to quit  
- **Score summary** and overall winner announcement

---

## 📋 Table of Contents
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Demo](#demo)  

## 🛠 Prerequisites

- **Python 3.6+**  
- **colorama** library for terminal colors:
  ```bash
  pip install colorama
🚀 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your_username/rps_game.git
cd rps_game
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
bash
Copy
Edit
python rps_advanced.py
Follow on-screen prompts:

Enter the number of rounds (e.g., 3, 5) or q to quit

For each round, choose rock/paper/scissors

See colorful ASCII art results and round outcomes

View final score and winner at the end

🕹 Demo
yaml
Copy
Edit
🎮 Rock–Paper–Scissors Game
Play best of how many? (3,5...) or 'q' to quit: 3

Round 1 of 3
Choose [r]ock, [p]aper, [s]cissors or 'q' to quit: r

You chose:
   [ASCII art of rock]
Computer chose:
   [ASCII art of paper]
Computer wins this round!

... (more rounds) ...

Final Score – You: 1, Computer: 2, Ties: 0
😞 Computer won overall.
