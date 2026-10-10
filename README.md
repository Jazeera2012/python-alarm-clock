# ⏰ Python Alarm Clock

A graphical alarm clock built with Python, Tkinter, and Pygame.

## ✨ Features

- 🕒 Live digital clock with hours, minutes, and seconds
- ⏰ Set an alarm using the `HH:MM:SS` format
- 🎵 Play MP3 music when the alarm rings
- 😴 Snooze the alarm for 5 minutes
- 🛑 Stop the alarm whenever needed
- 🎨 Custom GUI design
- ✅ Input validation and error messages

## 🛠️ Technologies Used

- Python
- Tkinter
- Pygame
- `datetime`
- `os`

## 📁 Project Structure

```text
python-alarm-clock/
├── alarm_clock.py
├── alarm_music.mp3
└── README.md
```

## ⚙️ Installation

1. Install Python 3.13 or another compatible Python version.
2. Install Pygame:

   ```bash
   python -m pip install pygame
   ```

3. Place your own MP3 alarm sound in the same folder as `alarm_clock.py`.
4. Make sure the file is named `alarm_music.mp3`.

## ▶️ How to Run

```bash
python alarm_clock.py
```

On macOS, you can also use `python3.13 alarm_clock.py` if Pygame is installed for that interpreter.

## 🎮 How to Use

1. Launch the application.
2. Enter the desired alarm time in `HH:MM:SS` format.
3. Click **Set Alarm**.
4. When the alarm rings, choose **Snooze 5 min** to postpone it or **Stop Alarm** to stop it.

## 📚 What I Learned

- Creating a graphical interface with Tkinter
- Working with Python functions and global variables
- Validating time input with `datetime`
- Using `after()` to schedule repeated checks
- Playing audio with Pygame
- Working with file paths using `os`
- Managing alarm states and implementing snooze functionality

## 👩‍💻 Author

Created by Jazeera as part of my Python projects portfolio.

---

*Note: The alarm may not work as expected if the computer is asleep or powered off. Use an MP3 file you have permission to distribute if you include it in the public repository.*
