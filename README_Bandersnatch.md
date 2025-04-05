# 🕹️ Bandersnatch

**Bandersnatch** is a Doom-style retro FPS game built using Python, featuring real-time **ray tracing** to render immersive and dynamic 3D environments. Dive into a surreal pixelated world full of horrors, puzzles, and secrets.

---

## 🚀 Features

- 🔫 Classic DOOM-style movement and combat  
- 🧠 Puzzle elements inspired by surreal horror themes  
- 💡 Ray-traced lighting and reflections (Python-based)  
- 🧟 Enemy AI with basic pathfinding and attack patterns  
- 🗝️ Level progression, health system, and item pickups  
- 🖼️ Retro pixel art-style graphics and textures  
- 🛠️ Modular codebase for easy level/map modifications  

---

## 📸 Screenshots

> *(Add your own screenshots in the `assets/screenshots/` folder)*

```
![Gameplay Screenshot](assets/screenshots/screenshot1.png)
![Raytraced Lighting](assets/screenshots/screenshot2.png)
```

---

## 🧑‍💻 Built With

- **Python 3.9+**
- **Pygame** — For windowing, input, and audio
- **NumPy** — For vector math & ray calculations
- **Custom Ray Tracer** — Written from scratch for real-time gameplay rendering

---

## 🛠️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/bandersnatch-fps.git
cd bandersnatch-fps
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Game**
```bash
python main.py
```

---

## 🎮 Controls

| Key         | Action              |
|-------------|---------------------|
| `W` `A` `S` `D` | Move Player         |
| `Mouse`     | Look/Aim             |
| `Left Click`| Shoot                |
| `E`         | Interact / Open Door |
| `Esc`       | Pause / Quit         |

---

## 📂 Project Structure

```
bandersnatch/
├── assets/             # Sprites, textures, sounds
├── engine/             # Core raytracing and rendering logic
├── levels/             # Level configuration files
├── main.py             # Game entry point
├── config.py           # Game settings and constants
├── README.md
└── requirements.txt
```

---

## 📈 Performance Tips

- For smoother performance, adjust `MAX_RAYS`, resolution, and lighting depth in `config.py`
- Optional: Use **PyPy** to run for better FPS in some environments

---

## 🤯 Inspirations

- [DOOM (1993)](https://doomwiki.org)
- [Wolfenstein 3D](https://en.wikipedia.org/wiki/Wolfenstein_3D)
- Netflix’s **Bandersnatch** (for surreal themes and choices)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍👩‍👧‍👦 Credits

Created by **Mayur Jadhav** and contributors  
Special thanks to the open-source game dev community!

---

## 🌌 Easter Egg

> "Reality is just a rendering away from collapse."

---
