import tkinter as tk
import random
import string

# ---------------- STRENGTH CHECK ----------------
def analyze_password(pw):
    score = 0
    suggestions = []

    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    else:
        suggestions.append("🔴 Make it at least 8-12 characters")

    if any(c.islower() for c in pw):
        score += 1
    else:
        suggestions.append("🟡 Add lowercase letters")

    if any(c.isupper() for c in pw):
        score += 1
    else:
        suggestions.append("🟡 Add uppercase letters")

    if any(c.isdigit() for c in pw):
        score += 1
    else:
        suggestions.append("🟡 Add numbers")

    if any(c in string.punctuation for c in pw):
        score += 1
    else:
        suggestions.append("🟣 Add special characters")

    if score <= 2:
        strength = "Weak 💔"
        bar = "🟥🟥⬜⬜⬜"
    elif score <= 4:
        strength = "Medium 💛"
        bar = "🟧🟧🟧⬜⬜"
    else:
        strength = "Strong 💚"
        bar = "🟩🟩🟩🟩🟩"

    return strength, bar, suggestions


# ---------------- LIVE CHECK ----------------
def check_password():
    pw = entry.get()
    if not pw:
        result_label.config(text="Enter a password 🌸")
        return

    strength, bar, tips = analyze_password(pw)

    result_label.config(text=f"{strength}  {bar}")

    suggestion_box.delete("1.0", tk.END)
    if tips:
        for t in tips:
            suggestion_box.insert(tk.END, t + "\n")
    else:
        suggestion_box.insert(tk.END, "✨ Your password is strong!")


# ---------------- GENERATE ----------------
def generate_password():
    length = length_slider.get()
    chars = string.ascii_letters + string.digits + string.punctuation
    pw = ''.join(random.choice(chars) for _ in range(length))

    entry.delete(0, tk.END)
    entry.insert(0, pw)

    check_password()


# ---------------- 🌸 SAKURA ANIMATION ----------------
petals = []

def create_petals():
    for _ in range(40):
        x = random.randint(0, 520)
        y = random.randint(-700, 0)
        size = random.randint(4, 10)
        speed = random.randint(2, 6)

        petal = canvas.create_oval(
            x, y, x + size, y + size,
            fill="#ffb6c1",
            outline=""
        )

        petals.append([petal, speed])


def animate():
    for p in petals:
        canvas.move(p[0], 0, p[1])

        pos = canvas.coords(p[0])

        if pos and pos[1] > 720:
            canvas.move(p[0], random.randint(0, 500), -800)

    window.after(50, animate)


# ---------------- UI ----------------
window = tk.Tk()
window.title("🌸 Password Studio Pro")
window.geometry("520x720")
window.resizable(False, False)

# Background canvas (for petals)
canvas = tk.Canvas(window, width=520, height=720, bg="#120018", highlightthickness=0)
canvas.pack(fill="both", expand=True)

create_petals()
animate()

# Glass frame
frame = tk.Frame(window, bg="#1f0f2e")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
tk.Label(
    frame,
    text="🌸 PASSWORD STUDIO PRO 🌸",
    font=("Arial", 16, "bold"),
    fg="#ff69b4",
    bg="#1f0f2e"
).pack(pady=10)

# INPUT
entry = tk.Entry(
    frame,
    font=("Arial", 14),
    width=28,
    justify="center",
    bg="#2a1b3d",
    fg="#ffb6c1",
    insertbackground="white"
)
entry.pack(pady=10)

# BUTTONS
tk.Button(
    frame,
    text="🔍 Check Strength",
    command=check_password,
    bg="#ff69b4",
    fg="white",
    relief="flat",
    width=20
).pack(pady=5)

tk.Button(
    frame,
    text="✨ Generate Password",
    command=generate_password,
    bg="#8a2be2",
    fg="white",
    relief="flat",
    width=20
).pack(pady=5)

# SLIDER
tk.Label(frame, text="Length", bg="#1f0f2e", fg="white").pack()

length_slider = tk.Scale(
    frame,
    from_=6,
    to=32,
    orient="horizontal",
    bg="#1f0f2e",
    fg="white",
    highlightthickness=0
)
length_slider.set(12)
length_slider.pack()

# RESULT
result_label = tk.Label(
    frame,
    text="Strength: -",
    bg="#1f0f2e",
    fg="white",
    font=("Arial", 13)
)
result_label.pack(pady=10)

# SUGGESTIONS
tk.Label(frame, text="Suggestions 🌸", bg="#1f0f2e", fg="white").pack()

suggestion_box = tk.Text(
    frame,
    height=8,
    width=40,
    bg="#2a1b3d",
    fg="white"
)
suggestion_box.pack()

window.mainloop()