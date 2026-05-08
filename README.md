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

<img width="1121" height="787" alt="main_window" src="https://github.com/user-attachments/assets/3d17a531-12fc-4a48-8eab-c64993eb878a" />


<img width="1115" height="775" alt="language_selection" src="https://github.com/user-attachments/assets/4ff28a8f-da3c-4db6-83a7-9bbeed2057db" />

<img width="1121" height="792" alt="level01_english" src="https://github.com/user-attachments/assets/a5c03272-bf4e-47f8-a3c9-4876e6a2f557" />

<img width="1122" height="792" alt="level01_arabic" src="https://github.com/user-attachments/assets/363ed491-58c0-412f-ac89-8d6fc6646b56" />

<img width="1122" height="787" alt="level01_english_results" src="https://github.com/user-attachments/assets/507f1a22-c3f9-46d0-9bf3-1ea06d977e87" />

<img width="1116" height="785" alt="level02_arabic" src="https://github.com/user-attachments/assets/b74ece50-9140-4f79-af33-9bf38c06d724" />

<img width="1117" height="780" alt="level02_english" src="https://github.com/user-attachments/assets/7d88a6cd-d057-4601-ab87-6b37c57f7d6c" />

<img width="1117" height="787" alt="level02_arabic_results" src="https://github.com/user-attachments/assets/f1a2f592-1ef3-4ef7-9916-fdeb581d9fe5" />

<img width="1122" height="790" alt="level02_results" src="https://github.com/user-attachments/assets/d69ef585-9040-4ebf-babd-951c7a884210" />


<img width="1122" height="781" alt="level03_english" src="https://github.com/user-attachments/assets/4894b38b-522b-432e-824f-ed6025c336f1" />

<img width="1117" height="786" alt="level03_arabic" src="https://github.com/user-attachments/assets/3276cb5e-ad6f-4c36-95bc-d16980fa2e66" />

<img width="1110" height="786" alt="level03_results" src="https://github.com/user-attachments/assets/70a2208a-f2fa-4ba1-9873-c1732a370aa0" />


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
