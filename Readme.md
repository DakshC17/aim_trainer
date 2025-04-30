# 🎯 Aim Trainer --->> ProLABS

A visually engaging **Aim Trainer** built with **Pygame**, bundled with a sleek **Streamlit** launcher. This game is designed to improve your reflexes and mouse accuracy while offering a clean and immersive UI experience.

---

## 🚀 Features

### 🎮 Game (Pygame)
- **Multiple targets** that grow and shrink.
- Click on targets before they disappear.
- **Speed** and **accuracy** tracking.
- **Clean UI** with top bar showing:
  - Time Elapsed
  - Speed (targets/sec)
  - Hits Count
  - Lives Remaining
- **End screen summary** with:
  - Time
  - Speed
  - Hits
  - Accuracy

### 🧭 Launcher (Streamlit)
- Fullscreen **Streamlit** app with a **gradient background**.
- Centered **Play** and **Exit** buttons.
- Smooth UI interactions and hover animations.
- Launches the game with a single click.

---

## 🖼️ Screenshots

**Launcher**

![Launcher](https://sa8pqnq0bt.ufs.sh/f/btLxSziC2OEmmKVYuFMFe7RdjbnL5tsYTxyNkgVo24HQMUKD)

**Game**

![Game](https://sa8pqnq0bt.ufs.sh/f/btLxSziC2OEmTsFFOm7pLEziayjGtoYQWRD27X6Sgx4JvkbN)

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Pygame**
- **Streamlit**

---

## 📂 File Structure
```bash
.
├── main.py           # Pygame game logic
├── launcher.py       # Streamlit launcher interface
├── README.md         # Project documentation


🚀 Run Instructions

Run Launcher with Streamlit-----

To start the launcher, simply run:

streamlit run launcher.py

Run Game Directly (optional)-----

If you want to run the game without the launcher, use:

python3 main.py
