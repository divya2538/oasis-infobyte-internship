import tkinter as tk
from tkinter import messagebox
import json
import os
import random

DATA_FILE = "bmi_history.json"


# ---------------- DATA ----------------
def load_history():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_history(record):
    data = load_history()
    data.append(record)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------- BMI ----------------
def category(bmi):
    if bmi < 18.5:
        return "💗 Underweight"
    elif bmi < 25:
        return "💚 Normal"
    elif bmi < 30:
        return "💛 Overweight"
    else:
        return "❤️ Obese"


def calculate():
    try:
        name = name_entry.get().strip()
        w = float(weight_entry.get())
        h = float(height_entry.get())

        if h > 3:
            h = h / 100

        bmi = w / (h ** 2)
        result = category(bmi)

        result_label.config(
            text=f"🌸 {name} 🌸\nBMI: {bmi:.2f}\n{result}"
        )

        save_history({
            "name": name,
            "weight": w,
            "height": h,
            "bmi": round(bmi, 2),
            "category": result
        })

        update_history()

    except:
        messagebox.showerror("Error", "Enter valid values 💕")


# ---------------- HISTORY ----------------
def update_history():
    history_box.delete("1.0", tk.END)
    for i in load_history()[-6:]:
        history_box.insert(tk.END, f"{i['name']} • {i['bmi']} • {i['category']}\n")


# ---------------- SAKURA ANIMATION ----------------
petals = []


def create_petals():
    for _ in range(30):
        x = random.randint(0, 520)
        y = random.randint(-600, 0)
        size = random.randint(6, 14)
        speed = random.randint(2, 5)
        drift = random.choice([-1, 1])

        petal = canvas.create_oval(
            x, y, x + size, y + size,
            fill="#ffb6c1", outline=""
        )

        petals.append([petal, speed, drift])


def animate():
    for p in petals:
        canvas.move(p[0], p[2], p[1])  # drift + fall

        pos = canvas.coords(p[0])

        if pos and pos[1] > 700:
            canvas.move(p[0], random.randint(0, 520), -800)

    window.after(40, animate)


# ---------------- UI ----------------
window = tk.Tk()
window.title("BMI CALCULATOR")
window.geometry("520x680")
window.resizable(False, False)

canvas = tk.Canvas(window, width=520, height=680, bg="#1a0f1f", highlightthickness=0)
canvas.pack(fill="both", expand=True)

create_petals()
animate()


# MAIN FRAME
frame = tk.Frame(window, bg="#2a1b3d")
frame.place(relx=0.5, rely=0.5, anchor="center")


title = tk.Label(
    frame,
    text="BMI CALCULATOR",
    font=("Arial", 18, "bold"),
    fg="#ff69b4",
    bg="#2a1b3d"
)
title.pack(pady=10)


tk.Label(frame, text="Name", bg="#2a1b3d", fg="white").pack()
name_entry = tk.Entry(frame, bg="#3b2a55", fg="white")
name_entry.pack(pady=5)

tk.Label(frame, text="Weight (kg)", bg="#2a1b3d", fg="white").pack()
weight_entry = tk.Entry(frame, bg="#3b2a55", fg="white")
weight_entry.pack(pady=5)

tk.Label(frame, text="Height (m or cm)", bg="#2a1b3d", fg="white").pack()
height_entry = tk.Entry(frame, bg="#3b2a55", fg="white")
height_entry.pack(pady=5)


tk.Button(
    frame,
    text="Calculate",
    command=calculate,
    bg="#ff69b4",
    fg="white",
    relief="flat"
).pack(pady=10)


result_label = tk.Label(
    frame,
    text="Enter details",
    bg="#2a1b3d",
    fg="#ffd1dc",
    font=("Arial", 13, "bold")
)
result_label.pack(pady=10)


tk.Label(frame, text="History", bg="#2a1b3d", fg="white").pack()

history_box = tk.Text(
    frame,
    height=8,
    width=40,
    bg="#3b2a55",
    fg="white"
)
history_box.pack(pady=10)

update_history()

window.mainloop()