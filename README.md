# ⌨️ Speed Typing Test Game

A desktop-based typing game developed using Python and Tkinter to help users improve their typing speed and accuracy through progressive difficulty levels.
You can also add your own words, sentences and paragraphs if you want to train yourself on specific content.

---

## 🎮 Game Features

🌍 **Bilingual Support**

  * English
  * Arabic

🧠 **3 Difficulty Levels**

  * **Level 1 (Beginner):** Word typing
  * **Level 2 (Intermediate):** Sentence typing
  * **Level 3 (Advanced):** Paragraph typing

⏱️ **Timer-Based Gameplay**

  * 60 seconds per level

📊 **Performance Tracking**

  * Correct inputs
  * Wrong inputs
  * Final score calculation

🎯 **Progression System**

  * Level 1 → requires more than 9 correct to pass, more than 19 correct to be expert, if less than 9 correct you will fail and need to retry
  * Level 2 → requires more than 5 correct to pass, more than 8 correct to be expert, if less than 5 correct you will fail and need to retry
  * Level 3 → requires more than 3 correct to pass, more than 5 correct to be expert, if less than 3 correct you will fail and need to retry

🔁 **User Controls**

  * Retry level
  * Next level
  * Return to main menu

---

## 🔄 Game Flow

1. User selects language (English / Arabic)
2. Text (word / sentence / paragraph) is displayed
3. User types input
4. Game compares input with expected text
5. Score is calculated
6. User progresses or retries based on performance

---

## 🖥️ User Interface

The game is built using **Tkinter GUI**, which includes:

* Interactive windows
* Dynamic labels and counters
* Input text fields
* Timer display
* Navigation buttons

The interface updates in real-time based on user interaction.

---

## 🧱 Project Structure

```
python_speed_typing_game/
│
├── main.py
├── Main_Window.py
├── Level_01English.py
├── Level_02English.py
├── Level_03English.py
├── Level_01Arabic.py
├── Level_02Arabic.py
├── Level_03Arabic.py
├── END GAME.py
│
├── Words_English.txt
├── paragraphs_English.txt
│
│
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ramihesham/python_speed_typing_test.git
cd python_speed_typing_game
```

---

### 2️⃣ Run the game

```bash
python main.py
```

---

## ⚠️ Requirements

* Python 3.x
* Tkinter (comes with Python)

### For Linux users:

```bash
sudo apt-get install python3-tk
```

---

## 📦 Dependencies

```
# No external dependencies required
```

(All modules used are part of Python standard library)

---

## 🖼️ Screenshots

![Main Menu](assets/main_window.png)
![language_selection](assets/language_selection.png)
![level01_english](assets/level01_english.png)
![level01_arabic](assets/level01_arabic.png)
![level01_english_results](assets/level01_english_results.png)
![level02_arabic](assets/level02_arabic.png)
![level02_arabic_results](assets/level02_arabic_results.png)
![level01_english](assets/level01_english.png)

---

## 🔮 Future Improvements

* 📈 Words Per Minute (WPM) calculation
* 🎯 Accuracy percentage
* 🏆 Leaderboard system
* 🌐 Web version (API + frontend)
* 📱 Mobile version (Kivy / Flutter)

---

## 👨‍💻 Author

Rami Hesham Mohamed

**Mechatronics & Robotics Engineering**

---
