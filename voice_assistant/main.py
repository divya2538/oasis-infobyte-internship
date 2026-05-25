import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import random

# ---------------- ENGINE ----------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    chat_box.insert(tk.END, f"\n🤖 AI: {text}\n")
    chat_box.yview(tk.END)
    engine.say(text)
    engine.runAndWait()


# ---------------- LISTEN ----------------
def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            chat_box.insert(tk.END, "\n🎤 Listening...\n")
            chat_box.yview(tk.END)

            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=6)

        command = r.recognize_google(audio)
        chat_box.insert(tk.END, f"\n🧑 You: {command}\n")
        chat_box.yview(tk.END)

        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that")
    except sr.RequestError:
        speak("Network error")
    except Exception:
        speak("Mic error")

    return ""


# ---------------- COMMANDS ----------------
def handle_command(command):

    if "time" in command:
        speak(datetime.datetime.now().strftime("%H:%M:%S"))

    elif "date" in command:
        speak(datetime.datetime.now().strftime("%d %B %Y"))

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "wikipedia" in command:
        try:
            query = command.replace("wikipedia", "").strip()
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("No results found")

    elif "exit" in command or "stop" in command:
        speak("Goodbye 🌸")
        window.destroy()

    elif command == "":
        pass

    else:
        speak("Command not recognized")


# ---------------- BUTTON ----------------
def start_listening():
    command = listen()
    handle_command(command)


# ---------------- SAKURA PATTERN ANIMATION ----------------
petals = []

def create_petals():
    for i in range(60):
        x = i * 10
        y = random.randint(-700, 0)
        size = random.randint(4, 10)

        speed = random.uniform(1.5, 4.5)
        drift = random.uniform(-1.2, 1.2)

        petal = canvas.create_oval(
            x, y, x + size, y + size,
            fill="#ffb6c1",
            outline=""
        )

        petals.append([petal, speed, drift])


def animate():
    for p in petals:
        petal_id = p[0]
        speed = p[1]
        drift = p[2]

        canvas.move(petal_id, drift, speed)

        x1, y1, x2, y2 = canvas.coords(petal_id)

        if y1 > 720:
            canvas.move(petal_id, random.randint(0, 520), -800)

    window.after(40, animate)


# ---------------- UI ----------------
window = tk.Tk()
window.title("🌸 Sakura Voice Assistant")
window.geometry("520x720")
window.resizable(False, False)

canvas = tk.Canvas(window, width=520, height=720, bg="#120018", highlightthickness=0)
canvas.pack(fill="both", expand=True)

create_petals()
animate()

# ---------------- GLASS FRAME ----------------
frame = tk.Frame(window, bg="#1f0f2e")
frame.place(relx=0.5, rely=0.5, anchor="center")

# TITLE
tk.Label(
    frame,
    text="🌸 SAKURA VOICE ASSISTANT 🌸",
    font=("Arial", 15, "bold"),
    fg="#ff69b4",
    bg="#1f0f2e"
).pack(pady=10)

# CHAT BOX
chat_box = scrolledtext.ScrolledText(
    frame,
    width=45,
    height=20,
    bg="#2a1b3d",
    fg="white",
    font=("Arial", 10),
    wrap=tk.WORD
)
chat_box.pack(pady=10)

chat_box.insert(tk.END, "🤖 AI: Assistant is ready 🌸\n")

# BUTTON
tk.Button(
    frame,
    text="🎤 Speak",
    command=start_listening,
    bg="#ff69b4",
    fg="white",
    relief="flat",
    width=20
).pack(pady=10)

window.mainloop()