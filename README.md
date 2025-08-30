# 🐍 Snake Game (Python + Tkinter)

A classic Snake Game built entirely with **Python** and **Tkinter**.  
This project was created by **Aryan Prasher** as a fun beginner-friendly GUI game.  
The code is clean, fully commented, and easy to customize for anyone looking to learn game development with Python.

---

## 🎮 Features
- Smooth snake movement with **keyboard controls** (W, A, S, D)
- Snake grows in size when it eats food
- Score counter that increases with each food item eaten
- Increasing difficulty (snake speed up as score increases)
- Collision detection (wall or body -> Game Over)
- Restart button to quickly start a new game
- Fully resizable and centered Tkinter game window

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Tkinter** (built-in GUI library)
- **Random module** for generating food positions

---

## 🚀 How to Run

### 1. Clone this repository
```bash
git clone https://github.com/YOUR-USERNAME/snake-game-python.git
cd snake-game-python

To run the game
python snake_game.py


🔧 How to Customize

You can easily modify the game using these constants in the code:
| Variable                    | Description                   | Example Value |
| --------------------------- | ----------------------------- | ------------- |
| `GAME_WIDTH`, `GAME_HEIGHT` | Window size                   | `700`, `700`  |
| `SPEED`                     | Snake speed (lower is faster) | `150`         |
| `SPACE_SIZE`                | Snake block size              | `50`          |
| `BODY_PARTS`                | Starting length of snake      | `3`           |
| `SNAKE_COLOR`               | Color of the snake            | `#00ff00`     |
| `FOOD_COLOR`                | Color of the food             | `#D1233B`     |
| `BACKGROUND_COLOR`          | Canvas background color       | `#A6FF96`     |


Want a harder game? Lower the SPEED.
Want a bigger snake? Increase BODY_PARTS.
Want cooler visuals? Change SNAKE_COLOR, FOOD_COLOR, and BACKGROUND_COLOR.


💡 Ideas for Future Updates

Here are some ideas for people to fork this repo and add cool features:

🏆 High Score Tracker: Save the best score locally or in a file

🎶 Sound Effects & Music: Play sounds when eating or game over

🎨 Themes: Add multiple themes (dark mode, retro, neon, etc.)

🕹️ Difficulty Modes: Easy/Medium/Hard with different speeds

🌍 Multiplayer Mode: Two-player snake game using different keys

🔥 Obstacles: Randomly generate blocks on the screen for extra difficulty

📱 Mobile Support: Convert this to a Kivy or PyGame project for mobile

💾 Leaderboard System: Use SQLite or Firebase to store player scores

⚡ Power-Ups: Add power-ups like speed boost, freeze timer, or bonus points

🧩 Grid Size Customization: Allow players to choose custom grid sizes

🖼️ Custom Skins: Players can upload their own snake & food images


🤝 Contributing

Want to make this game better? Here's how you can contribute:

Fork the repository

1)Create a new branch for your feature:
git checkout -b feature-name

2)Commit your changes:
git commit -m "Added a cool new feature"
3)Push your changes:
git push origin feature-name

🧑‍💻 Author

👤 Aryan Prasher
📧 aryan.125413@stu.upes.ac.in

📜 License

This project is licensed under the MIT License – feel free to use, modify, and share!

🎮 Enjoy the game and happy coding! 🚀

