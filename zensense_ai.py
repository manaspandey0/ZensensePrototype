import tkinter as tk
from tkinter import Label, Scale, Button, Frame, Text, Scrollbar, messagebox
import cv2
from PIL import Image, ImageTk
import random
import pygame
from datetime import datetime

# Initialize pygame for audio
pygame.mixer.init()

# Create the main application window
root = tk.Tk()
root.title("ZenSense AI Prototype")
root.geometry("1000x700")
root.configure(bg="#e6f7ff")  # Light blue background for a soothing look

# Placeholder for the current mood
current_mood = tk.StringVar()
current_mood.set("Neutral")

# Mood history log
mood_log = []

# Mood-specific tips
mood_tips = {
    "Happy": "Smile more! Stay positive and enjoy your drive.",
    "Calm": "Take deep breaths and keep the peace going.",
    "Energetic": "Drive safely and channel your energy wisely.",
    "Neutral": "Stay focused and enjoy a balanced drive.",
    "Sad": "Listen to uplifting music or talk to a friend.",
    "Stressed": "Try some relaxation techniques like deep breathing.",
    "Excited": "Keep your enthusiasm in check for safe driving.",
    "Focused": "Maintain your focus and stay comfortable.",
    "Angry": "Try to calm down with some relaxing techniques and music."
}

# List of moods with their specific settings
moods_data = {
    "Happy": {"lighting": 75, "temperature": 22, "seat": "Upright", "color": "#ffcccb", "song": "C:/Users/manas/Downloads/indian-instrumental-with-tabla-and-flute-for-film-and-cinema-249466.mp3"},
    "Calm": {"lighting": 50, "temperature": 20, "seat": "Relaxed", "color": "#add8e6", "song": "C:/Users/manas/Downloads/dreambig.mp3"},
    "Energetic": {"lighting": 85, "temperature": 24, "seat": "Normal", "color": "#ffffcc", "song": "C:/Users/manas/Downloads/onrepeat.mp3"},
    "Neutral": {"lighting": 60, "temperature": 21, "seat": "Normal", "color": "#d3d3d3", "song": "C:/Users/manas/Downloads/hearty.mp3"},
    "Sad": {"lighting": 55, "temperature": 23, "seat": "Relaxed", "color": "#c0c0c0", "song": "C:/Users/manas/Downloads/hearty.mp3"},
    "Stressed": {"lighting": 40, "temperature": 21, "seat": "Reclined", "color": "#afeeee", "song": "C:/Users/manas/Downloads/dreambig.mp3"},
    "Excited": {"lighting": 90, "temperature": 25, "seat": "Upright", "color": "#ffd700", "song": "C:/Users/manas/Downloads/onrepeat.mp3"},
    "Focused": {"lighting": 65, "temperature": 22, "seat": "Normal", "color": "#deb887", "song": "C:/Users/manas/Downloads/hearty.mp3"},
    "Angry": {"lighting": 30, "temperature": 20, "seat": "Reclined", "color": "#ff6666", "song": "C:/Users/manas/Downloads/hearty.mp3"}
}

# Detect a random mood
def detect_mood():
    mood = random.choice(list(moods_data.keys()))
    current_mood.set(mood)
    log_mood(mood)
    apply_mood_settings(mood)

# Log the detected mood
def log_mood(mood):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood_log.append(f"{timestamp}: {mood}")
    mood_history.insert(tk.END, f"{timestamp}: {mood}\n")
    mood_history.see(tk.END)

# Apply settings for the detected mood
def apply_mood_settings(mood):
    settings = moods_data[mood]
    lighting_scale.set(settings["lighting"])
    temperature_scale.set(settings["temperature"])
    seat_label.config(text=f"Seat Adjustment: {settings['seat']}")
    tips_label.config(text=mood_tips.get(mood, "Enjoy your drive!"))
    root.configure(bg=settings["color"])
    play_music(settings["song"])

# Play music for the current mood
def play_music(filename):
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
    except pygame.error:
        messagebox.showerror("Error", f"Music file '{filename}' not found!")

# Pause/Resume music controls
def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

# Continuous mood monitoring every 10 seconds
def monitor_mood():
    detect_mood()  # Detect mood every 10 seconds
    root.after(10000, monitor_mood)  # Repeat after 10 seconds

# GUI Layout
header_frame = Frame(root, bg="#4682B4", height=60)
header_frame.pack(fill="x")
Label(header_frame, text="ZenSense AI - Mood Based Customization", font=("Arial", 18), bg="#4682B4", fg="white").pack(pady=10)

main_frame = Frame(root, bg="#e6f7ff")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Left section: Mood detection and history
left_frame = Frame(main_frame, bg="#e6f7ff")
left_frame.pack(side="left", fill="y", padx=20)

Label(left_frame, text="Current Mood:", font=("Arial", 14), bg="#e6f7ff").pack(anchor="w", pady=5)
mood_label = Label(left_frame, textvariable=current_mood, font=("Arial", 16), fg="blue", bg="#e6f7ff")
mood_label.pack(anchor="w", pady=5)

Button(left_frame, text="Detect Mood", command=detect_mood, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=10)

Label(left_frame, text="Mood History:", font=("Arial", 14), bg="#e6f7ff").pack(anchor="w", pady=10)
mood_history = Text(left_frame, height=15, width=40, bg="#ffffff", font=("Arial", 10))
mood_history.pack(pady=5)
scrollbar = Scrollbar(left_frame, command=mood_history.yview)
scrollbar.pack(side="right", fill="y")
mood_history.configure(yscrollcommand=scrollbar.set)

# Right section: Customization and tips
right_frame = Frame(main_frame, bg="#e6f7ff")
right_frame.pack(side="right", fill="both", expand=True, padx=20)

Label(right_frame, text="Lighting Level:", font=("Arial", 12), bg="#e6f7ff").pack(pady=5)
lighting_scale = Scale(right_frame, from_=0, to=100, orient="horizontal", bg="#e6f7ff")
lighting_scale.pack()

Label(right_frame, text="Temperature (°C):", font=("Arial", 12), bg="#e6f7ff").pack(pady=5)
temperature_scale = Scale(right_frame, from_=16, to=30, orient="horizontal", bg="#e6f7ff")
temperature_scale.pack()

seat_label = Label(right_frame, text="Seat Adjustment: Normal", font=("Arial", 12), bg="#e6f7ff")
seat_label.pack(pady=10)

tips_label = Label(right_frame, text="Enjoy your drive!", font=("Arial", 12), bg="#e6f7ff", wraplength=300, justify="left")
tips_label.pack(pady=10)

Button(right_frame, text="Pause Music", command=pause_music, font=("Arial", 12), bg="#FFA07A").pack(pady=5)
Button(right_frame, text="Resume Music", command=resume_music, font=("Arial", 12), bg="#20B2AA").pack(pady=5)

# Camera display
camera_label = Label(right_frame, bg="#dcdcdc", width=400, height=350)
camera_label.pack(pady=10)

def show_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)
    camera_label.after(10, show_frame)

cap = cv2.VideoCapture(0)
show_frame()

# Start continuous mood monitoring
monitor_mood()

# Start the Tkinter event loop
root.mainloop()

# Release resources
cap.release()
cv2.destroyAllWindows()
