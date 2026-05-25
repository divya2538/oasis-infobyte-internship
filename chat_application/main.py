import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random

# ---------------- BOT LOGIC ----------------
def bot_reply(msg):
    msg = msg.lower()

    if "hello" in msg:
        return "Hey there 🌸💬"
    elif "time" in msg:
        return f"⏰ {datetime.now().strftime('%H:%M:%S')}"
    elif "how are you" in msg:
        return "I'm blooming softly like sakura petals 🌸"
    elif "name" in msg:
        return "I'm Sakura ChatBuddy 🌸"
    elif "bye" in msg:
        return "Goodbye 🌸 Take care!"
    else:
        return "I'm still learning 🌸 try again"


# ---------------- ADD MESSAGE (GLASS BUBBLE STYLE) ----------------
def add_message(sender, msg):
    time = datetime.now().strftime("%H:%M")

    chat.config(state="normal")

    if sender == "You":
        chat.insert(tk.END, f"\n🧑 You • {time}\n{msg}\n", "right")
    else:
        chat.insert(tk.END, f"\n🌸 Bot • {time}\n{msg}\n", "left")

    chat.config(state="disabled")
    chat.yview(tk.END)


# ---------------- SEND MESSAGE ----------------
def send(event=None):
    msg = entry.get().strip()
    if not msg:
        return

    add_message("You", msg)
    entry.delete(0, tk.END)

    reply = bot_reply(msg)
    add_message("Bot", reply)


# ---------------- SAKURA ANIMATION ----------------
def animate():
    for p in petals:
        canvas.move(p[0], 0, p[1])
        pos = canvas.coords(p[0])

        if pos and pos[1] > 720:
            canvas.move(p[0], random.randint(0, 500), -800)

    window.after(50, animate)


def create_petals():
    for _ in range(35):
        x = random.randint(0, 520)
        y = random.randint(-600, 0)
        size = random.randint(5, 12)
        speed = random.randint(2, 5)

        petal = canvas.create_oval(
            x, y, x + size, y + size,
            fill="#ffb6c1",
            outline=""
        )

        petals.append([petal, speed])


# ---------------- UI ----------------
window = tk.Tk()
window.title("🌸 Sakura ChatBuddy Glass")
window.geometry("520x720")
window.resizable(False, False)

# Background canvas
canvas = tk.Canvas(window, width=520, height=720, bg="#0b0014", highlightthickness=0)
canvas.pack(fill="both", expand=True)

petals = []
create_petals()
animate()

# MAIN FRAME (glass effect base)
frame = tk.Frame(window, bg="#1a0f2a")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title = tk.Label(
    frame,
    text="🌸 Sakura ChatBuddy  🌸",
    font=("Arial", 14, "bold"),
    fg="#ff69b4",
    bg="#1a0f2a"
)
title.pack(pady=8)

# CHAT BOX (fixed alignment + glass feel)
chat = scrolledtext.ScrolledText(
    frame,
    width=45,
    height=20,
    bg="#2a1b3d",
    fg="white",
    font=("Arial", 11),
    wrap=tk.WORD,
    borderwidth=0
)

chat.pack(pady=10)
chat.config(state="disabled")

# Proper alignment tags (IMPORTANT FIX)
chat.tag_configure("left", justify="left")
chat.tag_configure("right", justify="right")

# INPUT AREA
entry = tk.Entry(frame, width=30, font=("Arial", 12), bg="#3b2a55", fg="white", insertbackground="white")
entry.pack(side="left", padx=5, pady=10)

send_btn = tk.Button(
    frame,
    text="Send 🌸",
    command=send,
    bg="#ff69b4",
    fg="white",
    relief="flat"
)
send_btn.pack(side="left")

entry.bind("<Return>", send)

# START MESSAGE
add_message("Bot", "Hello 🌸 I'm your Sakura Glass ChatBuddy!")

window.mainloop()