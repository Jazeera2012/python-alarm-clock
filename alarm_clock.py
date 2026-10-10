import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import pygame # run as python3.13 alarm_clock.py

# Get the project folder and music file path
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
MUSIC_FILE = os.path.join(PROJECT_FOLDER, "alarm_music.mp3")

# Main window 
root = tk.Tk()
root.title("⏰ Alarm Clock")
root.geometry("440x550")
root.resizable(False, False)
root.configure(bg="#1c7278")

# Alarm variables
alarm_time = None
alarm_active = False
alarm_ringing = False

# Initialize pygame audio
try:
    pygame.mixer.init()
except pygame.error:
    pass

# Display title
title_label = tk.Label(
    root,
    text="⏰ ALARM CLOCK\nby Jazeera",
    font=("Arial", 25, "bold"),
    bg="#1e1e2e",
    fg="#7351c1"
)
title_label.pack(pady=20)

# Display current time
clock_label = tk.Label(
    root,
    text="",
    font=("Arial", 50, "bold"),
    bg="#1e1e2e",
    fg="#f5e0dc"
)
clock_label.pack(pady=10)

def update_clock():
    """Update the clock every second."""
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

# Time input instructions
instruction_label = tk.Label(
    root,
    text="Enter alarm time (HH:MM:SS)",
    font=("Arial", 12),
    bg="#1e1e2e",
    fg="white"
)
instruction_label.pack(pady=(15,5))

# Alarm time input
time_entry = tk.Entry(
    root,
    font=("Arial", 20),
    justify="center",
    width=12
)
time_entry.pack(pady=5)
time_entry.insert(0, "07:30:00")

# Status message
status_label = tk.Label(
    root,
    text="Ready to set your alarm!",
    font=("Arial", 11),
    bg="#1e1e2e",
    fg="#a6e3a1",
    wraplength=380
)
status_label.pack(pady=12)

def set_alarm():
    """Validate and set the alarm."""
    global alarm_time, alarm_active, alarm_ringing

    entered_time = time_entry.get().strip()

    try:
        parsed_time = datetime.strptime(entered_time, "%H:%M:%S")
        alarm_time = parsed_time.strftime("%H:%M:%S")
    except ValueError:
        messagebox.showerror(
            "Invalid Time",
            "Enter time in HH:MM:SS format.\nExample: 07:30:15"
        )
        return

    # Stop any previous alarm music
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()

    alarm_time = entered_time
    alarm_active = True
    alarm_ringing = False

    status_label.config(
        text=f"🔔 Alarm set for {alarm_time}",
        fg="#a6e3a1"
    )

def check_alarm():
    """Check whether the alarm time has arrived."""
    global alarm_active, alarm_ringing

    if alarm_active and not alarm_ringing:
        current_time = datetime.now().strftime("%H:%M:%S")

        if current_time == alarm_time:
            alarm_active = False
            ring_alarm()

    root.after(200, check_alarm)

def ring_alarm():
    """Play the alarm music."""
    global alarm_ringing

    if not os.path.isfile(MUSIC_FILE):
        messagebox.showerror(
            "Missing Music",
            "Place alarm_music.mp3 in the project folder."
        )
        alarm_ringing = False
        return
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.music.load(MUSIC_FILE) 
        pygame.mixer.music.play(-1)

        alarm_ringing = True

        status_label.config(
            text="🚨 ALARM IS RINGING!",
            fg= "#f38ba8"
        )
    except pygame.error as error:
        alarm_ringing = False
        messagebox.showerror("Audio Error", str(error))

def snooze_alarm():
    """Snooze the alarm for five minutes."""
    global alarm_time, alarm_active, alarm_ringing

    if not alarm_ringing:
        return

    # Stop the current music
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()

    # Calculate the new alarm time: five minutes later
    new_alarm = datetime.now() + timedelta(minutes=5)
    alarm_time = new_alarm.strftime("%H:%M:%S")

    alarm_ringing = False
    alarm_active = True

    status_label.config(
        text=f"😴 Snoozed! Alarm again at {alarm_time}",
        fg="#f9e2af"
    )

def stop_alarm():
    """Stop the alarm completely."""
    global alarm_time, alarm_active, alarm_ringing

    alarm_active = False
    alarm_ringing = False
    alarm_time = None

    if pygame.mixer.get_init():
        pygame.mixer.music.stop()

    status_label.config(
        text="🔕 Alarm stopped!",
        fg="#a6e3a1"
    )

# Set Alarm button
set_button = tk.Button(
    root,
    text="🔔 Set Alarm",
    font=("Arial", 13, "bold"),
    bg="#cba6f7",
    fg="#1e1e2e",
    width=20,
    command=set_alarm
)
set_button.pack(pady=6)

# Snooze button
snooze_button = tk.Button(
    root,
    text="😴 Snooze 5 min",
    font=("Arial", 13, "bold"),
    bg="#f9e1af",
    fg="#1e1e2e",
    width=20,
    command=snooze_alarm
)
snooze_button.pack(pady=6)

# Stop Alarm button
stop_button = tk.Button(
    root,
    text="🛑 Stop Alarm",
    font = ("Arial", 13, "bold"),
    bg="#f38ba8",
    fg="#1e1e2e",
    width=20,
    command=stop_alarm
)
stop_button.pack(pady=6)

def close_app():
    """Clean up audio and close the window."""
    stop_alarm()

    if pygame.mixer.get_init():
        pygame.mixer.quit()

    root.destroy()

# Start the clock and alarm checker
update_clock()
check_alarm()

# Handle window closing
root.protocol("WM_DELETE_WINDOW", close_app)

# Run the GUI application
root.mainloop()